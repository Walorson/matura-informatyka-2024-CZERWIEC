file = open("slowa.txt")
lines = file.readlines()
szukane_slowa = []

for slowo in lines:
    slowo = slowo.strip()
    unikalne_litery = set(slowo)

    for litera in unikalne_litery:
        ile = slowo.count(litera)

        if(ile >= len(slowo) / 2):
            szukane_slowa.append(slowo)
            break

print("WYNIK:\n")
for i in szukane_slowa:
    print(i)