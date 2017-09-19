import random

count = 0
heads = 0
tails = 0
while count < 100:
    coin_flip = random.randint(1, 2)
    if coin_flip == 1:
        heads += 1
    if coin_flip == 2:
        tails += 1
    count += 1
print (heads)
print (tails)
