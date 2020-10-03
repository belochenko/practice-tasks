class Vector:
    def __init__(self, vector1, vector2):
        self.first = vector1
        self.second = vector2

    def __add__(self, *args):
        return args

    def __repr__(self):
        return f'Vector ({self.first}, {self.second})'




v1 = Vector(1, 2)
v1 = [1, 2]
v1 = (1, 2)
v2 = Vector(3, 4)
c = v1 + v2
print(c)