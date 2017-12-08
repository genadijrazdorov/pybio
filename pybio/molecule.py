from .tools.mock import mock
from .formula import Formula
from .atom import Atom, Electron

from .tools.graph import Graph, Node


class Group(Node):
    """single node in a molecule

    ..

        A defined linked collection of atoms or a single atom within a
        molecular entity.

        -- http://goldbook.iupac.org/html/G/G02705.html

    """
    def __repr__(self):
        return "<Group {!r}>".format(self())
        
    def __str__(self):
        return "Group {}".format(self())


class Molecule(Graph):
    """Molecular entity

    ..

        Any constitutionally or isotopically distinct atom, molecule, ion, ion
        pair, radical, radical ion, complex, conformer etc., identifiable as a
        separately distinguishable entity.

        -- http://goldbook.iupac.org/html/M/M03986.html

    """
    Node = Group

    class NodesView(Graph.NodesView):
        def add(self, group):
            if isinstance(group, str):
                group = Atom(group)
            group = super().add(group)
            return group

    def __init__(self):
        super().__init__()
        self.groups = self.nodes
        self.bonds = self.edges
