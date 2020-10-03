def prime(a):
    i = 2
    while a % i != 0:
        i += 1
    return i == a
for number in range(2,100):
   if prime(number) == True & prime(number + 2) == True:
        print("({}, {})".format(number, number + 2))