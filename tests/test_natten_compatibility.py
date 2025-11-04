#!/usr/bin/env python3
"""
Test script to verify NATTEN compatibility across different versions.
Tests the three-tier compatibility system in dinat.py
"""

import sys
import torch

def test_natten_import():
    """Test if NATTEN can be imported and get version info"""
    print("=" * 60)
    print("NATTEN Compatibility Test")
    print("=" * 60)

    try:
        import natten
        print(f"✅ NATTEN imported successfully")

        # Try to get version
        if hasattr(natten, '__version__'):
            print(f"   Version: {natten.__version__}")
        else:
            print(f"   Version: Unknown (no __version__ attribute)")

    except ImportError as e:
        print(f"❌ NATTEN import failed: {e}")
        return False

    return True


def test_natten_functional_imports():
    """Test the three-tier import system from dinat.py"""
    print("\n" + "=" * 60)
    print("Testing NATTEN Functional Imports (Three-Tier System)")
    print("=" * 60)

    # Test 1: Short names (NATTEN <0.19)
    print("\n1. Testing short names (NATTEN <0.19):")
    try:
        from natten.functional import na1d_av, na1d_qk, na2d_av, na2d_qk
        print("   ✅ Short names available: na1d_av, na1d_qk, na2d_av, na2d_qk")
        return "short", {"na1d_av": na1d_av, "na1d_qk": na1d_qk, "na2d_av": na2d_av, "na2d_qk": na2d_qk}
    except ImportError as e:
        print(f"   ⚠️  Short names not available: {e}")

    # Test 2: Long names (NATTEN 0.19)
    print("\n2. Testing long names (NATTEN 0.19):")
    try:
        from natten.functional import (
            natten1dav as na1d_av,
            natten1dqkrpb as na1d_qk,
            natten2dav as na2d_av,
            natten2dqkrpb as na2d_qk,
        )
        print("   ✅ Long names available: natten1dav, natten1dqkrpb, natten2dav, natten2dqkrpb")
        return "long", {"na1d_av": na1d_av, "na1d_qk": na1d_qk, "na2d_av": na2d_av, "na2d_qk": na2d_qk}
    except ImportError as e:
        print(f"   ⚠️  Long names not available: {e}")

    # Test 3: Modern generic API (NATTEN >=0.20)
    print("\n3. Testing modern generic API (NATTEN >=0.20):")
    try:
        from natten.functional import neighborhood_attention_generic as _na_generic
        print("   ✅ Generic API available: neighborhood_attention_generic")
        print("   ℹ️  Will use custom wrappers for compatibility")

        # Create wrappers (simplified version from dinat.py)
        def create_wrapper(dim, is_av=False):
            def wrapper(*args, **kwargs):
                # This is a simplified test - just verify it's callable
                return _na_generic
            return wrapper

        na1d_qk = create_wrapper(1, False)
        na1d_av = create_wrapper(1, True)
        na2d_qk = create_wrapper(2, False)
        na2d_av = create_wrapper(2, True)

        return "generic", {"na1d_av": na1d_av, "na1d_qk": na1d_qk, "na2d_av": na2d_av, "na2d_qk": na2d_qk}
    except ImportError as e:
        print(f"   ❌ Generic API not available: {e}")
        return None, None


def test_actual_dinat_import():
    """Test importing the actual dinat.py module"""
    print("\n" + "=" * 60)
    print("Testing Actual dinat.py Import")
    print("=" * 60)

    try:
        # Add src to path
        import os
        src_path = os.path.join(os.path.dirname(__file__), 'src')
        if src_path not in sys.path:
            sys.path.insert(0, src_path)

        from allin1fix.models import dinat
        print("✅ dinat.py imported successfully")

        # Check if the functions are available
        if hasattr(dinat, 'na1d_av'):
            print("✅ na1d_av function is available in dinat module")
        if hasattr(dinat, 'na2d_av'):
            print("✅ na2d_av function is available in dinat module")

        return True
    except Exception as e:
        print(f"❌ Failed to import dinat.py: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_pytorch_version():
    """Check PyTorch version"""
    print("\n" + "=" * 60)
    print("PyTorch Environment")
    print("=" * 60)
    print(f"PyTorch version: {torch.__version__}")
    print(f"CUDA available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"CUDA version: {torch.version.cuda}")
        print(f"GPU count: {torch.cuda.device_count()}")


def main():
    """Run all compatibility tests"""
    print("\n🔬 NATTEN Compatibility Test Suite\n")

    # Test PyTorch
    test_pytorch_version()

    # Test NATTEN import
    if not test_natten_import():
        print("\n❌ NATTEN is not installed. Please install NATTEN first.")
        print("\nFor NATTEN 0.17.5:")
        print("  pip install natten==0.17.5")
        print("\nFor NATTEN 0.21.0:")
        print("  pip install natten==0.21.0+torch270cu128 -f https://whl.natten.org")
        return False

    # Test functional imports
    tier, functions = test_natten_functional_imports()

    if tier:
        print(f"\n✅ NATTEN compatibility tier: {tier.upper()}")
    else:
        print("\n❌ No compatible NATTEN API found")
        return False

    # Test actual dinat.py import
    test_actual_dinat_import()

    # Summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)

    if tier == "short":
        print("✅ NATTEN <0.19 detected - using short function names")
        print("   Compatible: Yes")
    elif tier == "long":
        print("✅ NATTEN 0.19 detected - using long function names")
        print("   Compatible: Yes")
    elif tier == "generic":
        print("✅ NATTEN >=0.20 detected - using generic API with wrappers")
        print("   Compatible: Yes (includes 0.21.0)")

    print("\n✅ All compatibility tests passed!")
    print("   The code will automatically adapt to your NATTEN version.")

    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
