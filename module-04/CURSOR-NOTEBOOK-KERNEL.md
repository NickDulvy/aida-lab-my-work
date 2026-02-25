# Python kernel for module-04 notebooks

> **First run:** See **NOTEBOOK-SETUP.md** in the project root for one-time setup.

## Quick start

1. **Open Cursor** with the folder **aida-lab-env** (File → Open Folder → select `aida-lab-env`).
2. Open any module-04 notebook (e.g. `4_1_detecting_anomalies_with_ai.ipynb`).
3. Click **Select Kernel** (top-right) → **Python Environments** → choose **Python 3.x ('.venv': venv)**  
   or **Jupyter Kernels** → **Python (aida-lab-env)**.

## Verify

Run in a cell:
```python
import sys
print(sys.executable)
```
You should see a path ending in `aida-lab-env/.venv/bin/python` (or similar).

## Alternative: Jupyter Lab

```bash
cd aida-lab-env
uv run jupyter lab
```
Then open the notebook in the browser.
