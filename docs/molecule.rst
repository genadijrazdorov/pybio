Molecule
********

    Any constitutionally or isotopically distinct atom, molecule, ion, ion
    pair, radical, radical ion, complex, conformer etc., identifiable as a
    separately distinguishable entity. (Molecular entity)

    -- http://goldbook.iupac.org/html/M/M03986.html

Molecular entity is represented as molecular :ref:`graph <graph>`.
Molecular graph is a set of a chemical groups [#1]_ connected by chemical bonds
[#2]_.


::

    >>> from pybio import Molecule, Atom
    >>> from pybio.molecule import Group


Building a molecule
===================

Building a simple molecule::

    >>> methane = Molecule()

    >>> C = methane.add("C")
    >>> H = methane.add("H")
    >>> methane.bonds[C, H] = 1
    >>> # Add hydrogens and bind them to carbon
    ... for __ in range(3):
    ...     methane.bonds[C, "H"] = 1
    ...

    >>> methane
    <pybio.molecule.Molecule object at 0x...>


Groups can be atoms and/or molecules.

Building a ammonium chloride molecule::

    >>> # NH4 polyatomic ion

    >>> NH4 = Molecule()
    >>> N = NH4.add("N")

    >>> for __ in range(4):
    ...     NH4.bonds[N, "H"] = True
    ...

    >>> NH4.charge = +1

    >>> # complete molecule

    >>> NH4Cl = Molecule()

    >>> # Bind NH4+ with Cl-
    >>> NH4Cl.bonds[NH4, "Cl-"] = True


Working with a molecule
=======================

:ref:`Atoms <atom>` and groups are accessible via groups attribute::

    >>> sorted([atom() for atom in methane.groups])
    [Atom('H'), Atom('H'), Atom('H'), Atom('H'), Atom('C')]

    >>> [group() for group in NH4Cl.groups]     # doctest: +SKIP
    [Molecule(), Atom('Cl', charge='-')]


Bonds are accessible as dictionary::

    >>> methane.bonds[C, H]
    1

    >>> methane.bonds[H, C] is methane.bonds[C, H]
    True


Order of a molecule (number of groups)::

    >>> len(methane)
    5

    >>> len(NH4Cl)
    2


Size of a molecule (number of bonds)::

    >>> len(methane.bonds)
    4

Degree of a group (number of incident bonds)::

    >>> len(methane[C])
    4


Membership testing::

    >>> # Concreate group
    ... C in methane
    True
    >>> N in NH4Cl
    True

    >>> # Atom value
    ... Atom("C") in methane
    True
    >>> Atom("N") in NH4Cl
    True

    >>> # faster if C is not in methane
    ... C in methane.groups
    True

    >>> # bond testing
    ... (C, H) in methane
    True
    >>> # faster
    ... (C, H) in methane.bonds
    True


Walking over atoms::

    >>> list(NH4Cl.walk(N))     # doctest: +SKIP
    [Atom('N+'), Atom('H'), Atom('H'), Atom('H'), Atom('H'), Atom('Cl-')]


.. rubric:: Footnotes

.. [#1] A defined linked collection of atoms or a single atom within a molecular entity. (http://goldbook.iupac.org/html/G/G02705.html)
.. [#2] ... a chemical bond between two atoms or groups of atoms in the case that the forces acting between them are such as to lead to the formation of an aggregate with sufficient stability to make it convenient for the chemist to consider it as an independent 'molecular species'. (http://goldbook.iupac.org/html/B/B00697.html)
