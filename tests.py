"""
Tests for the Alchemy Python imports module.

Validates all four mysteries:
  1. Package initialization
  2. Import pathways
  3. Absolute vs relative imports
  4. Circular dependency solutions
"""

import sys
import importlib


# ── Mystery 1: Package Initialization ──────────────────────────────────────

class TestPackageInitialization:
    def test_alchemy_package_importable(self):
        import alchemy
        assert alchemy is not None

    def test_version_metadata(self):
        import alchemy
        assert alchemy.__version__ == "1.0.0"
        assert alchemy.__author__ == "The Alchemist"

    def test_all_exports(self):
        import alchemy
        assert "Cauldron" in alchemy.__all__
        assert "ELEMENTS" in alchemy.__all__

    def test_cauldron_reexported_from_top_level(self):
        from alchemy import Cauldron
        assert Cauldron is not None

    def test_elements_constant_reexported(self):
        from alchemy import ELEMENTS
        assert isinstance(ELEMENTS, dict)
        assert len(ELEMENTS) == 4

    def test_cauldron_brew(self):
        from alchemy import Cauldron
        c = Cauldron()
        c.add("fire")
        c.add("water")
        result = c.brew()
        assert "fire" in result
        assert "water" in result
        assert "Philosopher's Stone" in result

    def test_cauldron_empty_brew(self):
        from alchemy import Cauldron
        c = Cauldron()
        assert c.brew() == "The cauldron is empty."


# ── Mystery 2: Import Pathways ──────────────────────────────────────────────

class TestImportPathways:
    def test_elements_subpackage_importable(self):
        from alchemy import elements
        assert elements is not None

    def test_all_elements_accessible(self):
        from alchemy.elements import fire, water, earth, air
        for elem in (fire, water, earth, air):
            assert hasattr(elem, "NAME")
            assert hasattr(elem, "SYMBOL")
            assert hasattr(elem, "PROPERTY")
            assert hasattr(elem, "describe")

    def test_elements_dict_keys(self):
        from alchemy.elements import ELEMENTS
        assert set(ELEMENTS.keys()) == {"fire", "water", "earth", "air"}

    def test_each_element_has_symbol_and_property(self):
        from alchemy.elements import ELEMENTS
        for name, info in ELEMENTS.items():
            assert "symbol" in info, f"{name} missing 'symbol'"
            assert "property" in info, f"{name} missing 'property'"

    def test_sys_path_is_list(self):
        assert isinstance(sys.path, list)
        assert len(sys.path) > 0

    def test_alchemy_in_sys_modules_after_import(self):
        import alchemy  # noqa: F401
        assert "alchemy" in sys.modules

    def test_pathway_seeker_locate_module(self, capsys):
        from alchemy.pathways import PathwaySeeker
        import alchemy.elements.fire  # ensure it is loaded
        seeker = PathwaySeeker()
        path = seeker.locate_module("alchemy.elements.fire")
        assert path is not None
        assert path.endswith("fire.py")

    def test_show_search_path_prints(self, capsys):
        from alchemy.elements import show_search_path
        show_search_path()
        captured = capsys.readouterr()
        assert "sys.path" in captured.out or "Python searches" in captured.out

    def test_show_module_origin(self, capsys):
        from alchemy.pathways import show_module_origin
        import alchemy.elements.fire as fire_mod
        show_module_origin(fire_mod)
        captured = capsys.readouterr()
        assert "alchemy.elements.fire" in captured.out


# ── Mystery 3: Absolute vs Relative Imports ─────────────────────────────────

class TestAbsoluteVsRelativeImports:
    def test_absolute_import_works(self):
        from alchemy.elements import fire
        assert fire.NAME == "fire"

    def test_absolute_import_nested(self):
        from alchemy.elements.fire import describe
        result = describe()
        assert "Fire" in result
        assert "transformation" in result

    def test_transmutations_absolute_function(self, capsys):
        from alchemy.transmutations import demonstrate_absolute
        demonstrate_absolute()
        captured = capsys.readouterr()
        assert "Absolute" in captured.out
        assert "fire" in captured.out.lower()

    def test_transmutations_relative_function(self, capsys):
        from alchemy.transmutations import demonstrate_relative
        demonstrate_relative()
        captured = capsys.readouterr()
        assert "Relative" in captured.out
        assert "fire" in captured.out.lower()

    def test_absolute_and_relative_produce_same_element_data(self):
        # Absolute path
        from alchemy.elements import fire as fire_abs
        # Relative path (via the transmutations package which uses relative imports)
        from alchemy.transmutations.relative_path import fire as fire_rel
        assert fire_abs.NAME == fire_rel.NAME
        assert fire_abs.SYMBOL == fire_rel.SYMBOL


# ── Mystery 4: Circular Dependency Solutions ────────────────────────────────

class TestCircularDependencies:
    def test_philosopher_importable_without_error(self):
        from alchemy.circle_of_life.philosopher import Philosopher
        assert Philosopher is not None

    def test_stone_importable_without_error(self):
        from alchemy.circle_of_life.stone import PhilosophersStone
        assert PhilosophersStone is not None

    def test_philosopher_seek_stone_insufficient_wisdom(self):
        from alchemy.circle_of_life.philosopher import Philosopher
        p = Philosopher(name="Novice", wisdom=10)
        result = p.seek_stone()
        assert "needs" in result
        assert "wisdom" in result

    def test_philosopher_seek_stone_sufficient_wisdom(self):
        from alchemy.circle_of_life.philosopher import Philosopher
        p = Philosopher(name="Master", wisdom=100)
        result = p.seek_stone()
        assert "created" in result
        assert "Stone" in result

    def test_philosopher_study_increases_wisdom(self):
        from alchemy.circle_of_life.philosopher import Philosopher
        p = Philosopher(name="Apprentice", wisdom=0)
        p.study(30)
        assert p.wisdom == 30

    def test_stone_transmute(self):
        from alchemy.circle_of_life.stone import PhilosophersStone
        stone = PhilosophersStone(creator="Alchemist")
        result = stone.transmute()
        assert "gold" in result

    def test_stone_grant_immortality(self):
        from alchemy.circle_of_life.stone import PhilosophersStone
        stone = PhilosophersStone(creator="Alchemist")
        result = stone.grant_immortality()
        assert "immortality" in result

    def test_shared_constants(self):
        from alchemy.circle_of_life.shared import WISDOM_THRESHOLD, TRANSMUTATION_FORMULA
        assert WISDOM_THRESHOLD == 100
        assert "gold" in TRANSMUTATION_FORMULA

    def test_demonstrate_circular_solution_runs(self, capsys):
        from alchemy.circle_of_life import demonstrate_circular_solution
        demonstrate_circular_solution()
        captured = capsys.readouterr()
        assert "Lazy" in captured.out or "late import" in captured.out.lower()
        assert "gold" in captured.out
