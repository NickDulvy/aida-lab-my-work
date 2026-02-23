#!/bin/bash
cd "$(dirname "$0")"
echo "Starting Jupyter Lab..."
echo "Your browser will open. Go to module-03 → heritage-sites-analysis.ipynb"
echo ""
uv run jupyter lab
