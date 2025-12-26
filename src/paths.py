import os
import sys
from pathlib import Path

def get_repo_root() -> str:
    """
    Returns the absolute path to the repository root.
    It walks upwards from this file until it finds a marker file (e.g., .git, requirements.txt, pyproject.toml).
    """
    current_path = Path(__file__).resolve()
    # If the file is in src/, we start looking from there
    # We walk up until we find a marker
    for parent in [current_path] + list(current_path.parents):
        if (parent / ".git").exists() or (parent / "requirements.txt").exists() or (parent / "pyproject.toml").exists():
            return str(parent)

    # Fallback: assume this file is in src/ and repo root is one level up
    return str(Path(__file__).resolve().parent.parent)

def get_outputs_dir() -> str:
    return os.path.join(get_repo_root(), "outputs")

def get_figures_dir() -> str:
    return os.path.join(get_outputs_dir(), "figures")

def get_tables_dir() -> str:
    return os.path.join(get_outputs_dir(), "tables")

def get_cache_dir() -> str:
    return os.path.join(get_outputs_dir(), "cache")

def ensure_output_dirs() -> None:
    """
    Ensures that the output directories exist.
    """
    os.makedirs(get_outputs_dir(), exist_ok=True)
    os.makedirs(get_figures_dir(), exist_ok=True)
    os.makedirs(get_tables_dir(), exist_ok=True)
    os.makedirs(get_cache_dir(), exist_ok=True)

if __name__ == "__main__":
    print(f"Repo root: {get_repo_root()}")
    print(f"Outputs: {get_outputs_dir()}")
    print(f"Figures: {get_figures_dir()}")
    print(f"Tables: {get_tables_dir()}")
    print(f"Cache: {get_cache_dir()}")
    ensure_output_dirs()
    print("Output directories ensured.")
