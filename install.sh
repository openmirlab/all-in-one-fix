#!/bin/bash
# Automated installation script for allin1fix
# This handles all build dependencies automatically

set -e

echo "🚀 Installing allin1fix with automatic dependency handling..."

if command -v uv &> /dev/null; then
    echo "📦 Using uv..."
    uv add setuptools hatchling editables torch numpy && \
    uv add allin1fix --no-build-isolation
    echo "✅ Installation complete!"
elif command -v pip &> /dev/null; then
    echo "📦 Using pip..."
    pip install setuptools hatchling editables torch numpy && \
    pip install allin1fix --no-build-isolation
    echo "✅ Installation complete!"
else
    echo "❌ Error: Neither uv nor pip found"
    exit 1
fi
