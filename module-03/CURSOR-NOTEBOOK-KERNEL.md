# How to Run the Notebook in Cursor (Option 2)

## Prerequisites
- Open Cursor with the folder **aida-lab-env** (File → Open Folder → select `aida-lab-env`)
- Or, if you opened `module-03` only, the settings will still find the parent `.venv`

---

## Step-by-Step: Select the Correct Kernel

### 1. Open the notebook
Open `heritage-sites-analysis.ipynb` in Cursor.

### 2. Find the kernel selector
- Look at the **top-right corner** of the notebook (above the first cell).
- You should see text like **"Select Kernel"** or **"Python 3.x.x"** or a kernel name.
- **Click it.**

### 3. Open "Select Another Kernel"
- If you see a short list, click **"Select Another Kernel…"** at the bottom.
- If you see "Select Kernel" only, click it once to open the picker.

### 4. Choose from Python Environments (preferred)
1. Under the list, look for **"Python Environments"**.
2. Click **"Python Environments"**.
3. Find the entry that points to the project `.venv`, e.g.:
   - `Python 3.x ('.venv': venv)`
   - Or a path containing `aida-lab-env/.venv` or `module-03/../.venv`
4. **Click that environment.**

### 5. Or choose from Jupyter Kernels
1. Click **"Jupyter Kernels"** instead.
2. Select **"Python (aida-lab)"**.
3. **Click it.**

### 6. If the kernel picker is empty
1. Press **Cmd+Shift+P** (macOS) or **Ctrl+Shift+P** (Windows/Linux).
2. Type: **`Notebook: Select Notebook Kernel`**
3. Press Enter.
4. Follow steps 4–5 above.

### 7. Or use the interpreter picker
1. Press **Cmd+Shift+P**.
2. Type: **`Python: Select Interpreter`**
3. Choose the interpreter with `.venv` in the path.
4. Reload the window: **Cmd+Shift+P** → **`Developer: Reload Window`**
5. Reopen the notebook and try running a cell again.

---

## Verifying the kernel

Run this in the first code cell:
```python
import sys
print(sys.executable)
```
You should see a path ending in `aida-lab-env/.venv/bin/python` (or similar).

---

## If it still fails

Cursor has known issues with kernel selection. Use Jupyter Lab instead:
```bash
cd aida-lab-env
uv run jupyter lab
```
Then open the notebook in the browser.
