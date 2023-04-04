import math
import turtle

"""Uebung 4-1"""

bob = turtle.Turtle()
bob.speed("fastest")


def quadrat(t: turtle.Turtle, laenge: int) -> None:
    for i in range(4):
        t.fd(laenge)
        t.lt(90)


def polygon(t: turtle.Turtle, laenge: float, n: int) -> None:
    for i in range(n):
        t.fd(laenge)
        t.lt(360.0 / n)


def kreis(t: turtle.Turtle, r: int) -> None:
    u = 2 * r * math.pi
    polygon(t, u, r)


def bogen(t: turtle.Turtle, r: int, winkel: int) -> None:
    u = 2 * r * math.pi
    for i in range(winkel):
        t.lt(1)
        t.fd(u / 360.0)


def gleichscheckligesdreieck(t: turtle.Turtle, laenge: float, winkel: float) -> None:
    t.fd(laenge)
    t.lt(180 - (180.0 - winkel) / 2)
    t.fd(2 * laenge * math.sin(math.radians(winkel / 2)))
    t.lt(180 - (180.0 - winkel) / 2)
    t.fd(laenge)
    t.lt(180 - winkel)


# bogen(bob, 100, 360)

########################################################################################################################
"""Uebung 4-2"""


def blume(t: turtle.Turtle, blaetter: int) -> None:
    for r in range(blaetter):
        for i in range(2):
            bogen(t, 200, 60)
            t.lt(120)
        t.lt(360 / blaetter)


def figur(t: turtle.Turtle, anzahl: int) -> None:
    for i in range(anzahl):
        gleichscheckligesdreieck(t, 200, 360 / anzahl)
        t.lt(360 / anzahl)


def spirale(t: turtle.Turtle, winkel: float) -> None:
    t.fd(1)
    t.lt(winkel)


# blume(bob, 20)
# figur(bob, 5)
# gleichscheckligesdreieck(bob, 200, 80)
# figur(bob, 50)
turtle.mainloop()
