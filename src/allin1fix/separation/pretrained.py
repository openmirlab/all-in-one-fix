# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
"""Loading pretrained models.
"""

import logging
from pathlib import Path
import typing as tp

from dora.log import fatal, bold

from .models.hdemucs import HDemucs
from .repo import RemoteRepo, LocalRepo, ModelOnlyRepo, BagOnlyRepo, AnyModelRepo, ModelLoadingError  # noqa
from .core.states import _check_diffq

logger = logging.getLogger(__name__)
ROOT_URL = "https://dl.fbaipublicfiles.com/demucs/"
REMOTE_ROOT = Path(__file__).parent / 'remote'

SOURCES = ["drums", "bass", "other", "vocals"]
DEFAULT_MODEL = 'htdemucs'


def demucs_unittest():
    model = HDemucs(channels=4, sources=SOURCES)
    return model


def add_model_flags(parser):
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("-s", "--sig", help="Locally trained XP signature.")
    group.add_argument("-n", "--name", default="htdemucs",
                       help="Pretrained model name or signature. Default is htdemucs.")
    parser.add_argument("--repo", type=Path,
                        help="Folder containing all pre-trained models for use with -n.")


def _parse_remote_files(remote_file_list) -> tp.Dict[str, str]:
    root: str = ''
    models: tp.Dict[str, str] = {}
    for line in remote_file_list.read_text().split('\n'):
        line = line.strip()
        if line.startswith('#'):
            continue
        elif len(line) == 0:
            continue
        elif line.startswith('root:'):
            root = line.split(':', 1)[1].strip()
        else:
            sig = line.split('-', 1)[0]
            assert sig not in models
            models[sig] = ROOT_URL + root + line
    return models


def get_model(name: str,
              repo: tp.Optional[Path] = None):
    """
    Load a pretrained source separation model.

    Parameters
    ----------
    name : str
        Model name (e.g., 'htdemucs', 'htdemucs_ft', 'htdemucs_6s', 'mdx_extra_q')
        Use list_models() to see all available models.
    repo : Optional[Path]
        Optional local model repository path

    Returns
    -------
    model
        Loaded model in eval mode, ready for inference

    Raises
    ------
    ValueError
        If model name is not found
    ImportError
        If required dependencies are missing

    Examples
    --------
    >>> model = get_model('htdemucs')
    >>> print(model.sources)
    ['drums', 'bass', 'other', 'vocals']
    """
    if name == 'demucs_unittest':
        return demucs_unittest()
    model_repo: ModelOnlyRepo
    if repo is None:
        models = _parse_remote_files(REMOTE_ROOT / 'files.txt')
        model_repo = RemoteRepo(models)
        bag_repo = BagOnlyRepo(REMOTE_ROOT, model_repo)
    else:
        if not repo.is_dir():
            fatal(f"{repo} must exist and be a directory.")
        model_repo = LocalRepo(repo)
        bag_repo = BagOnlyRepo(repo, model_repo)
    any_repo = AnyModelRepo(model_repo, bag_repo)

    try:
        model = any_repo.get_model(name)
    except ImportError as exc:
        if 'diffq' in exc.args[0]:
            _check_diffq()
        raise
    except Exception as exc:
        # Provide helpful error message with available models
        available_models = list_models()
        error_msg = (
            f"Model '{name}' not found.\n\n"
            f"Available models:\n"
        )

        # Show first 10 models
        for i, model_name in enumerate(available_models[:10]):
            error_msg += f"  - {model_name}\n"

        if len(available_models) > 10:
            error_msg += f"  ... and {len(available_models) - 10} more\n"

        error_msg += f"\nUse list_models() to see all {len(available_models)} available models."

        # Add suggestion if name is close to an available model
        from difflib import get_close_matches
        suggestions = get_close_matches(name, available_models, n=3, cutoff=0.6)
        if suggestions:
            error_msg += f"\n\nDid you mean: {', '.join(suggestions)}?"

        raise ValueError(error_msg) from exc

    model.eval()
    return model


def get_model_from_args(args):
    """
    Load local model package or pre-trained model.
    """
    if args.name is None:
        args.name = DEFAULT_MODEL
        print(bold("Important: the default model was recently changed to `htdemucs`"),
              "the latest Hybrid Transformer Demucs model. In some cases, this model can "
              "actually perform worse than previous models. To get back the old default model "
              "use `-n mdx_extra_q`.")
    return get_model(name=args.name, repo=args.repo)


def list_models() -> tp.List[str]:
    """
    List available pre-trained models.
    """
    models = _parse_remote_files(REMOTE_ROOT / 'files.txt')
    return list(models.keys())
