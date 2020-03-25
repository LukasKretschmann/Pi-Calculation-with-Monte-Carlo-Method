# Pi-Calculation-with-Monte-Carlo-Method
The circle number Pi is approximated with the Monte Carlo method by four times the probability that a point randomly chosen within the square falls into the circle. Due to the law of large numbers, the variance of the result decreases with increasing number of experiments.

If you have distributed the points, you count how many of them are in a circle. For a large number of points, the frequency distribution of the points changes into the probability. In other words, the number of points in the circle in relation to the total number indicates the probability that the next randomly placed point will also land in the circle and thus this probability also corresponds to the ratio of the circular area to the total area.

I uploaded the code as a classical Python (.py) format and also if somebody needs it as a jupyter notebook (.ipynb).


import random
import math

i = 10000000
count_inside1 = 0

for count in range(i):
    d = math.hypot(random.uniform(0,1),random.uniform(0,1))
    if d < 1: count_inside1 += 1
a = 4*count_inside1/count

print("Anzahl von Tropfen im Kreis:",count*5)
print("Berechneter Wert :",a)
print("Richtiger Wert für PI:  ",3.14159265359)
