from random import randint

samlat_tal = 0

for i in range(10000):
    x = randint(1,100)
    samlat_tal = samlat_tal + x

nytt_tal = samlat_tal/10000

print(nytt_tal)
