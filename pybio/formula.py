from collections import OrderedDict
from itertools import groupby


class Formula(OrderedDict):
    """
    """
    def __init__(self, formula=None):
        if formula is None:
            return super().__init__()

        composition = {}
        count = 1
        element = None
        for is_digit, group in groupby(formula, key=str.isdigit):
            if is_digit:
                count = int("".join(list(group)))

            else:
                composition[element] = count
                count = 1
                element = "".join(list(group))

        composition[element] = count
        del composition[None]

        super().__init__(sorted(composition.items()))

        try:
            self.move_to_end("H", last=False)
        except KeyError:
            pass

        try:
            self.move_to_end("C", last=False)
        except KeyError:
            pass


    def __repr__(self):
        return "Formula('{}')".format("".join(element + str(self[element]) for element in self))
