from .atom import Atom, Electron

from collections import OrderedDict, abc

import re


def formula(composition):
    """
    """
    try:
        formula = composition.formula

    except AttributeError:
        formula = Formula(composition)

    return formula


class Formula(OrderedDict):
    """Molecular formula

    """
    def __init__(self, formula=None):
        """

        Parameters:
        -----------
        formula : str or Mapping
            formula as a string or Atom-to-count mapping
            
        """
        if formula is None:
            return super().__init__()

        if isinstance(formula, abc.Mapping):
            composition = {atom : formula[atom] for atom in formula}
        else:
            composition = self._str2dict(formula)

        super().__init__(composition)
        self._order_by_hill()


    def _order_by_hill(self):
        hillify = lambda atom: (atom.symbol, atom.mass_number or float("inf"))
        atoms = sorted(self.keys(), key=hillify)

        # order C and H
        for atom in atoms:
            if atom.symbol in "CH":
                self.move_to_end(atom)

        # order others
        for atom in atoms:
            if atom.symbol not in "CH":
                self.move_to_end(atom)

        # put electron to end
        if Electron() in self:
            self.move_to_end(Electron())


    @classmethod
    def _str2dict(cls, formula):
        composition = {}
        electrons = 0
        PART = r"(\[)? (?(1)(\d*)) ([A-Z][a-z]?) (?(1)([-+]?\d*) \]) (\d*)"
        for _, A, symbol, z, count in re.findall(PART, str(formula), re.X):
            if count == "":
                count = 1
            else:
                count = int(count)
            if A:
                A = int(A)
            else:
                A = None
            if z:
                if z in "-+":
                    z += "1"
                z = int(z)
                electrons -= z * count
            try:
                composition[Atom(symbol, A)] += count

            except KeyError:
                composition[Atom(symbol, A)] = count

        if electrons:
            composition[Electron()] = electrons

        return composition


    def __str__(self):
        string = ""
        for element in self:
            count = self[element]
            if element.mass_number:
                element = "[{}]".format(element)
            else:
                element = str(element)
            string += element
            if count > 1:
                string += str(count)

        if Electron() in self:
            pos = string.index("e-")
            string = string[:pos]

            charge = -self[Electron()]
            if abs(charge) == 1:
                string += "-+"[charge > 0]
            else:
                string += "{:+d}".format(charge)

        return string


    def __repr__(self):
        return "Formula('{}')".format(str(self))


    def __add__(self, other):
        sum_ = {}
        for atom in set(self) & set(other):
            sum_[atom] = self[atom] + other[atom]
        for atom in set(self) - set(other):
            sum_[atom] = self[atom]
        for atom in set(other) - set(self):
            sum_[atom] = other[atom]
        return Formula(sum_)
