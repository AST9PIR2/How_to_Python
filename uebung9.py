from collections import Counter

fin = open('wortliste.txt')
fin_eng = open('words.txt')

"""Uebung 9-1"""


def print_woerter_laenger_20() -> None:
    for zeile in fin:
        wort = zeile.strip()
        if len(wort) > 20:
            print(wort)


########################################################################################################################
"""Uebung 9-2"""


def hat_kein_e() -> None:
    counter = 0
    length = 0
    for zeile in fin:
        length += 1
        wort = zeile.strip()
        if wort.count("e") == 0:
            counter += 1
            print(wort)

    print(f"Prozentsatz der enthaltenen Wörter ohne e: {counter / length * 100:.2f}%")


# hat_kein_e()

########################################################################################################################
"""Uebung 9-3"""


def vermeiden(wort: str, forbidden: str) -> bool:
    flag = True
    for s in wort:
        for a in forbidden:
            if s == a:
                flag = False
    return flag


def vermeiden_refactored(wort: str, forbidden: str) -> bool:
    for s in wort:
        if s in forbidden:
            return False

    return True


# print(vermeiden("aaaaaaaab", "cden"))
# print(vermeiden_refactored("aaaaaaaab", "cden"))

def serach_for_words_without(forbidden: str) -> None:
    for zeile in fin:
        flag = True
        wort = zeile.strip()
        for s in wort:
            for a in forbidden:
                if s == a:
                    flag = False
        if flag:
            print(wort)


def serach_for_words_without_refactored(forbidden: str) -> None:
    for zeile in fin:
        wort = zeile.strip()
        if not vermeiden_refactored(wort, forbidden):
            print(wort)


# print(serach_for_words_without("aeiou"))
# print(serach_for_words_without("aeiou"))

########################################################################################################################
"""Uebung 9-4"""


def verwendet_nur(wort: str, nichtvorhanden: str) -> bool:
    testlist = []
    for a in nichtvorhanden:
        testlist.append(a)

    wortlist = []
    for b in wort:
        if b not in wortlist:
            wortlist.append(b)

    if sorted(testlist) == sorted(wortlist):
        return True

    return False


def verwendet_nur_refactored(wort: str, nichtvorhanden: str) -> bool:
    for a in wort:
        if a not in nichtvorhanden:
            return False

    return True


# print(verwendet_nur("Hallo", "Halo"))
# print(verwendet_nur_refactored("Hallo", "Halo"))


########################################################################################################################
"""Uebung 9-5"""


def verwendet_alle(wort: str, vorhanden: str) -> bool:
    testlist = []
    for a in vorhanden:
        testlist.append(a)

    for b in wort:
        if b in testlist:
            testlist.remove(b)

    if testlist == []:
        return True
    else:
        return False


def verwendet_alle_refactored(wort: str, vorhanden: str) -> bool:
    for a in vorhanden:
        if a not in wort:
            return False

    return True


def verwendet_alle_refactored_die_zweite(wort: str, vorhanden: str) -> bool:
    return verwendet_nur_refactored(vorhanden, wort)


# print(verwendet_alle("Hallo", "lo"))
# print(verwendet_alle_refactored("Hallo", "lo"))
# print(verwendet_alle_refactored_die_zweite("Hallo", "lo"))

########################################################################################################################
"""Uebung 9-6"""


def ist_alphabetisch(wort: str) -> bool:
    testlist = []

    for a in wort:
        if a not in testlist:
            testlist.append(a)

    if testlist == sorted(testlist):
        return True

    return False


def ist_alphabetisch_refactored(wort: str) -> bool:
    return list(wort) == sorted(wort)


# print(ist_alphabetisch("Aaaabcde"))
# print(ist_alphabetisch("Aaaabcde"))
# print(ist_alphabetisch_refactored("Aaaabcde"))

########################################################################################################################
"""Uebung 9-7"""


def find_triple_paar():
    for zeile in fin_eng:
        wort = zeile.strip()

        i = 0
        counter = 0
        while len(wort) > 5 and i < len(wort) - 1:
            if wort[i] == wort[i + 1]:
                counter += 1
                i += 2
            else:
                counter = 0
                i += 1

            if counter >= 3:
                print(wort)


# find_triple_paar()

########################################################################################################################
"""Uebung 9-8"""


def ist_palindrom(s) -> bool:
    return s.lower() == s[::-1].lower()


def check_for_palindrome(milage: int):
    while milage != 0:
        if ist_palindrom(str(milage)):
            print(milage)
        milage -= 1


# print(check_for_palindrome(65456))


########################################################################################################################
"""Uebung 9-9"""


def altersvergleich_palindorm(mutter: int, sohn: int):
    geburtsalter = mutter - sohn
    sohn = 0
    print(f"Die Mutter bekommt den Sohn mit {geburtsalter} Jahren")

    while geburtsalter < 99:
        if str(geburtsalter) == str(sohn)[::-1]:
            print(f"Palindrom bei alter von Mutter {geburtsalter} und alter vom Sohn {sohn}")
        geburtsalter += 1
        sohn += 1


altersvergleich_palindorm(73, 37)
