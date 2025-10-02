#!/usr/bin/env python3
"""
Test the original all-in-one package.
"""

import sys
import traceback
from pathlib import Path

def test_allin1_original():
    """Test the original all-in-one package."""
    try:
        # Import the package
        import allin1
        print("✅ Successfully imported allin1 (original)")
        
        # Check available functions
        funcs = [attr for attr in dir(allin1) if not attr.startswith('_')]
        print(f"Available functions: {funcs}")
        
        # Test with the existing test audio
        test_audio_path = Path("test_audio_original.wav")
        if not test_audio_path.exists():
            print(f"❌ Test audio file not found: {test_audio_path}")
            return
        
        print(f"🎵 Testing analysis with: {test_audio_path}")
        
        # Run analysis
        result = allin1.analyze(str(test_audio_path), keep_byproducts=False)
        print("✅ Analysis completed successfully!")
        
        # Print basic results
        print(f"Result type: {type(result)}")
        
        # Check for common attributes
        attrs_to_check = ['bpm', 'beats', 'downbeats', 'segments', 'beat_positions']
        for attr in attrs_to_check:
            if hasattr(result, attr):
                value = getattr(result, attr)
                print(f"  - {attr}: {type(value)} (len={len(value) if hasattr(value, '__len__') else 'N/A'})")
            else:
                print(f"  - {attr}: NOT FOUND")
        
        # Save result details to file
        result_file = Path("test_original_result.txt")
        with open(result_file, 'w') as f:
            f.write(f"Original all-in-one analysis result\n")
            f.write(f"====================================\n\n")
            f.write(f"Result type: {type(result)}\n")
            f.write(f"Result attributes: {dir(result)}\n\n")
            
            for attr in attrs_to_check:
                if hasattr(result, attr):
                    value = getattr(result, attr)
                    f.write(f"{attr}:\n")
                    f.write(f"  Type: {type(value)}\n")
                    
                    if hasattr(value, '__len__'):
                        f.write(f"  Length: {len(value)}\n")
                        if len(value) > 0:
                            f.write(f"  First few values: {value[:5] if hasattr(value, '__getitem__') else str(value)[:200]}...\n")
                    else:
                        f.write(f"  Value: {value}\n")
                    f.write("\n")
        
        print(f"📝 Detailed results saved to: {result_file}")
        
    except Exception as e:
        print(f"❌ Error testing allin1 original: {e}")
        print(f"Traceback: {traceback.format_exc()}")

if __name__ == "__main__":
    test_allin1_original()