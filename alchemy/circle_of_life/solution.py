"""
Circular Dependency Solution – worked demonstration.

This module shows all three strategies side-by-side:

  Strategy 1 – Lazy import   : import inside a function (see philosopher.py)
  Strategy 2 – Shared module : extract common code to shared.py
  Strategy 3 – String annotation : avoid runtime import for type hints (see stone.py)
"""

from alchemy.circle_of_life.philosopher import Philosopher
from alchemy.circle_of_life.stone import PhilosophersStone


def demonstrate_circular_solution() -> None:
    print("\n--- Circular Dependency: Breaking the Circle ---")

    print("\nStrategy 1 – Lazy / late import (import inside a function):")
    print("  philosopher.py imports stone.py INSIDE seek_stone(), not at the top.")
    merlin = Philosopher(name="Merlin", wisdom=50)
    print(merlin.seek_stone())  # not enough wisdom yet
    merlin.study(60)
    print(merlin.seek_stone())  # now has enough wisdom

    print("\nStrategy 2 – Extract shared code to shared.py:")
    print("  Both modules import from shared.py instead of from each other.")
    from alchemy.circle_of_life.shared import WISDOM_THRESHOLD, TRANSMUTATION_FORMULA
    print(f"  WISDOM_THRESHOLD    = {WISDOM_THRESHOLD}")
    print(f"  TRANSMUTATION_FORMULA = {TRANSMUTATION_FORMULA!r}")

    print("\nStrategy 3 – String annotation (forward reference):")
    print("  stone.py references 'Philosopher' only as a string type hint,")
    print("  so Python never resolves that name at import time.")
    stone = PhilosophersStone(creator="Merlin")
    print(f"  {stone.transmute()}")
    print(f"  {stone.grant_immortality()}")

    print("\nAll circular dependency strategies demonstrated successfully.\n")
