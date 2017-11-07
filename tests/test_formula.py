from pybio.formula import Formula


class TestFormula():
    def test_CH4(self):
        assert Formula("CH4") == {'C':1, 'H':4}
