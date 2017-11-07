from collections import OrderedDict
from itertools import groupby


class Formula(OrderedDict):
    """
    """
    def __init__(self, formula=None):
        if formula is None:
            return super().__init__()

        composition = {}
        count = ""
        element = ""

        def record():
            nonlocal composition, count, element
            if count == "":
                count = 1
            composition[element] = int(count)

        for char in str(formula):
            if char.isdigit():
                count += char

            elif char.islower():
                element += char

            elif char.isupper():
                record()

                count = ""
                element = char

            else:
                raise ValueError

        record()
        del composition[""]

        super().__init__(sorted(composition.items()))

        try:
            self.move_to_end("H", last=False)
        except KeyError:
            pass

        try:
            self.move_to_end("C", last=False)
        except KeyError:
            pass


    def __str__(self):
        string = ""
        for element in self:
            count = self[element]
            if count == 1:
                string += element
            else:
                string += element + str(count)
        return string


    def __repr__(self):
        return "Formula('{}')".format(str(self))
