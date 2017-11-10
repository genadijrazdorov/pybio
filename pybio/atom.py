import re
import sys


class Atom(object):
    """Smallest particle still characterizing a chemical element

    Parameters
    ----------
    symbol: str
        Atomic symbol
    mass_number: int, optional
        Atomic mass number (A)
    charge: int, optional
        Charge number

    """
    def __init__(self, symbol, mass_number=None, charge=None):
        A, symbol, z = re.match(r"(\d+)? ([A-Z][a-z]?) ([-+]\d*)?", symbol, re.X).groups()
        self.symbol = symbol

        # string format
        if A or z:
            assert mass_number is None and charge is None
            if A is not None:
                A = int(A)
            self.mass_number = A
            if z is None:
                z = 0
            elif z in "-+":
                z += "1"
            self.charge = int(z)

        # explicit format
        else:
            if charge is None:
                charge = 0
            self.charge = charge
            self.mass_number = mass_number

    @property
    def atomic_number(self):
        """int: Atomic number (Z)"""
        return S2A[self.symbol]

    def __str__(self):
        A, sym, z = self.mass_number, self.symbol, self.charge
        result = "{}{}".format(A or "", sym)
        if z == 1:
            result += "+"
        elif z == -1:
            result += "-"
        elif z != 0:
            result += "{:+d}".format(z)

        return result

    def __repr__(self):
        return "Atom('{}')".format(str(self))

    def __hash__(self):
        return hash((self.symbol, self.mass_number, self.charge))

    def __eq__(self, other):
        S, O = self, other
        return (S.symbol, S.mass_number, S.charge) == (O.symbol, O.mass_number, O.charge)

    def __lt__(self, other):
        S, O = self, other

        S_mass_number = S.mass_number or float("inf")
        O_mass_number = O.mass_number or float("inf")

        return (S.atomic_number, S_mass_number, S.charge) < (O.atomic_number, O_mass_number, O.charge)

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self < other and not self == other

    def __ge__(self, other):
        return not self < other


class Electron(Atom):
    """Subatomic elementary particle with a negative elementary electric charge 

    References
    ----------
    * http://goldbook.iupac.org/html/E/E01975.html
    * https://en.wikipedia.org/wiki/Electron

    """
    symbol = ""
    mass_number = 0
    atomic_number = 0
    charge = -1

    def __init__(self):
        pass

    def __str__(self):
        return "e-"

    def __repr__(self):
        return "Electron()"




S2A = """
    H    1
    He   2
    Li   3
    Be   4
    B    5
    C    6
    N    7
    O    8
    F    9
    Ne   10
    Na   11
    Mg   12
    Al   13
    Si   14
    S    16
    Cl   17
    Ar   18
    K    19
    Ca   20
    Sc   21
    Ti   22
    V    23
    Cr   24
    Mn   25
    Fe   26
    Co   27
    Ni   28
    Cu   29
    Zn   30
    Ga   31
    Ge   32
    As   33
    Se   34
    Br   35
    Kr   36
    Rb   37
    Sr   38
    Y    39
    Zr   40
    Nb   41
    Mo   42
    Ru   44
    Rh   45
    Pd   46
    Ag   47
    Cd   48
    In   49
    Sn   50
    Sb   51
    Te   52
    I    53
    Xe   54
    Cs   55
    Ba   56
    La   57
    Ce   58
    Pr   59
    Nd   60
    Sm   62
    Eu   63
    Gd   64
    Tb   65
    Dy   66
    Ho   67
    Er   68
    Tm   69
    Yb   70
    Lu   71
    Hf   72
    Ta   73
    W    74
    Re   75
    Os   76
    Ir   77
    Pt   78
    Au   79
    Hg   80
    Tl   81
    Pb   82
    Bi   83
    Th   90
    Pa   91
    U    92
""".strip().split()

S2A = {sym: int(A) for sym, A in zip(S2A[::2], S2A[1::2])}
