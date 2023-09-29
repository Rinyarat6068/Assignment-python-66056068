from area.shape import Shape

class Cir(Shape):

    def __init__(self,pie, radius) -> None:
        self.pie = 3.14
        self.radius = radius**2
        self.cir_area = 0.0

    def __str__(self) -> str:
        return ('Circle area of ' + str(self.pie) + 'x' + str(self.radius) + 'U :' + str(self.area()))

    def area(self):
        self.cir_area = self.pie * self.radius
        return self.cir_area





