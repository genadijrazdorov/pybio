from .tools.mock import mock
from .formula import Formula
from .atom import Atom, Electron


class Molecule(object):
    """Molecular entity

    ..

        Any constitutionally or isotopically distinct atom, molecule, ion, ion
        pair, radical, radical ion, complex, conformer etc., identifiable as a
        separately distinguishable entity.

        -- http://goldbook.iupac.org/html/M/M03986.html

    """
    def __init__(self):
        self._groups = {}   # id(group): group
        self.bonds = set()  # frozenset(id(group), id(group): bond
        self.charge = 0


    def add(self, group):
        """Add chemical group or atom

        Parameters
        ----------
            group : Molecule or Atom
                Chemical group to be added to molecule

        """
        self._groups[id(group)] = group


    @property
    def groups(self):
        """Returns unique groups (including atoms) constituting molecule
        
        ..
        
            A defined linked collection of atoms or a single atom within a
            molecular entity.

            -- http://goldbook.iupac.org/html/G/G02705.html

        """
        return set(self._groups.values())


    @property
    def atoms(self):
        """Unique atoms bound in molecule"""
        return {atom for atom in self.iter_atoms()}


    def __len__(self):
        """Return len(self)"""
        return len(self._groups)


    def __contains__(self, group):
        """Return group in self"""
        return group in self.groups or group in self.atoms


    def __iter__(self):
        """Return iter(self)"""
        for id_ in self._groups:
            yield self._groups[id_]


    def iter_atoms(self):
        """Return iterator over atoms"""
        for id_ in self._groups:
            try:
                yield from self._groups[id_]

            except TypeError:
                yield self._groups[id_]


    def bind(self, from_, to, bond=None):
        """Add and Bind from_ and to entity

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
        """Molecular formula"""
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
        """Molecular mass"""
        return 2634.545


    def __repr__(self):
        result = super().__repr__()
        return result.replace("pybio.molecule.", "")


