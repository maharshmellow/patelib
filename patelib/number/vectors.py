import math

class vector2D:
    def __init__(self):
        self.__x = 0
        self.__y = 0
    def x(self):
        return self.__x
    def y(self):
        return self.__y
    def mag(self):
        return math.sqrt(self.__x**2+self.__y**2)
    def msgSq(self):
        return self.__x**2+self.__y**2
    def add(self, v):
        if isinstance(v, vector2D):
            self.__x += v.x()
            self.__y += v.y()
        else:
            self.__x += v
            self.__y += v
    def sub(self, v):
        self.add(-v)
    def mul(self, v):
        if isinstance(v, vector2D):
            print("patelib>number>vectors>Vector2D>mul(): Scalar only; use .cross() or .dot()")
        else:
            self.__x *= v;
            self.__y *= v;
    def div(self, v):
        if isinstance(v, vector2D):
            print("patelib>number>vectors>Vector2D>mul(): Scalar only; use .cross() or .dot()")
        else:
            self.mul(-v)
