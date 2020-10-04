import math


def precision(eps):
    acur = 0
    while eps <= 1:
        eps *= 10
        acur += 1
    return acur-1


def function(x, eps):
    l = float(x)
    l2 = float(x/2)
    while math.fabs(l - l2) >= float(eps):
        l /= 2
        l2 /= 2
    return format((1 + l2) ** (1/l2),f'.{precision(eps)}f')


a = function(1, float(input()))
print(a)
