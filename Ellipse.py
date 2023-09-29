from area.shape import Shape

class Ellipse(Shape):

    def __init__(self, radius_a, radius_b) -> None:
        self.radius_a = 3.14 * radius_a
        self.radius_b = radius_b
        self.ellipse_area = 0.0

    def __str__(self) -> str:
        return ('Ellipse area of ' + str(self.radius_a) +
                'Ux' + str(self.radius_b) + 'U: ' + str(self.area()))

    def area(self):
        self.ellipse_area = self.radius_a * self.radius_b
        return self.ellipse_area