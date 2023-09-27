from math import sin, cos, radians
import pygame as py
g = 10

class Pendulum:

    def __init__(self, m1, m2, l1, l2, x, y, a1, a2, width):

        self.m1 = m1
        self.m2 = m2
        self.l1 = l1
        self.l2 = l2
        self.x = x
        self.y = y
        self.a1 = a1
        self.a2 = a2
        self.a1_v = 0
        self.a2_v = 0
        self.a1_a = 0
        self.a2_a = 0
        self.width = width

    def draw(self, screen, color):

        x1 = self.x + self.l1 * sin(radians(self.a1))
        y1 = self.y + self.l1 * cos(radians(self.a1))

        x2 = x1 + self.l2 * sin(radians(self.a2))
        y2 = y1 + self.l2 * cos(radians(self.a2))

        py.draw.line(screen, color, (self.x, self.y), (x1, y1), self.width)
        py.draw.circle(screen, color, (x1, y1), self.m1)

        py.draw.line(screen, color, (x1, y1), (x2, y2), self.width)
        py.draw.circle(screen, color, (x2, y2), self.m1)

    def move(self):

        # num1 = float(-g*(2*self.m1 + self.m2) * sin(radians(self.a1)))
        # num2 = float(self.m2 * g * sin(radians(self.a1) - 2 * radians(self.a2)))
        # num3 = float(2 * sin(radians(self.a1) - radians(self.a2)) * self.m2)
        # num4 = float(self.a2_v**2 * self.l2 + self.a1_v**2 * self.l1 * cos(radians(self.a1) - radians(self.a2)))
        # den = float(self.l1 * (2 * self.m1 + self.m2 - self.m2 * cos(2 * radians(self.a1) - 2 * radians(self.a2))))
        # self.a1_a =  float(num1 - num2 - num3 * num4 / den)

        # num1 = float(2 * sin(radians(self.a1) - radians(self.a2)))
        # num2 = float(self.a1_v**2 * self.l1 * (self.m1 + self.m2))
        # num3 = float(g * (self.m1 + self.m2) * cos(radians(self.a1)))
        # num4 = float(self.a2_v**2 * self.l2 * self.m2 * cos(radians(self.a1) - radians(self.a2)))
        # den = float(self.l2 * (2 * self.m1 + self.m2 - self.m2 * cos(2 * radians(self.a1) - 2 * radians(self.a2))))

        # self.a2_a = float(num1 * (num2 + num3 + num4) / den)
        
        self.a1_v += self.a1_a
        self.a2_v += self.a2_a
        
        self.a1 += self.a1_v
        self.a2 += self.a2_v
        
