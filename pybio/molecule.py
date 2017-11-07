from .tools.mock import mock
from .formula import Formula


import pdb


class Molecule(object):
    """
    """
    def __init__(self, notation=None):
        self.notation = ""
        if notation is not None:
            self.notation = notation

    @mock
    def bind(self, from_, to, bond=None):
        pass

    @property
    @mock
    def formula(self):
        if self.notation == "EEQYNSTYR":
            return Formula("C50H72N14O20")

        elif self.notation == "H3N4F":
            return Formula("C56H94N4O40")

        else:
            return Formula("C106H164N18O59")

    @property
    @mock
    def mass(self):
        return 2634.545


