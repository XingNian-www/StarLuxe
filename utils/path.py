"""Utils for everything related path to a resource"""
import os, sys
from pathlib import Path

def resource_path(relative_path: str) -> Path:
    """Return the absolute path to a resource, working both in development mode and when packaged."""
    if "__compiled__" in globals() or getattr(sys, "frozen", False):
        base_path = Path(sys.executable).parent
    else:
        base_path = Path(__file__).parent.parent.resolve()

    return base_path / relative_path


def relative_path(relative_path: str) -> Path:
    """Return relative path to the resource file"""
    if "__compiled__" in globals() or getattr(sys, "frozen", False):
        base = Path(sys.executable).parent
    else:
        base = Path(__file__).parent.parent.resolve()

    return Path(base) / relative_path
