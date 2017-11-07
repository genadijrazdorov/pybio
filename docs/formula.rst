Molecular Formula
*****************

https://en.wikipedia.org/wiki/Chemical_formula#Molecular_formula
https://en.wikipedia.org/wiki/Chemical_formula#Hill_system

::

    >>> from pybio import Formula

    >>> methane = Formula("CH4")
    >>> methane
    Formula('CH4')

    >> print(methane)
    CH4

    >>> "C" in methane
    True

    >>> "Ca" in methane
    False

    >>> methane["H"]
    4


    >>> for formula in "IBr Cl4C IH3C C2BrH5 H2O4S".split():
    ...     print(Formula(formula))
    BrI
    CCl4
    CH3I
    C2H5Br
    H2O4S
    


