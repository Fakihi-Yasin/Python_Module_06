"""
MYSTERY 3: ABSOLUTE VS RELATIVE IMPORTS
=========================================
Python supports two styles of import for intra-package references:

ABSOLUTE IMPORTS  (recommended default – PEP 328 / PEP 8)
  Full dotted path from the top-level package:
      from alchemy.elements import fire
  ✔ Unambiguous – works from anywhere.
  ✔ Easier to refactor with IDEs.
  ✔ Required when running a module as a script (__name__ == '__main__').

RELATIVE IMPORTS  (useful inside tightly-coupled subpackages)
  Dot-notation relative to the current package:
      from . import fire           # same package
      from ..elements import fire  # parent's sibling
  ✔ Package-portable – renaming the top-level package doesn't break them.
  ✔ Makes intra-package relationships explicit.
  ✗ Cannot be used when running a file directly as a script.

See absolute_path.py and relative_path.py for live demonstrations.
"""

from alchemy.transmutations.absolute_path import demonstrate_absolute
from alchemy.transmutations.relative_path import demonstrate_relative

__all__ = ["demonstrate_absolute", "demonstrate_relative"]
