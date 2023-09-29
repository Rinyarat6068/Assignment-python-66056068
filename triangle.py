from area.shape import Shape

class Triangle(Shape):

    def __init__(self, base, height) -> None:
        self.base = base * 0.5
        self.height = height
        self.triangle_area = 0.0

    def __str__(self) -> str:
        return ('Triangle area of ' + str(self.base) + 'Ux' +
                str(self.height) + 'U :' + str(self.area()))

    def area(self):
        self.triangle_area = self.base * self.height
        return self.triangle_area