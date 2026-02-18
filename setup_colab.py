#!/usr/bin/env python3
"""
AIDA Lab Colab Setup Script

This script sets up the environment for participants using Google Colab.
It provides a fallback when uv is not available.

Usage in Colab:
    !wget -O setup_colab.py https://gist.githubusercontent.com/[GIST_ID]/raw/setup_colab.py
    !python setup_colab.py
"""

import subprocess
import sys
import os

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

def install_packages_with_pip():
    """Install packages using pip (Colab fallback)."""
    print("📦 Installing packages with pip (Colab fallback)...")
    
    # Try to use requirements.txt if available
    if os.path.exists("requirements.txt"):
        if run_command("pip install -r requirements.txt", "Installing from requirements.txt"):
            return True
        else:
            print("⚠️  requirements.txt failed, trying individual packages...")
    
    # Fallback to individual packages
    packages = [
        "pandas>=2.0.0", "numpy>=1.24.0", "matplotlib>=3.7.0", "seaborn>=0.12.0",
        "scipy>=1.16.1", "jupytext>=1.16.0", "nbconvert>=7.0.0", "ipykernel>=6.25.0",
        "jupyterlab>=4.0.0", "ipywidgets>=8.1.0", "jupyterlab-widgets>=3.0.0",
        "widgetsnbextension>=4.0.0", "ydata-profiling>=4.6.0", "autoviz>=0.1.69",
        "scikit-learn>=1.3.0", "openai>=1.0.0", "rapidfuzz>=3.14.1", "skrub>=0.6.1", "tqdm>=4.67.1"
    ]
    
    for package in packages:
        if not run_command(f"pip install {package}", f"Installing {package}"):
            print(f"⚠️  Warning: Failed to install {package}")
    
    return True

def main():
    """Main setup function."""
    print("🎉 Welcome to AIDA Lab Colab Setup!")
    print("=" * 50)
    
    # Check if we're in Colab
    try:
        import google.colab
        print("✅ Detected Google Colab environment")
        is_colab = True
    except ImportError:
        print("ℹ️  Not in Colab - checking for uv...")
        is_colab = False
    
    # Try uv first (for local environments)
    if not is_colab:
        if run_command("uv --version", "Checking uv installation"):
            if run_command("uv sync", "Installing dependencies with uv"):
                print("\n🎉 Setup complete with uv!")
                return True
            else:
                print("\n⚠️  uv sync failed, falling back to pip...")
        else:
            print("\n⚠️  uv not found, falling back to pip...")
    
    # Fallback to pip (works in Colab and local)
    if install_packages_with_pip():
        print("\n🎉 Setup complete with pip!")
        print("=" * 50)
        print("You can now:")
        print("  • Import and use all AIDA Lab packages")
        print("  • Run the course notebooks")
        print("\nHappy learning! 🚀")
        return True
    
    return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
