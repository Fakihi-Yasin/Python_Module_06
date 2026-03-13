"""
MYSTERY 4: BREAKING CIRCULAR DEPENDENCIES
===========================================
A circular import occurs when module A imports module B, and module B
(directly or indirectly) imports module A.

  philosopher.py  →  imports stone.py
  stone.py        →  imports philosopher.py   ← circle!

Python's import system partially handles circles by caching partially-
initialised modules in sys.modules, but accessing an attribute that has
not been defined yet raises an ImportError or AttributeError.

SOLUTIONS demonstrated in this subpackage
------------------------------------------
1. Late / lazy imports  – move the import inside a function so it only
   runs after both modules are fully initialised.

2. Extract shared code  – move the shared symbol into a third module
   (shared.py) that neither problematic module imports.

3. Restructure with __init__.py  – let the package __init__.py own the
   import order so neither leaf module needs to import the other.

See philosopher.py, stone.py, and solution.py for full worked examples.
"""

from alchemy.circle_of_life.solution import demonstrate_circular_solution

__all__ = ["demonstrate_circular_solution"]
