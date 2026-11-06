"""Minimal clipboard helper using pyperclip when available."""
try:
    import pyperclip
    AVAILABLE = True
except Exception:  # pragma: no cover
    pyperclip = None
    AVAILABLE = False

import sys


def copy(text: str) -> bool:
    if not AVAILABLE:
        print("pyperclip not installed: pip install pyperclip")
        return False
    pyperclip.copy(text)
    return True


def paste() -> str:
    if not AVAILABLE:
        print("pyperclip not installed: pip install pyperclip")
        return ""
    return pyperclip.paste()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: clipboard.py [copy <text> | paste]")
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "copy":
        text = " ".join(sys.argv[2:])
        copy(text)
        print("copied")
    elif cmd == "paste":
        print(paste())
