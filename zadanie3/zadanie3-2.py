import string

alphabet = string.ascii_lowercase
file = open("slowa.txt")
lines = file.readlines()
ile = 0
najdluzsze = ""

for slowo in lines:
    nowy = ""
    slowo = slowo.strip()

    for litera in slowo:
        index = alphabet.find(litera)
        index += 13 + 1

        if index > len(alphabet):
            index -= len(alphabet)
    
        nowy += alphabet[index - 1]

    if slowo == nowy[::-1]:
        ile += 1

        if len(slowo) > len(najdluzsze):
            najdluzsze = slowo

print("Ile? Tyle:", ile)
print("A o to i najdłuższe z nich:", najdluzsze)