class Rectangle():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def move(self, x, y):
        self.x1 += x
        self.x2 += x
        self.y1 += y
        self.y2 += y


class Triangle():

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def move(self, x, y):
        self.x1 += x
        self.y1 += y
        self.x2 += x
        self.y2 += y
        self.x3 += x
        self.y3 += y


def isInclude(r, p):
    if r.y1 > p.y2 and r.y2 < p.y3:
        print("Прямоугольник содержит Треугольник")
    else:
        print("Прямоугольник не содержит Треугольник")


x1 = 4  # x1,y1 - левый верхний угол прямоугольника
y1 = 6
x2 = 10
y2 = 2
# Включение
x1_1 = 9
y1_1 = 4
x1_2 = 11
y1_2 = 6
x1_3 = 13
y1_3 = 4

print("Кординаты прямоугольника(2 точки которые образуют диагональ)"
      "\n[" + str(x1) + "," + str(y1) + "]\n"
        "[" + str(x2) + "," + str(y2) + "]\n"
                                          
      "Кординаты треугольника"                   
      "\n[" + str(x1_1) + "," + str(y1_1) + "]\n"
        "[" + str(x1_2) + "," + str(y1_2) + "]\n"
        "[" + str(x1_3) + "," + str(y1_3) + "]\n")

x = int(input("Введите кординаты смещения по x :"))
yer = int(input("Введите кординаты смещения по y :"))

print("\nНовые кординаты прямоугольника(2 точки которые образуют диагональ)"
      "\n[" + str(x1+x) + "," + str(y1+x) + "]\n"
        "[" + str(x2+x) + "," + str(y2+x) + "]\n"

      "Новые кординаты треугольника"
      "\n[" + str(x1_1+x) + "," + str(y1_1+x) + "]\n"
        "[" + str(x1_2+x) + "," + str(y1_2+x) + "]\n"
        "[" + str(x1_3+x) + "," + str(y1_3+x) + "]\n")

Help = Rectangle(int(x1), int(y1), int(x2), int(y2))
Me = Triangle(x1_1, y1_1, x1_2, y1_2, x1_3, y1_3)

isInclude(Help, Me)
