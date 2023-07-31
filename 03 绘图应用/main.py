import numpy as np
from PIL import Image


# 画布
class Canvas:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        self.data = np.zeros((width, height, 3), dtype=np.uint8)
        self.data[:] = color

    def make(self):
        img = Image.fromarray(self.data, 'RGB')
        img.save('canvas.png')


# 长方形
class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        canvas.data[self.y:self.y + self.height, self.x:self.x + self.width] = self.color
        canvas.make()


# 正方形
class Square:
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        canvas.data[self.y:self.y + self.side, self.x:self.x + self.side] = self.color
        canvas.make()


canvas = Canvas(50, 50, [255, 255, 0])
rect1 = Rectangle(5, 5, 10, 5, [255, 0, 0])
rect1.draw(canvas)

square = Square(20, 20, 5, [0, 0, 255])
square.draw(canvas)
