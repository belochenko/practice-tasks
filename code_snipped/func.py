def area_sq(area):
    print(f"Area {area}")


def sq(n):
    return n ** 2


favorite_numbers = [6, 57, 4, 7, 68, 95]
def square_all(numbers):
     for n in numbers:
         yield n**2
         
squares = square_all(favorite_numbers)
print(list(squares))