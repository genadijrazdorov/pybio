Atom
====

    Smallest particle still characterizing a chemical element. It consists of a
    nucleus of a positive charge (Z is the proton number and e the elementary
    charge) carrying almost all its mass (more than 99.9%) and Z electrons
    determining its size.

    -- http://goldbook.iupac.org/html/A/A00493.html


Atom API::

    >>> from pybio import Atom

    >>> # Equality
    >>> Atom("C") == Atom("C")
    True

    >>> # Identity
    >>> Atom("C") is Atom("C")
    False

    >>> # Membership
    >>> Atom("C") in {Atom("C")}
    True


