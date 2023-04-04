########################################################################################################################
"""Uebung 8-1"""

print("test".find("s"))

########################################################################################################################
"""Uebung 8-2"""

print("banane".count("a"))

########################################################################################################################
"""Uebung 8-3"""

frucht = "banane"
print(frucht[0:5:2])

########################################################################################################################
"""Uebung 8-3"""

"""def erster(wort: str) -> str:
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
            return False"""


def ist_palindrom(s) -> bool:
    return s.lower() == s[::-1].lower()


print(ist_palindrom("anna"))

########################################################################################################################
"""Uebung 8-4"""
