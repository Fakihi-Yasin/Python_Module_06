"""
Absolute Import Demonstration
================================
Absolute imports use the full dotted path from the project root.
They are explicit and unambiguous – Python always knows exactly
which module is being requested.

    from alchemy.elements import fire
    from alchemy.elements.fire import describe
"""

# Full path from the top-level package  ← absolute import
from alchemy.elements import fire, water, earth, air
from alchemy.elements.fire import describe as fire_describe


def demonstrate_absolute() -> None:
    print("\n--- Absolute Imports ---")
    print("Importing via full path: 'from alchemy.elements import fire'")
    print(fire_describe())
    print(f"  water  : {water.describe()}")
    print(f"  earth  : {earth.describe()}")
    print(f"  air    : {air.describe()}")
    print("Absolute imports resolved successfully.\n")
