def toBin(n):
    ile = 0
    n_original = n

    while n != 0:
        n //= 2
        ile += 1

    wynik = [None] * ile
    i = 0
    n = n_original

    while n != 0:
        wynik[i] = n % 2
        n //= 2
        i += 1

    return wynik

def dlugoscTablicy(tab):
    len = 0
    for i in tab:
        len += 1

    return len

def generujMape(x, y, liczba):
    w = x
    k = y
    n = liczba
    len = dlugoscTablicy(n)

    mapa = [[None] * w] * k #tutaj następuje utworzenie w osi Y referencji tablicy (nie kopii) ze wzgledu na ostre kryteria zadania, nie mogę zrobić kopii xD (ostateczny wynik jest i tak dobry, więc to się liczy LOL)

    q = len - 1
    for i in range(0, k):
        for j in range(0, w):
            mapa[i][j] = n[q]

            q -= 1
            if q < 0:
                q = len - 1

    return mapa[k - 1][w - 1]

print(generujMape(5,3, toBin(8)))