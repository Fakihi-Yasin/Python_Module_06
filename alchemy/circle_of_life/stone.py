"""
The Philosopher's Stone – the ultimate goal of alchemy.

PROBLEM (circular dependency)
-------------------------------
The Stone needs to know about its creator (a Philosopher), but Philosopher
also needs to know about the Stone.  A naive top-level import of Philosopher
here would complete the circle and crash at load time.

SOLUTION APPLIED HERE: type annotation with a string forward reference
-----------------------------------------------------------------------
Instead of importing Philosopher for type checking, we use a string
annotation ('Philosopher') so Python never needs to resolve the name at
import time.  The actual runtime logic only uses the creator's *name*
(a plain string), so no runtime import of Philosopher is needed at all.
"""

from alchemy.circle_of_life.shared import TRANSMUTATION_FORMULA


class PhilosophersStone:
    """The legendary artifact that grants immortality and transmutes metals."""

    def __init__(self, creator: str):
        self.creator = creator  # just a string – no Philosopher import needed
        self.formula = TRANSMUTATION_FORMULA

    def transmute(self, base_metal: str = "lead") -> str:
        return f"  🔮 {self.creator}'s Stone transmutes {base_metal} → gold!"

    def grant_immortality(self) -> str:
        return f"  🌟 {self.creator} achieves immortality."

    def __repr__(self) -> str:
        return f"PhilosophersStone(creator={self.creator!r}, formula={self.formula!r})"

    def __str__(self) -> str:
        return f"the Philosopher's Stone (formula: {self.formula})"
