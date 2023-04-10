"""Uebung 10-1"""


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


def add_sum_of_given_list(liste: list) -> list:
    newlist = []
    while liste:
        newlist = [sum(liste)] + newlist
        liste.pop()

    return newlist


# print(add_sum_of_given_list([1, 2, 3]))


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
