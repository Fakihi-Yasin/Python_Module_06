"""
MYSTERY 1: PACKAGE INITIALIZATION
===================================
The __init__.py file is the "soul" of a package. When Python encounters a directory
with an __init__.py, it treats that directory as a package. This file runs
automatically whenever the package is imported.

Key roles of __init__.py:
  1. Marks a directory as a Python package.
  2. Runs initialization code (e.g., setting up state, logging, config).
  3. Controls what is publicly available via __all__.
  4. Can re-export symbols so callers don't need to know the internal structure.
"""

# This code executes once when `import alchemy` (or any submodule) is first run.
print("[alchemy] The ancient laboratory stirs to life...")

# __all__ controls what `from alchemy import *` exposes.
# Only symbols listed here are exported on a wildcard import.
__all__ = ["Cauldron", "ELEMENTS"]

# Package-level metadata
__version__ = "1.0.0"
__author__ = "The Alchemist"

# Re-export the main entry-point class so users can simply write:
#   from alchemy import Cauldron
# instead of:
#   from alchemy.cauldron import Cauldron
from alchemy.cauldron import Cauldron  # noqa: E402

# A package-level constant assembled from subpackage symbols
from alchemy.elements import ELEMENTS  # noqa: E402
