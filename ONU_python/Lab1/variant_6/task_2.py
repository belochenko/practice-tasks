def IsPrime(n):
    if n % 2 == 0 and n != 2:
        return False
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n



def IsHalfPrime(n):
    if n % 2 == 0 and IsPrime(n / 2):
        result = n / 2
        return (2, int(result)) 
    else:
        d = 3
        while d * d <= n:
            if IsPrime(d) and n % d == 0:
                result1 = n / d
                if IsPrime(result1):
                    return (int(result1), d)
            d += 2
    return('This number is not half-prime!')



n = int(input('Enter n: '))
print(IsHalfPrime(n))
