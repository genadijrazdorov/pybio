from .molecule import Molecule


class Glycan(Molecule):
    """
    """
    def __init__(self, notation=None, composition=None):
        if notation is None:
            assert composition is not None
            self.composition = self.notation = composition

        else:
            assert composition is None
            self.notation = notation

    def __repr__(self):
        if hasattr(self, "composition"):
            return "Glycan(composition='{}')".format(self.composition)
        else:
            return "Glycan('{}')".format(self.notation)

