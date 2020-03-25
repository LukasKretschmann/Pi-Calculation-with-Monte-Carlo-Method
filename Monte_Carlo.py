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
