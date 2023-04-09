from collections import Counter

fin = open('wortliste.txt')

"""Uebung 9-1"""


def print_woerter_laenger_20():
    for zeile in fin:
        wort = zeile.strip()
        if len(wort) > 20:
            print(wort)


########################################################################################################################
"""Uebung 9-2"""


def hat_kein_e():
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


def vermeiden(wort: str, forbidden: str):
    flag = True
    for s in wort:
        for a in forbidden:
            if s == a:
                flag = False
    return flag


# print(vermeiden("aaaaaaaabn", "cden"))

def serach_for_words_without(forbidden: str):
    for zeile in fin:
        flag = True
        wort = zeile.strip()
        for s in wort:
            for a in forbidden:
                if s == a:
                    flag = False
        if flag:
            print(wort)


# print(serach_for_words_without("aeiou"))

########################################################################################################################
"""Uebung 9-4"""


def verwendet_nur(wort: str, nichtvorhanden: str):
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


print(verwendet_nur("Hallo", "Halo"))
