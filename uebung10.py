"""Uebung 10-1"""
from datetime import datetime
from random import random, randrange
import time


def sum_list(liste: list) -> int:
    temp = 0
    for x in liste:
        if isinstance(x, int):
            temp += x
        else:
            temp += sum_list(x)
    return temp


# print(sum_list([[1, 2], [3, 4], [[2], [2, 3]]]))
# print(sum_list([1, 2, 3, 4, [2], [2, 3]]))


########################################################################################################################
"""Uebung 10-2"""


def cumsum(liste: list) -> list:
    newlist = []
    while liste:
        newlist = [sum(liste)] + newlist
        liste.pop()

    return newlist


print(cumsum([1, 2, 3]))

########################################################################################################################
"""Uebung 10-3"""

a = [1, 2, 3, 4]


def middle(liste: list) -> list:
    return liste[1:][:-1]


# print(middle(a))

########################################################################################################################
"""Uebung 10-4"""


def chop(liste: list) -> None:
    liste.pop()
    liste.pop(0)


# print(a)
# chop(a)
# print(a)

########################################################################################################################
"""Uebung 10-5"""


def is_sorted(liste: list) -> bool:
    return liste == sorted(liste)


# print(is_sorted([1, 3, 2]))
# print(is_sorted([1, 2, 3]))


########################################################################################################################
"""Uebung 10-6"""


def is_anagramm(eingabe: str, pruefung: str) -> bool:
    for x in eingabe.lower():
        if x not in pruefung.lower():
            return False

    return True


# print(is_anagramm("Lager", "Regal"))

########################################################################################################################
"""Uebung 10-7"""


def has_duplicates(liste: list) -> bool:
    for x in liste:
        if liste.count(x) > 1:
            return True
    return False


# print(has_duplicates(['a','b','c','d']))


########################################################################################################################
"""Uebung 10-8"""

'''Achtung! Die Monatstage wurden einfachheitshalber auf max 28 Tage limitiert'''


def date_generator(anzahl: int) -> list:
    dateliste = []
    for x in range(0, anzahl):
        dateliste.append(datetime(2000, randrange(11) + 1, randrange(28) + 1).strftime("%d.%m.%Y"))

    return dateliste


# print(has_duplicates(date_generator(23)))

'''Achtung die Funktion schätzt die Wahrscheinlichkeit im Brute Force stil. Eine genaue Berechnung wäre hier sicher
 vorteilhafter: https://de.wikipedia.org/wiki/Geburtstagsparadoxon'''


def geburtstagspruefung(anzahl: int, personen: int) -> None:
    counter = 0
    for x in range(0, anzahl):
        if has_duplicates(date_generator(personen)):
            counter += 1
    print(f"Bei {personen} ist die Wahrscheinlichkeit{counter / anzahl}% dass sie am selben Tag Geburtstag haben.")


# geburtstagspruefung(100, 23)

########################################################################################################################
"""Uebung 10-9"""


def read_write_append_append() -> list:
    fin = open('wortliste.txt')
    newlist_append = []
    for zeile in fin:
        wort = zeile.strip()
        newlist_append.append(wort)
    fin.close()
    return newlist_append


def read_write_append_brackets() -> list:
    fin = open('wortliste.txt')
    newlist_brackets = []
    for zeile in fin:
        wort = zeile.strip()
        newlist_brackets = newlist_brackets + [wort]
    fin.close()
    return newlist_brackets


def compare_runtime() -> None:
    start1 = time.time()
    func1 = read_write_append_append()
    print(type(func1))
    print(len(func1))
    end1 = time.time()

    start2 = time.time()
    func2 = read_write_append_brackets()
    print(type(func2))
    print(len(func2))
    end2 = time.time()

    print(f"Funktion 1 hat {end1 - start1:.03f}s gebraucht und Funktion 2 hat {end2 - start2:.03f}s gebraucht.")


#compare_runtime()

########################################################################################################################
"""Uebung 10-10"""

#def bisektion(sortedlist: list, gesuchteswort: str):
