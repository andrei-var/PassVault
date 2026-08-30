#!/usr/bin/env python3
"""
PassVault - Modern & Secure Password Manager
Entry point launcher.
"""
import os
import sys
import shutil
import subprocess

def ensure_modern_tk():
    """
    On macOS, Apple's default /usr/bin/python3 (Python 3.9) ships with legacy Tcl/Tk 8.5.
    CustomTkinter requires Tk 8.6+ to render its canvas and widgets (otherwise the window is blank).
    This function detects if Tk < 8.6 and automatically re-launches with a modern Python
    interpreter (Homebrew Python 3.11+, 3.12+, etc.) if available.
    """
    try:
        import tkinter
        if tkinter.TkVersion < 8.6:
            candidates = [
                "/opt/homebrew/bin/python3.11",
                "/opt/homebrew/bin/python3.12",
                "/opt/homebrew/bin/python3.10",
                "/opt/homebrew/bin/python3",
                "/usr/local/bin/python3.11",
                "/usr/local/bin/python3.12",
                "/usr/local/bin/python3",
                "python3.11",
                "python3.12",
                "python3.10",
            ]
            for cand in candidates:
                cand_path = cand if (os.path.isabs(cand) and os.path.exists(cand)) else shutil.which(cand)
                if cand_path and os.path.realpath(cand_path) != os.path.realpath(sys.executable):
                    res = subprocess.run(
                        [cand_path, "-c", "import sys, tkinter; sys.exit(0 if tkinter.TkVersion >= 8.6 else 1)"],
                        capture_output=True
                    )
                    if res.returncode == 0:
                        os.execv(cand_path, [cand_path] + sys.argv)
    except Exception:
        pass

ensure_modern_tk()

# Ensure repository root is in sys.path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

try:
    from src.ui.app import App
except ImportError as e:
    print(f"\n[PassVault Error] Failed to start: {e}")
    print("\nPlease ensure dependencies are installed:")
    print("  pip install -r requirements.txt")
    print("\nIf you are on macOS and encountering an empty window, ensure Tk 8.6+ is installed:")
    print("  brew install python@3.11 python-tk@3.11")
    print("  python3.11 run.py\n")
    sys.exit(1)

if __name__ == "__main__":
    app = App()
    app.mainloop()
