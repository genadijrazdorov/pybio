from pybio.formula import Formula
from pybio import Atom, Electron

from collections import OrderedDict

C = Atom("C")
H = Atom("H")
N = Atom("N")
O = Atom("O")
Cl = Atom("Cl")
e = Electron()

class TestFormula():
    def test_CH4(self):
        assert Formula("CH4") == OrderedDict(((C, 1), (H, 4)))

    def test_Hill_ordering(self):
        assert Formula("H4C") == OrderedDict(((C, 1), (H, 4)))
        assert Formula("NH4[Cl-]") == OrderedDict(((H, 4), (Cl, 1), (N, 1), (e, 1)))

    def test_different_isotopes(self):
        assert Formula("[12C]CH6") == OrderedDict([(Atom("12C"), 1), (C, 1), (H, 6)])

    def test_ions(self):
        assert Formula("CO[O-]2") == OrderedDict([(C, 1), (O, 3), (e, 2)])
        assert Formula("[N+]H4") == OrderedDict([(H, 4), (N, 1), (e, -1)])

    def test_repr(self):
        assert repr(Formula("CH4")) == "Formula('CH4')"
        assert repr(Formula("CO[O-]2")) == "Formula('CO3--')"

    def test_addition(self):
        assert Formula("CH4") + Formula("CH4") == Formula("C2H8")
        assert Formula("CH3") + Formula("OH") == Formula("CH4O")
