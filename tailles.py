import random

f=open("tailles.csv","w")
for i in range(173):
    number = random.randint(0,100)
    if number > 0 and number < 40:
        longueur = random.randint(8,11)
        f.write(str(longueur)+"\n")
    if number > 40 and number < 94:
        longueur = random.randint(12,18)
        f.write(str(longueur)+"\n")
    else:
        longueur = random.randint(19,24)
        f.write(str(longueur)+"\n")
