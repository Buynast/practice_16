# Напишите код для описания геометрической фигуры.
# Создайте класс «прямоугольник» с помощью метода init(). На выходе в консоли вам необходимо получить площадь данной фигуры.

class Rectangle:
    def __init__(self, x, y, widht, height):
        self.x = x
        self.y = y
        self.widht = widht
        self.height = height
    def __str__(self):
        return f'Rectangle : {self.x}, {self.y}, {self.widht}, {self.height}'
    def get_area(self):
        return self.x * self.y, self.widht * self.height

rect_1 = Rectangle(5, 10, 50, 100)

print(rect_1)
print(rect_1.get_area())