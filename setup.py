#!/usr/bin/env python3
"""
AIDA Lab Participant Setup Script

This script sets up a clean environment for participants in the
Applied AI in Data Analytics program.

Usage:
    python setup.py
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(cmd, description):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def main():
    """Main setup function."""
    print("🎉 Welcome to AIDA Lab Setup!")
    print("=" * 50)
    
    # Check if uv is installed
    if not run_command("uv --version", "Checking uv installation"):
        print("\n❌ uv is not installed. Please install uv first:")
        print("   curl -LsSf https://astral.sh/uv/install.sh | sh")
        print("   or visit: https://docs.astral.sh/uv/getting-started/installation/")
        return False
    
    # Install dependencies
    if not run_command("uv sync", "Installing dependencies"):
        return False
    
    # Install Jupyter kernel
    if not run_command("python -m ipykernel install --name python3 --user", "Installing Jupyter kernel"):
        return False
    
    print("\n🎉 Setup complete!")
    print("=" * 50)
    print("You can now:")
    print("  • Run 'uv run --with jupyter jupyter lab' to start Jupyter")
    print("  • Run 'uv run poe setup' to re-run setup")
    print("  • Run 'uv run poe check' to verify everything works")
    print("\nHappy learning! 🚀")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
