import math
def willis_product():
    half_of_pi = 3.14159265358979312 / 2
    pi_1 = 1.
    i = 1
    while round(pi_1, 4) != round(half_of_pi, 4):
        pi_1 *= ((4 * i ** 2) / (4 * i ** 2 - 1.))
        i += 1
    return(i)