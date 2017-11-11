from pybio import Molecule, Atom

from collections import OrderedDict
import pytest

A = Atom


@pytest.fixture
def methane():
    """Molecule instance of methane"""
    methane = Molecule()
    C = A("C")
    for __ in range(4):
        methane.bind(C, A("H"))
    return methane

@pytest.fixture
def ammonium_ion():
    """Molecule instance of ammonium ion"""
    nh4 = Molecule()
    N = A("N")
    for __ in range(4):
        nh4.bind(N, A("H"))
    nh4.charge = +1
    return nh4

@pytest.fixture
def nh4cl(ammonium_ion):
    """Molecule instance of ammonium chloride"""
    nh4cl = Molecule()
    nh4cl.bind(ammonium_ion, Atom("Cl", charge=-1))

    return nh4cl


class TestMolecule():
    def test_add_atom(self):
        molecule = Molecule()
        molecule.add(A("C"))
        assert molecule.atoms == {A("C"),}

    def test_bind_atoms(self):
        molecule = Molecule()
        molecule.bind(A("C"), A("H"))

        assert molecule.atoms == {A("C"), A("H")}
        assert molecule.bonds == {frozenset({A("C"), A("H")})}

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
        assert sorted(str(atom) for atom in methane) == "C H H H H".split()

    def test_formula(self, methane, nh4cl):
        assert methane.formula == OrderedDict(((A("C"), 1), (A("H"), 4)))
        assert nh4cl.formula == OrderedDict(((A("H"), 4), (A("Cl"), 1), (A("N"), 1)))

    def test_groups(self, ammonium_ion, nh4cl):
        assert nh4cl.groups == {ammonium_ion, A("Cl", charge=-1)}
