#!/usr/bin/env python3
"""
Deploy AIDA setup as a gist for easy cloning.

This script creates a gist with the AIDA setup files
so students can easily clone and use the clean environment.
"""

import os
import json
from pathlib import Path
from github import Github

def create_aida_gist():
    """Create a gist with AIDA setup files."""
    
    # Get GitHub token
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        print("❌ GITHUB_TOKEN environment variable not set")
        return None
    
    # Initialize GitHub client
    g = Github(token)
    
    # Prepare files for gist
    files = {}
    
    # Add pyproject.toml
    pyproject_path = Path("pyproject.toml")
    if pyproject_path.exists():
        files["pyproject.toml"] = {
            "content": pyproject_path.read_text()
        }
    
    # Add setup.py
    setup_path = Path("setup.py")
    if setup_path.exists():
        files["setup.py"] = {
            "content": setup_path.read_text()
        }
    
    # Add README.md
    readme_path = Path("README.md")
    if readme_path.exists():
        files["README.md"] = {
            "content": readme_path.read_text()
        }
    
    # Create gist
    try:
        gist = g.get_user().create_gist(
            public=True,
            files=files,
            description="AIDA Lab - Setup (Clean Environment) - Download all files and put in a folder",
        )
        
        print(f"✅ Gist created: {gist.html_url}")
        print(f"🔗 Clone URL: {gist.git_pull_url}")
        print(f"📁 Gist ID: {gist.id}")
        
        return gist
        
    except Exception as e:
        print(f"❌ Failed to create gist: {e}")
        return None

if __name__ == "__main__":
    create_aida_gist()
