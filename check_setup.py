"""Check that this computer is ready for the workshop exercise.

Run it from the repository folder, with your environment activated:

    python check_setup.py

It only reads your installation; it does not install or change anything.
"""

import importlib
import os
import shutil
import sys

MIN_PYTHON = (3, 9)
REPO_DIR = os.path.dirname(os.path.abspath(__file__))


def check(label, passed, detail="", hint=""):
    print(f"[{'OK' if passed else 'FAIL'}] {label}{': ' + detail if detail else ''}")
    if not passed and hint:
        print(f"       -> {hint}")
    return passed


def main():
    results = []
    version = ".".join(str(part) for part in sys.version_info[:3])
    results.append(
        check(
            "Python version",
            sys.version_info[:2] >= MIN_PYTHON,
            f"{version} ({sys.executable})",
            "Install Python 3.9 or newer; see SETUP.md.",
        )
    )

    for name in ("numpy", "pytest"):
        try:
            module = importlib.import_module(name)
        except ImportError:
            results.append(
                check(
                    f"{name} installed",
                    False,
                    hint="Activate your environment, then run: python -m pip install -r requirements.txt",
                )
            )
        else:
            results.append(check(f"{name} installed", True, module.__version__))

    results.append(
        check(
            "Running from the repository folder",
            os.path.abspath(os.getcwd()) == REPO_DIR,
            os.getcwd(),
            f"Change into the repository folder first: cd {REPO_DIR}",
        )
    )

    try:
        from psf_model import gaussian_psf

        image = gaussian_psf((5, 5), 1.0)
        model_ok = image.shape == (5, 5)
    except Exception as error:  # report any import or runtime problem
        results.append(check("PSF model imports and runs", False, repr(error)))
    else:
        results.append(check("PSF model imports and runs", model_ok))

    in_venv = sys.prefix != sys.base_prefix or "CONDA_PREFIX" in os.environ
    print(f"[INFO] Virtual or conda environment active: {'yes' if in_venv else 'no (recommended, see SETUP.md)'}")
    print(f"[INFO] Git available: {'yes' if shutil.which('git') else 'no (fine if you use the ZIP download)'}")

    if all(results):
        print("\nReady. Next, run the tests with:  python -m pytest")
        return 0
    print("\nNot ready yet. Fix the FAIL lines above (see SETUP.md), then run this check again.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
