import math


def textausgabe():
    print('Hallo')
    print('Welt')


# textausgabe()

########################################################################################################################
"""Uebung 3-1"""


def rechts_ausgeben(s: str) -> None:
    print(" " * (70 - len(s)) + s)


rechts_ausgeben("Allen")
rechts_ausgeben("test")
rechts_ausgeben("a")

"""Uebung 3-2"""


def mach_zwei(f: any, x: str) -> None:
    f(x)
    f(x)


def print_spam(x: str) -> None:
    print(x)


mach_zwei(print_spam, "SPAM")


def mach_vier(f: any, x: str) -> None:
    mach_zwei(f, x)
    mach_zwei(f, x)


mach_vier(print_spam, "SPAM")

########################################################################################################################
"""Uebung 3-3"""


def raster(x: int) -> None:
    for i in range(x):
        print("+", end="")
        line_add(x)
        print()
        row_pipe(x)
    print("+", end="")
    line_add(x)


def line_add(x: int) -> None:
    print(("-" * 4 + "+") * x, end="")


def line_pipe(x: int) -> None:
    print("|", end="")
    print(((" " * 4 + "|") * x))


def row_pipe(x: int) -> None:
    for i in range(4):
        line_pipe(x)


raster(2)
