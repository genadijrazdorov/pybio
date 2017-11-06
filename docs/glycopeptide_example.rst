Glycopeptide example
********************

::

    >>> from pybio import Peptide, Glycan, Molecule
    
    >>> # Immunoglobulin heavy constant gamma 1 (Homo sapiens)
    >>> # P01857[176 - 184]
    >>> peptide = Peptide("EEQYNSTYR")
    >>> peptide
    Peptide("EEQYNSTYR")

    >>> peptide.formula
    Formula("C50H72N14O20")

    >>> # Major IgG1 Fc N-glycan
    >>> G0F = Glycan(composition="H3N4F")
    >>> G0F
    Glycan(composition="H3N4F")

    >>> G0F.formula
    Formula("C56H94N4O40")

    >>> # glycopeptide build
    >>> glycopeptide = Molecule()
    >>> glycopeptide.bind(peptide, G0F, "glycosidic")

    >>> glycopeptide.formula
    Formula("C106H164N18O59")

    >>> glycopeptide.mass
    2634.545

    >>> glycopeptide.mass
    2633.038599933


