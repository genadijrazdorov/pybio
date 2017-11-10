Molecular Formula
*****************

https://en.wikipedia.org/wiki/Chemical_formula#Molecular_formula

https://en.wikipedia.org/wiki/Chemical_formula#Hill_system

::

    >>> from pybio import Formula, Atom

    >>> methane = Formula("CH4")


Representing & printing::

    >>> methane
    Formula('CH4')

    >>> print(methane)
    CH4


Individual element testing, counting::

    >>> Atom("C") in methane
    True

    >>> Atom("Ca") in methane
    False

    >>> methane[Atom("H")]
    4


Ions::

    >>> Formula("[N+]H4")
    Formula('H4N+')

Isotopes::

    >>> Formula("H4[13C]")
    Formula('[13C]H4')


Hill system::

    >>> for formula in "IBr Cl4C IH3C C2BrH5 H2O4S".split():
    ...     print(formula, "->", Formula(formula))
    IBr -> BrI
    Cl4C -> CCl4
    IH3C -> CH3I
    C2BrH5 -> C2H5Br
    H2O4S -> H2O4S
    
