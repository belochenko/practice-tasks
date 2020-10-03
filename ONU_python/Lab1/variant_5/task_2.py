def reverse (n):
	result = n[::-1]
	return result

def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

name = input("Enter your name ")
a = ""
for i in name :
	a += str(ord(i))
a = reverse(a)
b = ""
for i in a:
    if int(i)%2 != 0:
        b += i
        break
    else:
        b += i
b = reverse(b)
if (int(b) == 1):
	print("True")
else:
	b = IsPrime(int(b))
	print(b)