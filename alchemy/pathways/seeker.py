"""
Pathway Seeker – inspects Python's import machinery at runtime.

Key concepts shown here:
  • sys.path        – the ordered list of directories Python searches
  • sys.modules     – the cache of already-imported modules
  • module.__file__ – the file path where a module was found
  • module.__spec__ – the ModuleSpec describing how the module was loaded
"""

import sys
from types import ModuleType
from typing import Optional


class PathwaySeeker:
    """Explores and explains Python's module search path."""

    def describe_sys_path(self) -> None:
        """Print each entry in sys.path with its index."""
        print("\n[PathwaySeeker] sys.path (module search order):")
        for idx, entry in enumerate(sys.path):
            label = entry or "(current working directory)"
            print(f"  [{idx}] {label}")

    def list_loaded_modules(self, prefix: str = "alchemy") -> None:
        """List modules in sys.modules that match a given prefix."""
        print(f"\n[PathwaySeeker] Loaded modules matching '{prefix}':")
        matches = sorted(k for k in sys.modules if k.startswith(prefix))
        if matches:
            for name in matches:
                print(f"  • {name}")
        else:
            print("  (none)")

    def locate_module(self, module_name: str) -> Optional[str]:
        """Return the file path of an already-imported module, or None."""
        mod: Optional[ModuleType] = sys.modules.get(module_name)
        if mod is None:
            print(f"[PathwaySeeker] '{module_name}' is not in sys.modules (not imported yet).")
            return None
        path = getattr(mod, "__file__", None)
        if path:
            print(f"[PathwaySeeker] '{module_name}' found at: {path}")
        else:
            print(f"[PathwaySeeker] '{module_name}' is a built-in or namespace package.")
        return path


def show_module_origin(module: ModuleType) -> None:
    """Pretty-print the origin information for any module object."""
    name = getattr(module, "__name__", "unknown")
    file_ = getattr(module, "__file__", "built-in")
    package = getattr(module, "__package__", None)
    spec = getattr(module, "__spec__", None)
    loader = spec.loader.__class__.__name__ if spec and spec.loader else "unknown"

    print(f"\n[Module Origin] {name}")
    print(f"  file    : {file_}")
    print(f"  package : {package}")
    print(f"  loader  : {loader}")
