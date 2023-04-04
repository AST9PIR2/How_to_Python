"""Uebung 6-2"""


def ack(m: int, n: int) -> int:
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))
    else:
        return - 1


print(ack(3, 4))

########################################################################################################################
"""Uebung 6-3"""


def erster(wort: str) -> str:
    return wort[0]


def letzter(wort: str) -> str:
    return wort[-1]


def mitte(wort: str) -> str:
    return wort[1:-1]


def ist_palindorm(wort: str) -> bool:
    if len(wort) % 2 != 0:
        return False
    else:
        if erster(wort.lower()) == letzter(wort.lower()):
            if len(wort) > 2:
                return ist_palindorm(mitte(wort))
            else:
                return True
        else:
            return False


print("Ist das angegebene Wort ein Palindrom? ", ist_palindorm("Anna"))

########################################################################################################################
"""Uebung 6-4"""


def ist_potenz(a: int, b: int) -> bool:
    if a % b == 0 and b % (a / b):
        return True
    else:
        return False


print(ist_potenz(426878854210636742656, 14))

########################################################################################################################
"""Uebung 6-5"""


def ggt(a: int, b: int) -> int:
    if a % b == 0:
        return b
    else:
        return ggt(b, (a % b))


print(ggt(6, 4))
