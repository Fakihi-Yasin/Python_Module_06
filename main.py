"""
main.py – The Alchemist's Grand Experiment
============================================
Runs all four sacred mysteries of Python imports:

  Mystery 1 – Package Initialization     (alchemy/__init__.py)
  Mystery 2 – Import Pathways            (alchemy/elements/__init__.py + pathways/)
  Mystery 3 – Absolute vs Relative       (alchemy/transmutations/)
  Mystery 4 – Circular Dependencies      (alchemy/circle_of_life/)
"""


def separator(title: str) -> None:
    width = 60
    print("\n" + "=" * width)
    print(f"  {title}")
    print("=" * width)


# ── Mystery 1: Package Initialization ──────────────────────────────────────
separator("MYSTERY 1: Package Initialization")
print(
    "\nSimply importing `alchemy` triggers alchemy/__init__.py.\n"
    "Watch for the '[alchemy] The ancient laboratory stirs to life...' message above.\n"
    "That line ran automatically when `import alchemy` was first executed.\n"
)

import alchemy  # noqa: E402  ← this import already ran at the top via the separator call

print(f"  alchemy.__version__ = {alchemy.__version__!r}")
print(f"  alchemy.__author__  = {alchemy.__author__!r}")
print(f"  alchemy.__all__     = {alchemy.__all__}")

cauldron = alchemy.Cauldron()
cauldron.add("fire")
cauldron.add("water")
cauldron.add("earth")
cauldron.add("air")
print("\n" + cauldron.describe())
print("\n" + cauldron.brew())

# ── Mystery 2: Import Pathways ──────────────────────────────────────────────
separator("MYSTERY 2: Import Pathways")
print(
    "\nsys.path is the ordered list of directories Python searches when you\n"
    "write `import something`. The first match wins.\n"
)

from alchemy.elements import show_search_path, ELEMENTS  # noqa: E402
show_search_path()

print("[Import Pathways] Elements discovered in alchemy.elements:")
for name, info in ELEMENTS.items():
    print(f"  {info['symbol']}  {name:6s} – {info['property']}")

from alchemy.pathways import PathwaySeeker, show_module_origin  # noqa: E402
import alchemy.elements.fire as fire_mod  # noqa: E402

seeker = PathwaySeeker()
seeker.describe_sys_path()
seeker.list_loaded_modules("alchemy")
show_module_origin(fire_mod)

# ── Mystery 3: Absolute vs Relative Imports ─────────────────────────────────
separator("MYSTERY 3: Absolute vs Relative Imports")
print(
    "\nAbsolute imports spell out the full dotted path from the project root.\n"
    "Relative imports use leading dots to express position within a package.\n"
)

from alchemy.transmutations import demonstrate_absolute, demonstrate_relative  # noqa: E402
demonstrate_absolute()
demonstrate_relative()

# ── Mystery 4: Circular Dependencies ───────────────────────────────────────
separator("MYSTERY 4: Breaking Circular Dependencies")
print(
    "\nCircular imports occur when module A imports B and B imports A.\n"
    "Three strategies break the circle:\n"
    "  1. Lazy/late import  – import inside the function that needs it.\n"
    "  2. Shared module     – move shared symbols to a third file.\n"
    "  3. String annotation – use forward-reference strings for type hints.\n"
)

from alchemy.circle_of_life import demonstrate_circular_solution  # noqa: E402
demonstrate_circular_solution()

separator("The Grand Experiment Complete")
print("\nAll four mysteries of Python imports have been revealed. 🧪✨\n")
