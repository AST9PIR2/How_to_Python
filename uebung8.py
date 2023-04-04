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


def kleine_buchstaben1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False


"""Diese Funktion prüft nicht das ganze Wort sondern nur den ersten Buchstaben"""


def kleine_buchstaben2(s):
    for c in s:
        if 'c'.islower():
            return True
        else:
            return False

"""Diese Funktion prüft nur ob 'c' klein geschrieben ist"""


def kleine_buchstaben3(s):
    for c in s:
        flag = c.islower()
    return flag

"""Diese Funktion prüft nur den letzten Buchstaben"""

def kleine_buchstaben4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

"""Diese Funktion funktioniert richtig"""

def kleine_buchstaben5(s):
    for c in s:
        if not c.islower():
            return False
        return True

"""Prüft wieder nur den ersten Buchstaben"""

########################################################################################################################
"""Uebung 8-5"""


def rotiere_zeichen(eingabe: str, versatzt: int) -> str:
    msg = ''
    for s in eingabe:
        msg += (chr(ord(s) + versatzt))
    return msg

print(rotiere_zeichen("Hallo", 1))

