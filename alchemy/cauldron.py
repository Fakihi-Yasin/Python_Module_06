"""
The Cauldron – the heart of the alchemical laboratory.
It combines all four elements and demonstrates how a top-level module
can draw from subpackages using absolute imports.
"""

from alchemy.elements import fire, water, earth, air  # absolute imports


class Cauldron:
    """A vessel that combines the classical elements."""

    def __init__(self):
        self.contents = []

    def add(self, element: str) -> None:
        self.contents.append(element)

    def brew(self) -> str:
        if not self.contents:
            return "The cauldron is empty."
        mixture = " + ".join(self.contents)
        return f"Brewing: {mixture} → Philosopher's Stone!"

    def describe(self) -> str:
        lines = [
            "=== Cauldron Contents ===",
            f"  Fire  : {fire.SYMBOL}  ({fire.PROPERTY})",
            f"  Water : {water.SYMBOL}  ({water.PROPERTY})",
            f"  Earth : {earth.SYMBOL}  ({earth.PROPERTY})",
            f"  Air   : {air.SYMBOL}  ({air.PROPERTY})",
        ]
        return "\n".join(lines)
