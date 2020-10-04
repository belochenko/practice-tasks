def is_prime(n):
    if n == 2 or n == 3:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True


def get_num(nums):
    newtel = []
    for num in nums[::-1]:
        if int(num) % 2 == 0:
            newtel.append(num)
        else:
            newtel.append(num)
            break
    return is_prime(int(''.join(newtel[::-1])))


phone_number = str(input("Enter your number: "))
r = get_num(phone_number)
print(r)
