import time
import turtle



# print(time.time())


def stunden(time: float) -> float:
    stunden = time / 3600
    return stunden


def jahre(stunden: float) -> float:
    tage = stunden / 8760
    return tage


year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def heute() -> str:
    temp = time.time()
    Jahr = int(1970 + jahre(stunden(temp)))
    time_pased = jahre(stunden(temp)) + 11  # Schaltjahre
    for x in year:
        if (time_pased - x) > 0:
            time_pased = time_pased - x
    return f"Jahr {Jahr}, Tag {int(time_pased)}"


# print(heute())


def beweis_fermat(a: int, b: int, c: int, n: int):
    if a ** n + b ** n == c ** n:
        print("Heiliger Strohsack, Fermant hatte nicht recht!")
    else:
        print("Nein, das funktioniert nicht")


# a = int(input("Bitte gib a ein"))
# b = int(input("Bitte gib b ein"))
# c = int(input("Bitte gib c ein"))
# n = int(input("Bitte gib n ein"))

# beweis_fermat(a, b, c, n)


def ist_dreieck(a: int, b: int, c: int) -> None:
    if a + b <= c or a + c <= b or b + c <= a:
        print("Das kann kein Dreieck werden")
    else:
        print("Aus diesen Seiten kann man ein Dreieck bauen")


'''Diese Rekursion läuft runter bis n==0 wenn n < 0 übergeben wird läuft sie max'''


def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n - 1, n + s)


bob = turtle.Turtle()
bob.speed("fastest")


def zeichne(t, laenge, n):
    if n == 0:
        return
    winkel = 50
    t.fd(laenge * n)
    t.lt(winkel)
    zeichne(t, laenge, n - 1)
    t.rt(2 * winkel)
    zeichne(t, laenge, n - 1)
    t.lt(winkel)
    t.bk(laenge * n)


# ist_dreieck(5, 3, 6)


# recurse(4, 0)

zeichne(bob, 10, 10)
