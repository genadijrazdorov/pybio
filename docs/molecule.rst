Molecule
********

    Any constitutionally or isotopically distinct atom, molecule, ion, ion
    pair, radical, radical ion, complex, conformer etc., identifiable as a
    separately distinguishable entity. (Molecular entity)

    -- http://goldbook.iupac.org/html/M/M03986.html

Molecular entity based on molecular graph

https://wiki.python.org/moin/PythonGraphApi

::

    >>> from pybio import Molecule, Atom
    >>> from pybio.formula import formula


Simple molecule
===============

Building a simple molecule::

    >>> methane = Molecule()
    >>> C, hydrogens = Atom("C"), [Atom("H") for _ in range(4)]

    >>> # Just to demostrate atom addition
    >>> methane.add(C)

    >>> # Add atoms and bind them with single covalent bond
    >>> for H in hydrogens:
    ...     methane.bind(C, H)
    ...

    >>> methane
    <Molecule object at 0x...>

Atoms::

    >>> methane.atoms == {Atom('C'), Atom('H')}
    True

Size::

    >>> len(methane)
    5

Atom in a molecule test::

    >>> C in methane
    True

    >>> Atom("C") in methane
    True

Iterating over atoms of a molecule::

    >>> for atom in methane:    # doctest: +SKIP
    ...     print(atom)
    ...
    H
    C
    H
    H
    H

..
    Bonds:


Molecular formula::

    >>> methane.formula
    Formula('CH4')


Complex molecule
================

Building a ammonium chloride molecule::

    >>> # NH4 polyatomic ion

    >>> NH4 = Molecule()
    >>> N, hydrogens = Atom("N"), [Atom("H") for _ in range(4)]

    >>> for H in hydrogens:
    ...     NH4.bind(N, H)
    ...

    >>> NH4.charge = +1

    >>> NH4Cl = Molecule()

    >>> # Bind NH4+ with Cl-
    >>> NH4Cl.bind(NH4, Atom("Cl", charge=-1))

Groups

    A defined linked collection of atoms or a single atom within a molecular
    entity. This use of the term in physical organic and general chemistry is
    less restrictive than the definition adopted for the purpose of
    nomenclature of organic compounds. 

    -- http://goldbook.iupac.org/html/G/G02705.html

::

    >>> for group in NH4Cl:
    ...     print(formula(group))
    ...
    H4N
    Cl

Atoms::

    >>> NH4Cl.atoms == {Atom('N'), Atom('H'), Atom('Cl-')}
    True

Number of groups or atoms::

    >>> len(NH4Cl)
    2

Atom in a molecule test::

    >>> N in NH4Cl
    True

    >>> Atom("N") in NH4Cl
    True

Iterating over atoms of a molecule::

    >>> for atom in NH4Cl.iter_atoms():    # doctest: +SKIP
    ...     print(atom)
    ...
    H
    N+
    H
    H
    H
    Cl-

Molecular formula::

    >>> NH4Cl.formula
    Formula('H4ClN')

