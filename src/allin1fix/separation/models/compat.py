"""
Compatibility module for demucsfix to handle old demucs module references.
This allows demucsfix to be a drop-in replacement for demucs.
"""

import sys
from types import ModuleType

# Create a demucs module that imports from demucsfix
class DemucsModule(ModuleType):
    """Compatibility module that redirects imports from demucs to demucsfix."""
    
    def __init__(self):
        super().__init__('demucs')
        
        # Import only essential modules that don't have problematic dependencies
        try:
            from . import separate
            self.separate = separate
        except ImportError:
            # Create a dummy module if import fails
            self.separate = ModuleType('demucs.separate')
        
        try:
            from . import api
            self.api = api
        except ImportError:
            self.api = ModuleType('demucs.api')
        
        try:
            from . import audio
            self.audio = audio
        except ImportError:
            self.audio = ModuleType('demucs.audio')
        
        try:
            from . import apply
            self.apply = apply
        except ImportError:
            self.apply = ModuleType('demucs.apply')
        
        try:
            from . import hdemucs
            self.hdemucs = hdemucs
        except ImportError:
            self.hdemucs = ModuleType('demucs.hdemucs')
        
        try:
            from . import htdemucs
            self.htdemucs = htdemucs
        except ImportError:
            self.htdemucs = ModuleType('demucs.htdemucs')
        
        try:
            from . import demucs
            self.demucs = demucs
        except ImportError:
            self.demucs = ModuleType('demucs.demucs')
        
        try:
            from . import transformer
            self.transformer = transformer
        except ImportError:
            self.transformer = ModuleType('demucs.transformer')
        
        try:
            from . import wav
            self.wav = wav
        except ImportError:
            self.wav = ModuleType('demucs.wav')
        
        try:
            from . import utils
            self.utils = utils
        except ImportError:
            self.utils = ModuleType('demucs.utils')
        
        # Set __version__ for compatibility
        self.__version__ = '4.1.0a2'
        
        # Set __file__ and __path__ for compatibility
        self.__file__ = __file__
        self.__path__ = [__file__.replace('compat.py', '')]

# Create and install the compatibility module
demucs_module = DemucsModule()
sys.modules['demucs'] = demucs_module

# Also handle the case where demucs.separate is imported directly
sys.modules['demucs.separate'] = demucs_module.separate
sys.modules['demucs.api'] = demucs_module.api
sys.modules['demucs.audio'] = demucs_module.audio
sys.modules['demucs.apply'] = demucs_module.apply
sys.modules['demucs.hdemucs'] = demucs_module.hdemucs
sys.modules['demucs.htdemucs'] = demucs_module.htdemucs
sys.modules['demucs.demucs'] = demucs_module.demucs
sys.modules['demucs.transformer'] = demucs_module.transformer
sys.modules['demucs.wav'] = demucs_module.wav
sys.modules['demucs.utils'] = demucs_module.utils
