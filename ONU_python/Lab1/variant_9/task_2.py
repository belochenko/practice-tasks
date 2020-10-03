def IsPrime(n):
    d = 2
    while int(n) % d != 0:
        d += 1
    return d == int(n)


quantity = int(input("Please, enter the population of Odessa: "))
p = [int(d) for d in str(quantity)]

ind = 0

for i in p[::-1]:
    if int(i) % 2 != 0:
        break
    p.pop()

result = ''.join([str(i) for i in p])
final_result = IsPrime(result)

print(f"{result} - is the number, which is left")
print(f"Is it prime number? - {final_result}")
