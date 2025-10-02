# Copyright (c) Meta Platforms, Inc. and affiliates.
# Original code from Demucs (https://github.com/facebookresearch/demucs)
# Integrated and adapted for all-in-one-fix
# SPDX-License-Identifier: MIT

"""
Integrated source separation module.

This module provides source separation functionality using Demucs models.
Original code by Meta Platforms, Inc. (demucs v4.1.0a2), integrated from demucsfix.
"""

from .pretrained import get_model, list_models
from .inference import apply_model
from .audio import save_audio, AudioFile, convert_audio, convert_audio_channels

__all__ = [
    'get_model',
    'list_models',
    'apply_model',
    'save_audio',
    'AudioFile',
    'convert_audio',
    'convert_audio_channels',
]
