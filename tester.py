import random
import math

array = []
for i in range(100000):
    run = True
    total = 0
    x = 0
    while run:
        var = random.randrange(1, 10000)
        total += var
        x += 1
        if 555 <= total/100:
            # checks our average result of [x: 11.76, var:66.68, or total:588.31]
            array.append(total)
            run = False

double_check = []
for i in range(100000):
    mean = sum(array)/100000
    double_check.append(mean)

real_mean = sum(double_check)/100000

tripple_check = []
for i in range(100000):
    mean = sum(double_check)/100000
    tripple_check.append(mean)

true_mean = sum(tripple_check)/100000
print(true_mean)
