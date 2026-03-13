"""
Import Pathway Explorer subpackage.

Provides utilities for inspecting how Python locates modules at runtime.
"""

from alchemy.pathways.seeker import PathwaySeeker, show_module_origin

__all__ = ["PathwaySeeker", "show_module_origin"]
