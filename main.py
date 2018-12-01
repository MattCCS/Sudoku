
from typing import Dict, Set

ALL_VALUES = "123456789ABCDEFG"

RANK = 3
assert 1 <= RANK <= 4

VALUES = ALL_VALUES[:RANK**2]


BOARD = """\
. 9 8 7 . . . . 5
. . . . 3 . 8 9 .
4 . 5 6 . . 1 . 7
6 . . . . 7 . . .
5 . . . . . 3 . 6
8 . 1 . . . . 7 .
. . . . . 5 . . .
. . . . . . 4 . .
1 . . . . 8 5 . .
"""


class NoValueError(Exception): pass  # noqa


class Cell:
    def __init__(self, values=None):
        # print(f"__init__(values={values})")
        if values is None:
            values = VALUES
        self._values = set(values)

    @property
    def val(self):
        if len(self._values) == 1:
            return list(self._values)[0]
        raise NoValueError()

    @val.setter
    def val(self, value):
        self._values = set([value])

    def __bool__(self):
        """Return whether this cell is solved"""
        return len(self._values) == 1

    # collection operations
    def __len__(self):
        return len(self._values)

    def __iter__(self):
        return iter(self._values)

    def __contains__(self, key):
        return key in self._values

    # set operations
    def __sub__(self, other):
        # print(f"__sub__({self}, {other})")
        return Cell(values=(self._values - other))

    def __rsub__(self, other):
        # print(f"__rsub__({self}, {other})")
        return Cell(values=(other - self._values))

    def __and__(self, other):
        return Cell(values=(self._values & other))

    def __rand__(self, other):
        return Cell(values=(other & self._values))

    def __or__(self, other):
        return Cell(values=(self._values | other))

    def __ror__(self, other):
        return Cell(values=(other | self._values))

    # human operations
    def __repr__(self):
        return f"Cell({''.join(sorted(self._values))})"


class Board:
    def __init__(self):
        # self.cells: 
        self.rows: Dict[int, Set[Cell]] = {}
        self.columns: Dict[int, Set[Cell]] = {}
        self.boxes: Dict[int, Set[Cell]] = {}

    def get(x, y):
        return list(self.columns[x] & self.rows[y])[0]


def main():
    pass


if __name__ == '__main__':
    main()
