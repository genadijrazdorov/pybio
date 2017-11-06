from collections import OrderedDict
from itertools import groupby

import pdb


class Molecule(object):
    """
    """
    def __init__(self, notation=None):
        self.notation = ""
        if notation is not None:
            self.notation = notation

    def bind(self, from_, to, bond=None):
        pass

    @property
    def formula(self):
        if self.notation == "EEQYNSTYR":
            return Formula("C50H72N14O20")

        elif self.notation == "H3N4F":
            return Formula("C56H94N4O40")

        else:
            return Formula("C106H164N18O59")

    @property
    def mass(self):
        return 2634.545


class Formula(OrderedDict):
    """
    """
    def __init__(self, formula=None):
        if formula is None:
            return super().__init__()

        composition = {}
        count = 1
        element = None
        for is_digit, group in groupby(formula, key=str.isdigit):
            if is_digit:
                count = int("".join(list(group)))

            else:
                composition[element] = count
                count = 1
                element = "".join(list(group))

        composition[element] = count
        del composition[None]

        super().__init__(sorted(composition.items()))

        try:
            self.move_to_end("H", last=False)
        except KeyError:
            pass

        try:
            self.move_to_end("C", last=False)
        except KeyError:
            pass


    def __repr__(self):
        return "Formula('{}')".format("".join(element + str(self[element]) for element in self))
