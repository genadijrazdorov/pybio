from pybio import Atom as A


class TestAtom():
    def test_init(self):
        A("C")
        A("C", mass_number=12)
        A("C", mass_number=13, charge=+1)
        assert True

    def test_init_with_string(self):
        C12 = A("12C+2")
        assert C12.symbol == "C"
        assert C12.mass_number == 12
        assert C12.charge == 2

    def test_str(self):
        assert str(A("C", mass_number=13, charge=+1)) == "13C+"
        assert str(A("C", mass_number=13, charge=+2)) == "13C+2"
        assert str(A("C", mass_number=13, charge=-2)) == "13C-2"

    def test_equality(self):
        assert A("C") == A("C")
        assert A("C") != A("N")

        assert A("C") != A("C", mass_number=12)

    def test_identity(self):
        C = A("C")
        assert C is not A("C")
        assert C is C

    def test_membership(self):
        C = A("C")
        assert C in {C}
        assert C in {A("C")}

    def test_comparing(self):
        C = A("C")
        assert C < A("N")
        assert not C >= A("N")
        assert A("12C") < A("13C")
        assert not A("12C") >= C
