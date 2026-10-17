# Setup

You need **Python 3.9 or newer**. The only packages are `numpy` and `pytest`.
Setup takes about five minutes; please do it before the exercise starts.

## 1. Get the code

**With Git:**

```bash
git clone https://github.com/miccles/ciera-ai-assisted-coding-for-research.git psf-demo
cd psf-demo
```

**Without Git:** download the ZIP, then *extract* it. On Windows, right-click the
ZIP and choose **Extract All…**; do not open the files from inside the ZIP
window. Then open a terminal in the extracted folder that contains `README.md`.
It is usually called `psf-demo`, but your browser may give it another name
(such as `psf-demo (1)`) or put it inside a second folder; use whichever folder
holds `README.md`.

All commands below must be run **from the folder that contains `README.md`**.
These instructions call it the `psf-demo` folder.

## 2. Create and activate an environment

### macOS and Linux (Terminal)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows (PowerShell)

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell says that running scripts is disabled, allow it for this window
only and try again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.venv\Scripts\Activate.ps1
```

### Windows (Command Prompt)

```bat
py -m venv .venv
.venv\Scripts\activate.bat
```

When the environment is active, your prompt starts with `(.venv)`. From now on
the command is `python` on every system.

### Using conda instead

```bash
conda create -n psf-demo python=3.12 numpy pytest
conda activate psf-demo
```

Skip step 3 if you use conda.

## 3. Install the packages

```bash
python -m pip install -r requirements.txt
```

## 4. Check your setup

```bash
python check_setup.py
```

Every line should say `OK` and the last line should say `Ready`.

## 5. Run the tests

```bash
python -m pytest
```

All tests should pass. Use `python -m pytest`, not `pytest`: it always uses
the Python of your active environment.

## 6. Open the folder in VS Code

Use **File ▸ Open Folder…** and choose the `psf-demo` folder itself (the one
that contains `README.md`), not a parent folder. If VS Code asks for a Python
interpreter, choose the one inside `.venv` (or your `psf-demo` conda
environment).

## Troubleshooting

| Problem | Fix |
| --- | --- |
| `python3: command not found` (macOS) | Install Python 3 from python.org and open a new Terminal, or, if you already have Anaconda or Miniconda, use the conda instructions above. |
| `py` is not recognized (Windows) | Install Python from python.org and tick **Add python.exe to PATH**, or use `python` instead of `py`. |
| `No module named numpy` or `No module named pytest` | Your environment is not active. Activate it (step 2) and run step 3 again. |
| `check_setup.py` says to change folder | `cd` into the `psf-demo` folder that contains `README.md`. |
| `pip install` fails on a university network | Try again on another network, or use the conda instructions above. |
