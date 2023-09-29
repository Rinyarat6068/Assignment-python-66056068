from area.shape import Shape

class Kite(Shape):

    def __init__(self, a, b) -> None:
        self.a = 2*a
        self.b = 2*b
        self.kite_area = 0.0

    def __str__(self) -> str:
        return ('Kite area of ' + str(self.a) +
                'Ux' + str(self.b) + 'U: ' + str(self.area()))

    def area(self):
        self.kite_area = self.a + self.b
        return self.kite_area