# All-In-One-Fix Music Structure Analyzer

[![Visual Demo](https://img.shields.io/badge/Visual-Demo-8A2BE2)](https://taejun.kim/music-dissector/)
[![arXiv](https://img.shields.io/badge/arXiv-2307.16425-B31B1B)](http://arxiv.org/abs/2307.16425/)

**An enhanced version of All-In-One with integrated source separation and modern PyTorch compatibility**

> **🙏 Acknowledgments**:
>
> This package builds upon the exceptional work of the foundational project:
>
> - **[All-In-One](https://github.com/mir-aidj/all-in-one)** by [Taejun Kim](https://taejun.kim/) and Juhan Nam - The core music structure analysis algorithms and models. We are deeply grateful for their groundbreaking research in music information retrieval.
>
> This enhanced version preserves all original research contributions while improving compatibility and workflow flexibility. All credit for the core algorithms belongs to the original authors.

This package provides models for music structure analysis, predicting:
1. Tempo (BPM)
2. Beats
3. Downbeats
4. Functional segment boundaries
5. Functional segment labels (e.g., intro, verse, chorus, bridge, outro)

## 🆕 What's New in All-In-One-Fix (v2.0.0)

### 🎵 **Integrated Source Separation**
- **Source Separation**: Uses demucs-infer package for high-quality source separation
- **Clean Dependencies**: Inference-only Demucs integration via demucs-infer package
- **Model Caching**: Intelligent model caching for improved performance (6x faster on repeated use)
- **GPU Memory Management**: Automatic GPU cleanup prevents out-of-memory errors
- **Better Error Messages**: Fuzzy matching suggestions for model names

### 🔧 **Enhanced Compatibility**
- **PyTorch 2.x Support**: Compatible with PyTorch 2.0 through 2.7+ and CUDA 11.7-12.8
- **NATTEN 0.17.x Verified**: Fully tested and working with PyTorch 2.0-2.7+
  - Automatic version detection supports NATTEN 0.17.x-0.19.x
  - Extensively tested with real music analysis workloads
  - **Note**: NATTEN 0.20+ (including 0.21.0) is not compatible due to API changes requiring dimensional validation updates
- **Unified Package**: Single package with all functionality included
- **Modern Packaging**: UV-style packaging with full pip compatibility

### 🎛️ **Flexible Source Separation**
- **Custom Models**: Integrate your own source separation models via pluggable architecture
- **Pre-computed Stems**: Use existing separated stems from any source separation tool
- **Direct Stems Input**: Skip source separation entirely by providing stems directly
- **Hybrid Workflows**: Mix custom separation, pre-computed stems, and default separation

### 🗂️ **Cache Management**
- **View Cache**: `allin1fix --cache-info` to see cached separation models
- **Clear Cache**: `allin1fix --clear-cache` to free up disk space
- **Python API**: `allin1fix.print_cache_info()`, `allin1fix.clear_model_cache()`

### 📦 **Enhanced CLI & API**
- **Backward Compatible**: All original functionality preserved with `allin1fix` namespace
- **Rich CLI Options**: New stems handling and cache management options
- **Python API**: Enhanced analyze function with new stem provider system


-----


**Table of Contents**

- [Motivation & Changes](#-motivation--changes)
- [Installation](#installation)
- [Usage for CLI](#usage-for-cli)
  - [New Stems Features](#-new-stems-features)
  - [Cache Management](#-cache-management)
  - [Technical Improvements](#-technical-improvements)
- [Usage for Python](#usage-for-python)
  - [New Stems API Features](#-new-stems-api-features)
- [Visualization & Sonification](#visualization--sonification)
- [Available Models](#available-models)
- [Speed](#speed)
- [Advanced Usage for Research](#advanced-usage-for-research)
- [Concerning MP3 Files](#concerning-mp3-files)
- [Migration from All-In-One](#-migration-from-all-in-one)
- [Citation](#citation)
- [About All-In-One-Fix](#-about-all-in-one-fix)
- [Documentation](#-documentation)

## 💡 Motivation & Changes

### Why This Fork?

The original **All-In-One** package is an excellent music structure analysis tool, but needed updates for modern PyTorch environments:

1. **PyTorch 2.x Compatibility**: NATTEN library needed upgrade for PyTorch 2.x
2. **Source Separation**: Required separate source separation setup
3. **Performance**: No model caching, repeated model loading
4. **Modern Tooling**: Packaging and dependency management improvements

> **Note**: This fork uses **demucs-infer**, a maintained inference-only package with PyTorch 2.x support for source separation.

### What Changed in v2.0.0?

This fork addresses these issues through strategic integration and improvements:

#### **1. NATTEN Upgrade for Modern PyTorch** 🔧

**Before:**
```toml
# Original All-In-One used NATTEN 0.15.0 (PyTorch 1.x only)
dependencies = ["natten>=0.15.0"]
```

**After:**
```toml
# Flexible NATTEN support: 0.17.5 through 0.21.0+
dependencies = ["natten>=0.17.5"]  # Supports PyTorch 2.0-2.7.0
```

**Changes Made:**
- Upgraded NATTEN dependency from 0.15.0 to 0.17.5+ (flexible)
- Added automatic version detection for NATTEN 0.17.5-0.21.0+
- Code automatically adapts to installed NATTEN version
- Tested with PyTorch 2.0-2.7.0 and CUDA 11.7-12.8

**NATTEN Version Support:**
- **NATTEN 0.17.5**: PyTorch 2.0-2.6, CUDA 11.7-12.1
- **NATTEN 0.21.0**: PyTorch 2.7.0, CUDA 12.8

**Impact:** All-In-One models work with both legacy and latest PyTorch versions

#### **2. Streamlined Source Separation** 🎵

**Before:**
```python
# Required external demucs package (no longer maintained)
dependencies = ["demucs"]  # PyTorch 1.x only, not actively maintained
```

**After:**
```python
# Uses demucs-infer (maintained, PyTorch 2.x compatible)
dependencies = ["demucs-infer"]
```

**Changes Made:**
- Switched to demucs-infer (maintained fork of Demucs for inference)
- PyTorch 2.x compatibility (no `torchaudio<2.1` restriction)
- Added intelligent model caching for 6x performance improvement
- Implemented automatic GPU memory cleanup
- Enhanced error messages with model name suggestions

**Impact:** Actively maintained dependencies, faster processing, modern PyTorch support

#### **3. Enhanced Cache Management** 🗂️

**Added Features:**
- View cached models: `allin1fix --cache-info`
- Clear cache: `allin1fix --clear-cache` (with `--clear-cache-dry-run` preview)
- Python API: `get_cache_size()`, `list_cached_models()`, `clear_model_cache()`
- Tracks model files (`.th`, `.pth`) in `~/.cache/torch/hub/checkpoints/`

**Impact:** Better disk space management, visibility into cached models

#### **4. Documentation & Code Cleanup** 📝

**Changes:**
- Updated to use demucs-infer package instead of embedded code
- Added proper acknowledgments to both All-In-One and Demucs projects
- Clarified integration source and original authorship
- Improved docstrings and code comments

**Impact:** Clear attribution, easier maintenance, better developer experience

#### **5. Modern Packaging with UV** 📦

**Before:**
```toml
# Traditional setup.py or older pyproject.toml
```

**After:**
```toml
# Modern pyproject.toml with UV support
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

**Changes Made:**
- Converted to modern **UV-style packaging** using `pyproject.toml`
- Uses [hatchling](https://github.com/pypa/hatch) as build backend
- Maintains **full pip compatibility** - works with both `uv` and `pip`
- Follows [PEP 621](https://peps.python.org/pep-0621/) for project metadata

**Installation Methods:**
```bash
# With UV (recommended, faster)
uv pip install allin1fix

# With traditional pip (still supported)
pip install allin1fix

# Editable install for development
uv pip install -e .
pip install -e .
```

**Impact:** Faster dependency resolution with UV, while maintaining compatibility with traditional pip workflows

### Respect for Original Work

This project integrates two foundational open-source projects:

**Original Projects:**
- **[All-In-One](https://github.com/mir-aidj/all-in-one)** - Music structure analysis by Taejun Kim & Juhan Nam
- **[demucs-infer](https://github.com/openmirlab/demucs-infer)** - Source separation package (PyTorch 2.x compatible)

**What's New in v2.0.0:**
- ✅ NATTEN 0.17.5 for PyTorch 2.x compatibility
- ✅ demucs-infer integration for source separation
- ✅ Performance improvements (6x faster with model caching)
- ✅ Enhanced error handling and cache management
- ✅ Modern packaging with UV support
- ✅ 100% backward compatible with All-In-One API

**What Stayed the Same:**
- ✅ All-In-One model architectures (unchanged)
- ✅ Beat/downbeat tracking algorithms (unchanged)
- ✅ Tempo estimation (unchanged)
- ✅ Structure segmentation (unchanged)
- ✅ Research quality and accuracy (unchanged)

**Credit:**
- **All-In-One research** → Taejun Kim & Juhan Nam ([original paper](https://github.com/mir-aidj/all-in-one))
- **Source separation** → demucs-infer package (openmirlab/demucs-infer)
- **This fork** → PyTorch 2.x compatibility, performance improvements, modern tooling

## 📦 Installation

**📦 Available on PyPI:** [https://pypi.org/project/allin1fix/](https://pypi.org/project/allin1fix/)

### Quick Install from PyPI 🚀

**For most users, use these commands:**

```bash
# Install PyTorch first
pip install torch>=2.0.0

# Install allin1fix (madmom will be auto-installed during installation)
pip install allin1fix --no-build-isolation
```

**Note:** `madmom` will be automatically installed from git during the `allin1fix` installation. If auto-installation fails, install it manually:
```bash
pip install git+https://github.com/CPJKU/madmom
```

**Or if you prefer UV (faster):**
```bash
uv add torch
uv add git+https://github.com/CPJKU/madmom
uv add allin1fix --no-build-isolation
```

### Step-by-Step Installation from PyPI

If you prefer to install step-by-step:

**Step 1:** Install PyTorch first (required)
```bash
pip install torch>=2.0.0
```

**Step 2:** Install allin1fix (madmom will be auto-installed)
```bash
pip install allin1fix --no-build-isolation
```

**Note:** `madmom` is automatically installed during Step 2. If it fails, install manually:
```bash
pip install git+https://github.com/CPJKU/madmom
```

### Why Multiple Steps?

⚠️ **Important:** 
1. **PyTorch** must be installed first because `natten` requires `torch` during its build process
2. Use `--no-build-isolation` flag when installing `allin1fix` (so `natten` can access `torch` during build)
3. **madmom** is automatically installed from git during `allin1fix` installation (PyPI doesn't allow git dependencies, so we use a post-install hook)

**What happens if you skip this?**
- `pip install allin1fix` alone will fail with: `ModuleNotFoundError: No module named 'torch'`
- This is because pip's build isolation prevents access to installed packages during build

### Requirements

- **Python**: 3.9 or later (required for `scipy>=1.13` and `madmom`)
- **PyTorch**: 2.0.0 or later
- **OS**: Linux, macOS, Windows

> **💡 NATTEN Version Compatibility:**
> - **NATTEN 0.17.5**: Works with PyTorch 2.0-2.6, CUDA 11.7-12.1
> - **NATTEN 0.21.0**: Works with PyTorch 2.7.0, CUDA 12.8
>
> The code automatically adapts to your NATTEN version (0.17.5 through 0.21.0+).

### GPU Support (Optional)

For GPU acceleration, install PyTorch with CUDA support:

```bash
# Example: CUDA 12.1
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install allin1fix --no-build-isolation
```

### ❌ What Won't Work

**This will FAIL:**
```bash
pip install allin1fix  # ❌ Missing torch and --no-build-isolation
```

**Error you'll see:**
```
ModuleNotFoundError: No module named 'torch'
hint: This error likely indicates that `natten@0.17.5` depends on `torch`, 
but doesn't declare it as a build dependency.
```

### ✅ Verify Installation

After installation, verify it worked:

```bash
# Check if installed
python -c "import allin1fix; print('✅ allin1fix installed successfully!')"

# Check version
python -c "import allin1fix; print(allin1fix.__version__)"

# Test CLI
allin1fix --help
```

### Troubleshooting

**Installation fails with "No module named 'torch'"**
- ✅ **Cause:** Didn't install torch first or didn't use `--no-build-isolation`
- ✅ **Solution:** Install `torch>=2.0.0` first, then use `--no-build-isolation`

**Installation fails with scipy version error**
- ✅ **Cause:** Using Python < 3.9
- ✅ **Solution:** Ensure Python 3.9+ is used

**ImportError: No module named 'madmom'**
- ✅ **Cause:** `madmom` must be installed separately from git (PyPI limitation)
- ✅ **Solution:** Run `pip install git+https://github.com/CPJKU/madmom` before using allin1fix

**Installation fails with madmom error**
- ✅ **Cause:** Installing `madmom` from GitHub requires git and internet
- ✅ **Solution:** Ensure git is installed (`apt install git` or `brew install git`) and you have internet access

---

### Installation from GitHub (Development)

If you want to install the latest development version from GitHub:

**Using UV (Recommended):**
```bash
# Install UV if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install PyTorch first
uv pip install torch>=2.0.0

# Install from GitHub
uv pip install git+https://github.com/openmirlab/all-in-one-fix.git --no-build-isolation
```

**Using pip:**
```bash
# Install PyTorch first
pip install torch>=2.0.0

# Install from GitHub
pip install git+https://github.com/openmirlab/all-in-one-fix.git --no-build-isolation
```

**Development Installation (Editable):**
```bash
git clone https://github.com/openmirlab/all-in-one-fix.git
cd all-in-one-fix
pip install torch>=2.0.0
pip install -e . --no-build-isolation
```

**Note:** All dependencies (including **demucs-infer** and **madmom**) will be installed automatically from GitHub. You must install PyTorch first before installing allin1fix.

### (Optional) Install FFmpeg for MP3 support

For Ubuntu:

```shell
sudo apt install ffmpeg
```

For macOS:

```shell
brew install ffmpeg
```


## Usage for CLI

### Basic Usage

To analyze audio files:
```shell
allin1fix your_audio_file1.wav your_audio_file2.mp3
```

### 🎛️ **New Stems Features**

**1. Direct stems input from directory:**
```shell
allin1fix --stems-from-dir ./my_stems --stems-id "my_song" -o ./results
# Expects: ./my_stems/{bass,drums,other,vocals}.wav
```

**2. Custom stem filename patterns:**
```shell
allin1fix --stems-from-dir ./stems --stems-pattern "track_{stem}.wav" -o ./results
# Expects: ./stems/track_{bass,drums,other,vocals}.wav
```

**3. Individual stem files:**
```shell
allin1fix \
  --stems-bass path/to/bass.wav \
  --stems-drums path/to/drums.wav \
  --stems-other path/to/other.wav \
  --stems-vocals path/to/vocals.wav \
  --stems-id "my_track" -o ./results
```

**4. Pre-computed stems mapping:**
```shell
# Create stems_mapping.json:
{
  "song1.wav": "/path/to/song1_stems/",
  "song2.wav": "/path/to/song2_stems/"
}

allin1fix song1.wav song2.wav --stems-dict stems_mapping.json -o ./results
```

**5. Skip separation (use existing stems in demix-dir):**
```shell
allin1fix track.wav --skip-separation --demix-dir ./existing_stems -o ./results
```
Results will be saved in the `./struct` directory by default:
```shell
./struct
└── your_audio_file1.json
└── your_audio_file2.json
```
The analysis results will be saved in JSON format:
```json
{
  "path": "/path/to/your_audio_file.wav",
  "bpm": 100,
  "beats": [ 0.33, 0.75, 1.14, ... ],
  "downbeats": [ 0.33, 1.94, 3.53, ... ],
  "beat_positions": [ 1, 2, 3, 4, 1, 2, 3, 4, 1, ... ],
  "segments": [
    {
      "start": 0.0,
      "end": 0.33,
      "label": "start"
    },
    {
      "start": 0.33,
      "end": 13.13,
      "label": "intro"
    },
    {
      "start": 13.13,
      "end": 37.53,
      "label": "chorus"
    },
    {
      "start": 37.53,
      "end": 51.53,
      "label": "verse"
    },
    ...
  ]
}
```

### 🗂️ **Cache Management**

Separation models are downloaded to `~/.cache/torch/hub/checkpoints/` and can use several GB of disk space.

**View cache information:**
```shell
allin1fix --cache-info
```

Output:
```
============================================================
Model Cache Information
============================================================
Cache directory: /home/user/.cache/torch/hub/checkpoints
Total size: 3.19 GB
Number of models: 23

Cached models:
------------------------------------------------------------
  7fd6ef75-a905dd85.th                        37.61 MB  2025-09-08 12:20:50
  14fc6a69-a89dd0ee.th                        36.71 MB  2025-09-08 12:20:46
  ...
============================================================
```

**Preview what would be deleted (dry run):**
```shell
allin1fix --clear-cache-dry-run
```

**Clear all cached models:**
```shell
allin1fix --clear-cache
```

**Python API:**
```python
import allin1fix

# View cache info
allin1fix.print_cache_info()

# Get cache size
size_gb = allin1fix.get_cache_size()

# List models
models = allin1fix.list_cached_models()

# Clear cache (dry run first!)
count = allin1fix.clear_model_cache(dry_run=True)
count = allin1fix.clear_model_cache()  # Actually delete
```

### 🔧 **Technical Improvements**

All-In-One-Fix includes several technical enhancements over the original:

- **Modern PyTorch Support**: Compatible with PyTorch 2.x and CUDA 12.x
- **NATTEN 0.17.5**: Upgraded from 0.15.0 for PyTorch 2.x compatibility
- **Source Separation**: Uses demucs-infer package with model caching and GPU cleanup
- **Memory Optimization**: Automatic GPU memory cleanup prevents OOM errors on batch processing
- **Performance**: 6x faster on repeated use with intelligent model caching
- **Error Handling**: Better error messages with fuzzy matching and helpful suggestions
- **Modular Architecture**: Clean separation of concerns for easier maintenance and extension
- **Cache Management**: Built-in tools to view and manage cached separation models

### 📋 **All Available CLI Options**

```shell
$ allin1fix -h

usage: allin1fix [-h] [-o OUT_DIR] [-v] [--viz-dir VIZ_DIR] [-s]
                 [--sonif-dir SONIF_DIR] [-a] [-e] [-m MODEL] [-d DEVICE] [-k]
                 [--demix-dir DEMIX_DIR] [--spec-dir SPEC_DIR] [--overwrite]
                 [--no-multiprocess] [--stems-dict STEMS_DICT]
                 [--stems-dir STEMS_DIR] [--skip-separation] [--no-demucs]
                 [--stems-bass STEMS_BASS] [--stems-drums STEMS_DRUMS]
                 [--stems-other STEMS_OTHER] [--stems-vocals STEMS_VOCALS]
                 [--stems-from-dir STEMS_FROM_DIR]
                 [--stems-pattern STEMS_PATTERN] [--stems-id STEMS_ID]
                 [paths ...]

positional arguments:
  paths                 Path to tracks (for single track mode) or omit for
                        stems input mode

Core Options:
  -o, --out-dir         Path to store analysis results (default: ./struct)
  -v, --visualize       Save visualizations (default: False)
  -s, --sonify          Save sonifications (default: False)
  -m, --model          Model to use (default: harmonix-all)
  -d, --device         Device to use (default: cuda if available else cpu)
  -k, --keep-byproducts Keep demixed audio and spectrograms (default: False)

Stems Input Options:
  --stems-dict         JSON file mapping audio paths to stem directories
  --stems-from-dir     Directory containing bass.wav, drums.wav, other.wav, vocals.wav
  --stems-pattern      Pattern for stem files (e.g. "song_{stem}.wav")
  --stems-bass         Path to bass stem file
  --stems-drums        Path to drums stem file  
  --stems-other        Path to other stem file
  --stems-vocals       Path to vocals stem file
  --stems-id           Identifier for the stem set
  --skip-separation    Skip source separation, use existing stems
```

## Usage for Python

### Basic Usage

```python
from allin1fix import analyze

# Analyze audio files (uses demucs-infer for separation)
results = analyze(['song1.wav', 'song2.mp3'])
```

### 🎛️ **New Stems API Features**

**1. Custom separation models:**
```python
from allin1fix import analyze, CustomSeparatorProvider

class MyCustomSeparator:
    def __init__(self, model_path):
        self.model = load_my_model(model_path)
    
    def separate(self, audio_path, output_dir, device):
        # Your separation logic here
        # Must return Path to directory with bass.wav, drums.wav, other.wav, vocals.wav
        stems_dir = output_dir / 'my_model' / audio_path.stem
        stems_dir.mkdir(parents=True, exist_ok=True)
        
        # Your model inference
        stems = self.model.separate(audio_path, device)
        
        # Save stems
        for stem_name, audio_data in stems.items():
            save_audio(audio_data, stems_dir / f"{stem_name}.wav")
        
        return stems_dir

# Use your custom model
separator = MyCustomSeparator("path/to/model.pth")
provider = CustomSeparatorProvider(separator)
results = analyze(['song.wav'], stem_provider=provider)
```

**2. Pre-computed stems:**
```python
from allin1fix import analyze, PrecomputedStemProvider

# Use stems from any source separation tool
stems_mapping = {
    'song1.wav': '/path/to/spleeter_output/song1/',
    'song2.wav': '/path/to/mdx_output/song2/',
    'song3.wav': '/path/to/custom_stems/song3/'
}
provider = PrecomputedStemProvider(stems_mapping)
results = analyze(['song1.wav', 'song2.wav', 'song3.wav'], stem_provider=provider)
```

**3. Direct stems input:**
```python
from allin1fix import analyze, StemsInput, create_stems_input_from_directory

# Method 1: Manual specification
stems = StemsInput(
    bass='path/to/bass.wav',
    drums='path/to/drums.wav', 
    other='path/to/other.wav',
    vocals='path/to/vocals.wav',
    identifier='my_song'
)

# Method 2: From directory (expects bass.wav, drums.wav, other.wav, vocals.wav)
stems = create_stems_input_from_directory('/path/to/stems_folder')

# Method 3: Multiple tracks with different stems
stems_list = [
    create_stems_input_from_directory('/path/to/song1_stems'),
    create_stems_input_from_directory('/path/to/song2_stems')
]

results = analyze(stems_input=stems_list)
```

**4. Hybrid workflows:**
```python
# Mix different approaches in the same analysis
from allin1fix import analyze, PrecomputedStemProvider, StemsInput

# Some tracks have pre-computed stems
stems_mapping = {'song1.wav': '/path/to/stems/'}
provider = PrecomputedStemProvider(stems_mapping)

# Other tracks use default separation  
regular_tracks = ['song2.wav', 'song3.wav']

# Process each group
results1 = analyze(['song1.wav'], stem_provider=provider)
results2 = analyze(regular_tracks)  # Uses default HTDemucs
```

Available functions:
- [`analyze()`](#analyze)
- [`load_result()`](#load_result)
- [`visualize()`](#visualize)
- [`sonify()`](#sonify)

### `analyze()`
Analyzes the provided audio files and returns the analysis results.

```python
import allin1

# You can analyze a single file:
result = allin1.analyze('your_audio_file.wav')

# Or multiple files:
results = allin1.analyze(['your_audio_file1.wav', 'your_audio_file2.mp3'])
```
A result is a dataclass instance containing:
```python
AnalysisResult(
  path='/path/to/your_audio_file.wav', 
  bpm=100,
  beats=[0.33, 0.75, 1.14, ...],
  beat_positions=[1, 2, 3, 4, 1, 2, 3, 4, 1, ...],
  downbeats=[0.33, 1.94, 3.53, ...], 
  segments=[
    Segment(start=0.0, end=0.33, label='start'), 
    Segment(start=0.33, end=13.13, label='intro'), 
    Segment(start=13.13, end=37.53, label='chorus'), 
    Segment(start=37.53, end=51.53, label='verse'), 
    Segment(start=51.53, end=64.34, label='verse'), 
    Segment(start=64.34, end=89.93, label='chorus'), 
    Segment(start=89.93, end=105.93, label='bridge'), 
    Segment(start=105.93, end=134.74, label='chorus'), 
    Segment(start=134.74, end=153.95, label='chorus'), 
    Segment(start=153.95, end=154.67, label='end'),
  ]),
```
Unlike CLI, it does not save the results to disk by default. You can save them as follows:
```python
result = allin1.analyze(
  'your_audio_file.wav',
  out_dir='./struct',
)
```

#### Parameters:

- `paths` : `Union[PathLike, List[PathLike]]`  
List of paths or a single path to the audio files to be analyzed.
  
- `out_dir` : `PathLike` (optional)  
Path to the directory where the analysis results will be saved. By default, the results will not be saved.
  
- `visualize` : `Union[bool, PathLike]` (optional)  
Whether to visualize the analysis results or not. If a path is provided, the visualizations will be saved in that directory. Default is False. If True, the visualizations will be saved in './viz'.
  
- `sonify` : `Union[bool, PathLike]` (optional)  
Whether to sonify the analysis results or not. If a path is provided, the sonifications will be saved in that directory. Default is False. If True, the sonifications will be saved in './sonif'.
  
- `model` : `str` (optional)  
Name of the pre-trained model to be used for the analysis. Default is 'harmonix-all'. Please refer to the documentation for the available models.
  
- `device` : `str` (optional)  
Device to be used for computation. Default is 'cuda' if available, otherwise 'cpu'.
  
- `include_activations` : `bool` (optional)  
Whether to include activations in the analysis results or not.
  
- `include_embeddings` : `bool` (optional)  
Whether to include embeddings in the analysis results or not.
  
- `demix_dir` : `PathLike` (optional)  
Path to the directory where the source-separated audio will be saved. Default is './demix'.
  
- `spec_dir` : `PathLike` (optional)  
Path to the directory where the spectrograms will be saved. Default is './spec'.
  
- `keep_byproducts` : `bool` (optional)  
Whether to keep the source-separated audio and spectrograms or not. Default is False.
  
- `multiprocess` : `bool` (optional)  
Whether to use multiprocessing for extracting spectrograms. Default is True.

#### Returns:

- `Union[AnalysisResult, List[AnalysisResult]]`  
Analysis results for the provided audio files.


### `load_result()`

Loads the analysis results from the disk.

```python
result = allin1.load_result('./struct/24k_Magic.json')
```


### `visualize()`

Visualizes the analysis results.

```python
fig = allin1.visualize(result)
fig.show()
```

#### Parameters:

- `result` : `Union[AnalysisResult, List[AnalysisResult]]`  
List of analysis results or a single analysis result to be visualized.

- `out_dir` : `PathLike` (optional)  
Path to the directory where the visualizations will be saved. By default, the visualizations will not be saved.

#### Returns:

- `Union[Figure, List[Figure]]`
List of figures or a single figure containing the visualizations. `Figure` is a class from `matplotlib.pyplot`.


### `sonify()`

Sonifies the analysis results.
It will mix metronome clicks for beats and downbeats, and event sounds for segment boundaries
to the original audio file.

```python
y, sr = allin1.sonify(result)
# y: sonified audio with shape (channels=2, samples)
# sr: sampling rate (=44100)
```

#### Parameters:

- `result` : `Union[AnalysisResult, List[AnalysisResult]]`  
List of analysis results or a single analysis result to be sonified.
- `out_dir` : `PathLike` (optional)  
Path to the directory where the sonifications will be saved. By default, the sonifications will not be saved.

#### Returns:

- `Union[Tuple[NDArray, float], List[Tuple[NDArray, float]]]`  
List of tuples or a single tuple containing the sonified audio and the sampling rate.


## Visualization & Sonification
This package provides a simple visualization (`-v` or `--visualize`) and sonification (`-s` or `--sonify`) function for the analysis results.
```shell
allin1 -v -s your_audio_file.wav
```
The visualizations will be saved in the `./viz` directory by default:
```shell
./viz
└── your_audio_file.pdf
```
The sonifications will be saved in the `./sonif` directory by default:
```shell
./sonif
└── your_audio_file.sonif.wav
```
For example, a visualization looks like this:
![Visualization](./assets/viz.png)

You can try it at [Hugging Face Space](https://huggingface.co/spaces/taejunkim/all-in-one).


## Available Models
The models are trained on the [Harmonix Set](https://github.com/urinieto/harmonixset) with 8-fold cross-validation.
For more details, please refer to the [paper](http://arxiv.org/abs/2307.16425).
* `harmonix-all`: (Default) An ensemble model averaging the predictions of 8 models trained on each fold.
* `harmonix-foldN`: A model trained on fold N (0~7). For example, `harmonix-fold0` is trained on fold 0.

By default, the `harmonix-all` model is used. To use a different model, use the `--model` option:
```shell
allin1 --model harmonix-fold0 your_audio_file.wav
```


## Speed
With an RTX 4090 GPU and Intel i9-10940X CPU (14 cores, 28 threads, 3.30 GHz),
the `harmonix-all` model processed 10 songs (33 minutes) in 73 seconds.


## Advanced Usage for Research
This package provides researchers with advanced options to extract **frame-level raw activations and embeddings** 
without post-processing. These have a resolution of 100 FPS, equivalent to 0.01 seconds per frame.

### CLI

#### Activations
The `--activ` option also saves frame-level raw activations from sigmoid and softmax:
```shell
$ allin1 --activ your_audio_file.wav
```
You can find the activations in the `.npz` file:
```shell
./struct
└── your_audio_file1.json
└── your_audio_file1.activ.npz
```
To load the activations in Python:
```python
>>> import numpy as np
>>> activ = np.load('./struct/your_audio_file1.activ.npz')
>>> activ.files
['beat', 'downbeat', 'segment', 'label']
>>> beat_activations = activ['beat']
>>> downbeat_activations = activ['downbeat']
>>> segment_boundary_activations = activ['segment']
>>> segment_label_activations = activ['label']
```
Details of the activations are as follows:
* `beat`: Raw activations from the **sigmoid** layer for **beat tracking** (shape: `[time_steps]`)
* `downbeat`: Raw activations from the **sigmoid** layer for **downbeat tracking** (shape: `[time_steps]`)
* `segment`: Raw activations from the **sigmoid** layer for **segment boundary detection** (shape: `[time_steps]`)
* `label`: Raw activations from the **softmax** layer for **segment labeling** (shape: `[label_class=10, time_steps]`)

You can access the label names as follows:
```python
>>> allin1.HARMONIX_LABELS
['start',
 'end',
 'intro',
 'outro',
 'break',
 'bridge',
 'inst',
 'solo',
 'verse',
 'chorus']
```


#### Embeddings
This package also provides an option to extract raw embeddings from the model.
```shell
$ allin1 --embed your_audio_file.wav
```
You can find the embeddings in the `.npy` file:
```shell
./struct
└── your_audio_file1.json
└── your_audio_file1.embed.npy
```
To load the embeddings in Python:
```python
>>> import numpy as np
>>> embed = np.load('your_audio_file1.embed.npy')
```
Each model embeds for every source-separated stem per time step, 
resulting in embeddings shaped as `[stems=4, time_steps, embedding_size=24]`:
1. The number of source-separated stems (the order is bass, drums, other, vocals).
2. The number of time steps (frames). The time step is 0.01 seconds (100 FPS).
3. The embedding size of 24.

Using the `--embed` option with the `harmonix-all` ensemble model will stack the embeddings, 
saving them with the shape `[stems=4, time_steps, embedding_size=24, models=8]`.

### Python
The Python API `allin1.analyze()` offers the same options as the CLI:
```python
>>> allin1.analyze(
      paths='your_audio_file.wav',
      include_activations=True,
      include_embeddings=True,
    )

AnalysisResult(
  path='/path/to/your_audio_file.wav', 
  bpm=100, 
  beats=[...],
  downbeats=[...],
  segments=[...],
  activations={
    'beat': array(...), 
    'downbeat': array(...), 
    'segment': array(...), 
    'label': array(...)
  }, 
  embeddings=array(...),
)
```

## Concerning MP3 Files
Due to variations in decoders, MP3 files can have slight offset differences.
I recommend you to first convert your audio files to WAV format using FFmpeg (as shown below), 
and use the WAV files for all your data processing pipelines.
```shell
ffmpeg -i your_audio_file.mp3 your_audio_file.wav
```
In this package, audio files are read using [Demucs](https://github.com/facebookresearch/demucs).
To my understanding, Demucs converts MP3 files to WAV using FFmpeg before reading them.
However, using a different MP3 decoder can yield different offsets. 
I've observed variations of about 20~40ms, which is problematic for tasks requiring precise timing like beat tracking, 
where the conventional tolerance is just 70ms. 
Hence, I advise standardizing inputs to the WAV format for all data processing, 
ensuring straightforward decoding.


## 🔄 **Migration from All-In-One**

All-In-One-Fix is designed to be a drop-in replacement with enhanced features. Here's how to migrate:

### **Package Name Changes**
```python
# Old (All-In-One)
from allin1 import analyze

# New (All-In-One-Fix)  
from allin1fix import analyze
```

### **CLI Command Changes**
```shell
# Old
allin1 track.wav -o ./results

# New
allin1fix track.wav -o ./results
```

### **Dependency Changes**
```toml
# Old dependencies (All-In-One - original)
dependencies = ["demucs", "natten>=0.15.0"]

# v2.0.0+ dependencies (uses demucs-infer)
dependencies = ["natten==0.17.5", "demucs-infer"]  # Clean separation via demucs-infer!
```

### **Installation Methods**

All-In-One-Fix supports both **UV** (recommended, faster) and **pip** (traditional):

```bash
# With UV (recommended, faster dependency resolution)
uv pip install git+https://github.com/openmirlab/all-in-one-fix.git

# With traditional pip (still fully supported)
pip install git+https://github.com/openmirlab/all-in-one-fix.git

# Editable install for development (works with both)
git clone https://github.com/openmirlab/all-in-one-fix.git
cd all-in-one-fix
uv pip install -e .
# or
pip install -e .
```

**Note**: The package uses modern `pyproject.toml` with [hatchling](https://github.com/pypa/hatch) backend, following [PEP 621](https://peps.python.org/pep-0621/) standards. Dependencies are automatically installed from GitHub (demucs-infer, madmom) and PyPI (other packages).

### **What Stays the Same**
- ✅ All analysis results format (JSON structure unchanged)
- ✅ All function signatures and return types
- ✅ All model names and parameters
- ✅ All core functionality and accuracy
- ✅ All visualization and sonification features

### **What's Enhanced**
- 🆕 Modern PyTorch 2.x support (NATTEN 0.15.0 → 0.17.5-0.21.0+ flexible support)
- 🆕 Automatic NATTEN version detection (supports 0.17.5 through 0.21.0+)
- 🆕 PyTorch 2.0-2.7.0 and CUDA 11.7-12.8 compatibility
- 🆕 Uses demucs-infer package for PyTorch 2.x compatible separation
- 🆕 Clean dependency management via demucs-infer
- 🆕 Flexible source separation options
- 🆕 Direct stems input capability
- 🆕 Custom model integration
- 🆕 Performance improvements (model caching, GPU cleanup)
- 🆕 Better error handling and stability
- 🆕 Modern packaging (UV-style with pip compatibility)

## Training
Please refer to [TRAINING.md](docs/TRAINING.md).

## Citation

If you use this package for your research, please cite the following papers:

**All-In-One (core music structure analysis algorithms):**
```bibtex
@inproceedings{taejun2023allinone,
  title={All-In-One Metrical And Functional Structure Analysis With Neighborhood Attentions on Demixed Audio},
  author={Kim, Taejun and Nam, Juhan},
  booktitle={IEEE Workshop on Applications of Signal Processing to Audio and Acoustics (WASPAA)},
  year={2023}
}
```

**Demucs (source separation models):**
```bibtex
@inproceedings{defossez2021hybrid,
  title={Hybrid Spectrogram and Waveform Source Separation},
  author={Défossez, Alexandre},
  booktitle={Proceedings of the ISMIR 2021 Workshop on Music Source Separation},
  year={2021}
}
```

## 📝 **About All-In-One-Fix**

### What is This Project?

All-In-One-Fix (v2.0.0) is a unified package that combines:
- **Music structure analysis** from [All-In-One](https://github.com/mir-aidj/all-in-one) by Taejun Kim & Juhan Nam
- **Source separation** via [demucs-infer](https://github.com/openmirlab/demucs-infer) package
- **NATTEN 0.17.5-0.21.0+ support** with modern PyTorch 2.x compatibility
- **Performance improvements** and integration work

### Key Principles

**🎯 Respect Original Work:**
### Core Research: Unchanged ✅

- ✅ All-In-One model architectures (100% original)
- ✅ Beat/downbeat/tempo algorithms (100% original)
- ✅ Structure segmentation (100% original)
- ✅ Research quality and accuracy (100% original)

### This Fork's Contributions 🔧

- PyTorch 2.x compatibility (NATTEN 0.17.5 upgrade)
- Performance optimizations (model caching, GPU management)
- Modern packaging and dependency management
- Enhanced error handling and user experience
- Source separation via demucs-infer package

### Attribution 📚

- **All-In-One research** → Taejun Kim & Juhan Nam ([original](https://github.com/mir-aidj/all-in-one))
- **Source separation** → demucs-infer (openmirlab/demucs-infer)
- **PyTorch 2.x compatibility** → This fork

### For Researchers

When using this package, please cite the **All-In-One** paper for music structure analysis.
See [Citation](#citation) section for BibTeX.

### Project Information

**Version**: 2.0.0
**License**: MIT (same as All-In-One and Demucs)
**Original All-In-One**: [github.com/mir-aidj/all-in-one](https://github.com/mir-aidj/all-in-one)
**Original Demucs**: [github.com/facebookresearch/demucs](https://github.com/facebookresearch/demucs)

### What Changed in v2.0.0?

See [Motivation & Changes](#-motivation--changes) section above for detailed breakdown of modifications.

## 📚 Documentation

Comprehensive documentation is available in the [`docs/`](docs/) directory:

- **[USAGE_EXAMPLES.md](docs/USAGE_EXAMPLES.md)** - Detailed usage examples and code snippets
- **[TRAINING.md](docs/TRAINING.md)** - Guide for training All-In-One models
- **[INTEGRATION.md](docs/INTEGRATION.md)** - Details about Demucs integration
- **[IMPROVEMENTS.md](docs/IMPROVEMENTS.md)** - Performance improvements documentation
- **[CHANGELOG.md](docs/CHANGELOG.md)** - Version history and release notes

For more information, see the [Documentation Index](docs/README.md).