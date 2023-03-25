class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, vector):
        self.x = self.x + vector.x
        self.y = self.y + vector.y
        self.z = self.z + vector.z
        return self

    def minus(self, vector):
        self.x = self.x - vector.x
        self.y = self.y - vector.y
        self.z = self.z - vector.z
        return self


    def multiply(self, number):
        self.x = self.x * number
        self.y = self.y * number
        self.z = self.z * number
        return self

    def skalayr(self, vector):
        return self.x * vector.x + self.y * vector.y + self.z * vector.z

    def vectornoe(self, vector):
        a = self.y * vector.z - self.z * vector.y
        b = self.z * vector.x - self.x * vector.z
        c = self.x * vector.y - self.y * vector.x
        self.x = a
        self.y = b
        self.z = c
        return self

if __name__ == '__main__':
    vector = Vector(1,2,3)
    vector1 = Vector(2,3,4)
    vector2 = Vector(2, 3, 4)
    vector6 = Vector(1,2,3)
    result4 = vector.skalayr(vector1)
    result5 = vector6.vectornoe(vector1)
    vector3 = Vector(2, 3, 4)
    result = vector1.add(vector)
    print(result.x, result.y, result.z)
    result2 = vector.minus(vector2)
    print(result2.x, result2.y, result2.z)
    result3 = vector3.multiply(int(input()))
    print(result3.x, result3.y, result3.z)
    print(result4)
    print(result5.x, result5.y, result5.z)