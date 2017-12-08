from pybio import Molecule, Atom
from pybio.molecule import Group

from collections import OrderedDict
import pytest

import pdb

A = Atom

@pytest.fixture
def molecule():
    """Empty molecule"""
    return Molecule()

@pytest.fixture
def methane():
    """Molecule instance of methane"""
    methane = Molecule()
    C = methane.groups.add("C")
    for __ in range(4):
        methane.bonds[C, "H"] = 1
    return methane

@pytest.fixture
def ammonium_ion():
    """Molecule instance of ammonium ion"""
    nh4 = Molecule()
    N = nh4.groups.add("N")
    for __ in range(4):
        nh4.bonds[N, "H"] = 1
    nh4.charge = +1
    return nh4

@pytest.fixture
def nh4cl(ammonium_ion):
    """Molecule instance of ammonium chloride"""
    nh4cl = Molecule()
    nh4cl.bonds[ammonium_ion, "Cl-"] = 1

    return nh4cl


class TestMolecule():
    def test_add_atom_as_Atom(self, molecule):
        C = molecule.groups.add(A("C"))
        assert set(molecule) == {C}

    def test_add_atom_as_str(self, molecule):
        C = molecule.groups.add("C")
        assert C() == Atom("C")
        assert set(molecule) == {C}

    def test_add_group(self, molecule):
        group = Molecule()
        group = molecule.groups.add(group)
        assert set(molecule) == {group}

    def test_discard_atom(self, molecule):
        C = molecule.groups.add("C")

        molecule.groups.discard(C)
        assert set(molecule) == set()

    def test_bind_atoms(self, molecule):
        C, H = molecule.groups.add("C"), molecule.groups.add("H")
        molecule.bonds[C, H] = 1

        assert set(molecule) == {C, H}
        assert molecule.bonds == {frozenset({C, H}): 1}

    @pytest.mark.skip
    def test_atoms(self, methane, nh4cl):
        C, N, H, Cl = (Atom(symbol) for symbol in "C N H Cl-".split())
        assert methane.atoms == {C, H}
        assert nh4cl.atoms == {N, H, Cl}

    def test_len(self, methane):
        assert len(methane) == 5

    def test_contains_atom(self, methane):
        assert A("C") in methane
        assert A("N") not in methane

    def test_contains_group(self, ammonium_ion, nh4cl):
        assert ammonium_ion in nh4cl

    def test_iter(self, methane):
        assert sorted(str(atom()) for atom in methane) == "C H H H H".split()

    @pytest.mark.skip
    def test_equality(self, molecule, methane):
        assert molecule != methane

        C = molecule.groups.add("C")
        for __ in range(4):
            molecule.bonds[C, "H"] = 1
        assert molecule == methane

