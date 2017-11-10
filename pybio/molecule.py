from .tools.mock import mock
from .formula import Formula
from .atom import Atom, Electron


class Molecule(object):
    """Molecular entity

    Any constitutionally or isotopically distinct atom, molecule, ion, ion
    pair, radical, radical ion, complex, conformer etc., identifiable as a
    separately distinguishable entity.

    """
    def __init__(self):
        """
        """
        self._groups = {}   # id(group): group
        self.bonds = set()  # frozenset(id(group), id(group): bond
        self.charge = 0


    def add(self, group):
        """add a group or atom

        Parameters
        ----------
            group : Molecule or Atom
                Group to be added

        """
        self._groups[id(group)] = group


    @property
    def groups(self):
        """A defined linked collection of atoms or a single atom within a molecular entity.
        """
        return set(self._groups.values())


    @property
    def atoms(self):
        return {atom for atom in self.iter_atoms()}


    def __len__(self):
        return len(self._groups)


    def __contains__(self, group):
        return group in self.groups or group in self.atoms


    def __iter__(self):
        for id_ in self._groups:
            yield self._groups[id_]


    def iter_atoms(self):
        for id_ in self._groups:
            try:
                yield from self._groups[id_]

            except TypeError:
                yield self._groups[id_]


    def bind(self, from_, to, bond=None):
        """bind from and to entity

        Note
        ----
        Entities are added if not already part of self.

        Parameters
        ----------
        from_ : Molecule or Atom
        to    : Molecule or Atom
        bond  : bond type, optional

        """
        self.add(from_)
        self.add(to)
        self.bonds.add(frozenset({from_, to}))


    @property
    def formula(self):
        """Returns molecular formula of self"""
        electrons = 0
        composition = {}
        for atom in self.iter_atoms():
            if atom.charge != 0:
                electrons -= atom.charge
                atom = Atom(atom.symbol, atom.mass_number)
            try:
                composition[atom] += 1

            except KeyError:
                composition[atom] = 1

        if electrons:
            composition[Electron()] = electrons

        return Formula(composition)


    @property
    def formula(self):
        """Returns molecular formula of self"""
        composition = {Electron(): 0}
        for group in self:
            composition[Electron()] -= group.charge
            try:
                composition = group.formula + composition

            except AttributeError:
                atom = Atom(group.symbol, group.mass_number)
                try:
                    composition[atom] += 1

                except KeyError:
                    composition[atom] = 1

        if Electron() in composition and composition[Electron()] == 0:
            del composition[Electron()]

        return Formula(composition)


    @property
    @mock
    def mass(self):
        return 2634.545


    def __repr__(self):
        result = super().__repr__()
        return result.replace("pybio.molecule.", "")


