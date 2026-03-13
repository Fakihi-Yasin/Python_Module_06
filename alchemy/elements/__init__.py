"""
MYSTERY 2: IMPORT PATHWAYS
============================
When Python executes `import something` it searches a list of locations called
the *module search path* (sys.path).  The search order is:

  1. The directory containing the script that was run (or '' for interactive).
  2. Directories listed in the PYTHONPATH environment variable.
  3. Installation-dependent default directories (standard library, site-packages).

This subpackage __init__.py demonstrates the pathway concept by:
  • collecting all element modules into a single namespace, and
  • exposing a summary dictionary so callers can inspect "what lives here".

Run `python -c "import sys; print(sys.path)"` to see your own search path.
"""

import sys

# Re-export individual element modules so callers can write:
#   from alchemy.elements import fire
# or simply:
#   from alchemy.elements import ELEMENTS
from alchemy.elements import fire, water, earth, air  # noqa: E402 (absolute)

# A summary of all elements available in this subpackage
ELEMENTS = {
    fire.NAME: {"symbol": fire.SYMBOL, "property": fire.PROPERTY},
    water.NAME: {"symbol": water.SYMBOL, "property": water.PROPERTY},
    earth.NAME: {"symbol": earth.SYMBOL, "property": earth.PROPERTY},
    air.NAME: {"symbol": air.SYMBOL, "property": air.PROPERTY},
}

__all__ = ["fire", "water", "earth", "air", "ELEMENTS", "show_search_path"]


def show_search_path() -> None:
    """Print the current module search path (sys.path) for educational purposes."""
    print("\n[Import Pathway] Python searches these locations in order:")
    for idx, path in enumerate(sys.path, start=1):
        label = path if path else "(current working directory)"
        print(f"  {idx:>2}. {label}")
    print()
