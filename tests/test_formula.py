from pybio.formula import Formula

from collections import OrderedDict


class TestFormula():
    def test_CH4(self):
        assert Formula("CH4") == {'C':1, 'H':4}

    def test_H4C(self):
        assert Formula("H4C") == OrderedDict(C=1, H=4)

    def test_repr(self):
        assert repr(Formula("CH4")) == "Formula('CH4')"
