import math

def function(x, eps):
    previous = 0
    sum = 1
    i = 1
    while math.fabs(sum - previous) > eps:
        previous = sum
        sign = (-1) ** i
        num = x ** (2*i)
        den = math.factorial(2*i)
        sum += sign * num / den
        i+= 1
    return sum


a = function(0.5, 0.00001)
print(a)