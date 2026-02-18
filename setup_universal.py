#!/usr/bin/env python3
"""
AIDA Lab Universal Setup Script

This script automatically detects the best available package manager
and sets up the environment accordingly.

Supported package managers (in order of preference):
1. uv (fastest, modern)
2. poetry (comprehensive, widely supported)
3. pip (universal fallback, works everywhere)

Usage:
    python setup_universal.py
"""

import subprocess
import sys
import os
import shutil

def run_command(cmd, description, check=True):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=check, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} completed")
            return True
        else:
            print(f"❌ {description} failed")
            if result.stderr:
                print(f"Error: {result.stderr}")
            return False
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        if e.stderr:
            print(f"Error: {e.stderr}")
        return False

def check_command_exists(command):
    """Check if a command exists in PATH."""
    return shutil.which(command) is not None

def setup_with_uv():
    """Setup using uv (preferred method)."""
    print("🚀 Using uv (fastest option)...")
    
    if not run_command("uv --version", "Checking uv installation"):
        return False
    
    if run_command("uv sync", "Installing dependencies with uv"):
        print("✅ uv setup completed successfully!")
        return True
    
    return False

def setup_with_poetry():
    """Setup using poetry."""
    print("📚 Using poetry...")
    
    if not run_command("poetry --version", "Checking poetry installation"):
        return False
    
    if run_command("poetry install", "Installing dependencies with poetry"):
        print("✅ poetry setup completed successfully!")
        return True
    
    return False

def setup_with_pip():
    """Setup using pip (universal fallback)."""
    print("📦 Using pip (universal fallback)...")
    
    # Try requirements.txt first
    if os.path.exists("requirements.txt"):
        if run_command("pip install -r requirements.txt", "Installing from requirements.txt"):
            print("✅ pip setup completed successfully!")
            return True
        else:
            print("⚠️  requirements.txt failed, trying pyproject.toml...")
    
    # Try pyproject.toml with pip
    if os.path.exists("pyproject.toml"):
        if run_command("pip install -e .", "Installing from pyproject.toml"):
            print("✅ pip setup completed successfully!")
            return True
    
    # Fallback to individual packages
    print("⚠️  Falling back to individual package installation...")
    packages = [
        "pandas>=2.0.0", "numpy>=1.24.0", "matplotlib>=3.7.0", "seaborn>=0.12.0",
        "scipy>=1.16.1", "jupytext>=1.16.0", "nbconvert>=7.0.0", "ipykernel>=6.25.0",
        "jupyterlab>=4.0.0", "ipywidgets>=8.1.0", "jupyterlab-widgets>=3.0.0",
        "widgetsnbextension>=4.0.0", "ydata-profiling>=4.6.0", "autoviz>=0.1.69",
        "scikit-learn>=1.3.0", "openai>=1.0.0", "rapidfuzz>=3.14.1", "skrub>=0.6.1", "tqdm>=4.67.1"
    ]
    
    success_count = 0
    for package in packages:
        if run_command(f"pip install {package}", f"Installing {package}", check=False):
            success_count += 1
    
    if success_count > len(packages) * 0.8:  # 80% success rate
        print("✅ pip setup completed successfully!")
        return True
    
    return False

def main():
    """Main setup function."""
    print("🎉 Welcome to AIDA Lab Universal Setup!")
    print("=" * 50)
    
    # Check if we're in Colab
    try:
        import google.colab
        print("✅ Detected Google Colab environment")
        is_colab = True
    except ImportError:
        print("ℹ️  Local environment detected")
        is_colab = False
    
    # Try package managers in order of preference
    if not is_colab and check_command_exists("uv"):
        if setup_with_uv():
            return True
        print("⚠️  uv failed, trying poetry...")
    
    if check_command_exists("poetry"):
        if setup_with_poetry():
            return True
        print("⚠️  poetry failed, trying pip...")
    
    # Always try pip as fallback
    if setup_with_pip():
        return True
    
    print("\n❌ All setup methods failed!")
    print("Please check your Python environment and try again.")
    return False

if __name__ == "__main__":
    success = main()
    if success:
        print("\n🎉 Setup complete!")
        print("=" * 50)
        print("You can now:")
        print("  • Import and use all AIDA Lab packages")
        print("  • Run the course notebooks")
        print("\nHappy learning! 🚀")
    
    sys.exit(0 if success else 1)
