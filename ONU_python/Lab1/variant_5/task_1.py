import math

def function(x, eps):
    previous = 0
    sum = 1
    i = 1
    while math.fabs(sum - previous) > eps:
        previous = sum
        sign = (-1) ** (i-1)
        num = x ** (2*i-1)
        den = math.factorial(2*i-1)
        sum += sign * num / den
        i += 1
    return sum - 1
a = function(0.12, 0.00001)
print(a)