import re

file = open("slowa.txt")
lines = file.readlines()
ile = 0

for i in lines:
    if re.search(r"k.t", i) != None:
        ile += 1

print("Ile? tyle: " + str(ile))