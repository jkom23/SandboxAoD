from cmath import pi
import random
import math

numerator=0
denominator=0
for i in range(1,1000000):
    x = random.uniform(0,1)
    y = random.uniform(0,1)
    if math.sqrt(x**2+y**2)<=1:
        numerator+=1
        denominator+=1
    else:
        denominator+=1

pi_estimate=4*(numerator/denominator)
print(pi_estimate)
print(abs((pi_estimate-math.pi)/math.pi)*100)