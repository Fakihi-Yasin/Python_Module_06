"""
The Philosopher – an alchemist in search of the Philosopher's Stone.

PROBLEM (circular dependency)
-------------------------------
The original naive version would write:
    from alchemy.circle_of_life.stone import PhilosophersStone  # ← circle!

Because stone.py in turn imports Philosopher from this very file, Python
would see a partially-initialised module and raise an ImportError.

SOLUTION APPLIED HERE: lazy / late import
-------------------------------------------
The import of PhilosophersStone is deferred to inside the method that
actually needs it (seek_stone).  By the time that method is called,
both modules are fully loaded, so the import succeeds.
"""

from alchemy.circle_of_life.shared import WISDOM_THRESHOLD


class Philosopher:
    """An alchemist who seeks the Philosopher's Stone."""

    def __init__(self, name: str, wisdom: int = 0):
        self.name = name
        self.wisdom = wisdom

    def study(self, amount: int = 10) -> None:
        self.wisdom += amount
        print(f"  {self.name} studies... (wisdom: {self.wisdom})")

    def seek_stone(self) -> str:
        # Late import – avoids the circular dependency at module load time.
        from alchemy.circle_of_life.stone import PhilosophersStone  # noqa: PLC0415

        if self.wisdom >= WISDOM_THRESHOLD:
            stone = PhilosophersStone(creator=self.name)
            return f"  ✨ {self.name} created {stone}!"
        gap = WISDOM_THRESHOLD - self.wisdom
        return f"  {self.name} needs {gap} more wisdom to create the Stone."

    def __repr__(self) -> str:
        return f"Philosopher(name={self.name!r}, wisdom={self.wisdom})"
