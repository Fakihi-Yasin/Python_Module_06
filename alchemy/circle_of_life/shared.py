"""
Shared constants extracted to break the circular dependency.

Both philosopher.py and stone.py originally needed WISDOM_THRESHOLD.
By moving it here, neither needs to import the other.

This is Solution 2: "Extract shared code into a third module".
"""

WISDOM_THRESHOLD = 100
TRANSMUTATION_FORMULA = "lead → gold"
