"""
Relative Import Demonstration
================================
Relative imports use leading dots to express the position of the target
module relative to the *current* package.

  .          → same package          (alchemy.transmutations)
  ..         → parent package        (alchemy)
  ..elements → sibling subpackage    (alchemy.elements)

Usage:
    from ..elements import fire          # one level up, then into elements
    from ..elements.fire import describe
"""

# One dot  = alchemy.transmutations (this package) – nothing to import here
# Two dots = alchemy (parent), then drill into elements  ← relative imports
from ..elements import fire, water, earth, air
from ..elements.fire import describe as fire_describe


def demonstrate_relative() -> None:
    print("\n--- Relative Imports ---")
    print("Importing via relative path: 'from ..elements import fire'")
    print(fire_describe())
    print(f"  water  : {water.describe()}")
    print(f"  earth  : {earth.describe()}")
    print(f"  air    : {air.describe()}")
    print("Relative imports resolved successfully.\n")
