import random

count = 0
orel = 0
reshka = 0
while count < 100:
    coin_flip = random.randint(1, 2)
    if coin_flip == 1:
        orel += 1
    if coin_flip == 2:
        reshka += 1
    count += 1
print (orel)
print (reshka)
