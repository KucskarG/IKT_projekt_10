import random
i = int (input('Irj egy szamot: '))
szam= random.randint(1,5)
if i == szam:
    print('Eltaláltad')
if i > szam:
    print('nagyobb a számod')
else:
    print('kisebb a számod')
