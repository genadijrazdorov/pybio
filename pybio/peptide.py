from .molecule import Molecule


class Peptide(Molecule):
    """
    """
    def __init__(self, sequence):
        self.sequence = sequence

    def __repr__(self):
        return "Peptide('{}')".format(self.sequence)
