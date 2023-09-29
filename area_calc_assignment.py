from area.triangle import Triangle
from area.Circle import Cir
from area.Ellipse import Ellipse
from area.kite import Kite

if "__main__" == __name__:
    tri1 = Triangle(base=5, height=12)
    print(tri1)

    cir1 = Cir(pie=0,radius=24)
    print(cir1)

    el1 = Ellipse(radius_a=12, radius_b=7)
    print(el1)

    kite1 = Kite(a=6,b=4)
    print(kite1)