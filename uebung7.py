import math

"""Uebung 7-1"""


def mysqrt(a: int, x: int) -> float:
    while True:
        y = (x + a / x) / 2
        if y == x:
            return y
        x = y


def test_quadrat():
    print('{:<5} {:<20} {:<20} {:<20}'.format("a", "mysqrt(a)", "math.sqrt(a)", "diff"))
    for a in range(1, 10):
        print('{:<5} {:<20} {:<20} {:<20}'.format(a, mysqrt(a, 3), math.sqrt(a), math.sqrt(a) - mysqrt(a, 3)))


print(test_quadrat())

########################################################################################################################
"""Uebung 7-2"""


def eval_Schleife():
    while True:
        msg = input("-> ")
        if msg == "fertig":
            return print("Terminated!")
        print(eval(msg))


# eval_Schleife()


########################################################################################################################
"""Uebung 7-3"""


def schaetzung_pi() -> float:
    k = 0
    summe = 0
    term = 1

    while term > (10 ** -15):
        term = (math.factorial(4 * k) * (1103 + 26390 * k)) / (math.factorial(k) ** 4 * 396 ** (4 * k))
        summe = summe + term
        k += 1

    return 1 / (2 * math.sqrt(2) / 9801 * summe)


print(schaetzung_pi())
