liczba_wywolan = 0

def F(x):
    global liczba_wywolan
    liczba_wywolan += 1

    if x == 0:
        return 0
    else:
        return 2 + F(x // 2)

print(F(35), liczba_wywolan)

#2.2
for i in range (0, 1000000):
    if(F(i) == 18):
        print(i)