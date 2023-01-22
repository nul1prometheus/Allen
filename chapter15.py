import math
import turtle

class Point:
    """Представление точки в двумерном пространстве"""


blank = Point()
blank1 = Point()
blank.x = 3
blank.y = 4
blank1.x = 6
blank1.y = 7


def print_point(p):
    print('(%g, %g)' % (p.x, p.y))


def distance_between_points(p1, p2):
    # print((p1.x - p2.x)**2)
    distance = math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
    # print(distance)
    return distance


# print(distance_between_points(blank, blank1))

class Rectangle:
    """Define rectangle, attributes: width, height, corner"""


box = Rectangle()
box.width = 100
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0


def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p


center = find_center(box)
print_point(center)
# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()


def draw_rect(somerect):
    turtle.setpos(somerect.corner.x, somerect.corner.y)
    turtle.right(90)
    turtle.forward(somerect.width)
    turtle.left(90)
    turtle.forward(somerect.height)
    turtle.left(90)
    turtle.forward(somerect.width)
    turtle.left(90)
    turtle.forward(somerect.height)
    turtle.done()


# draw_rect(box)


class Circle:
    """some circle, attributes: center (Point), radius"""


circle1 = Circle()
circle1.center = Point()
circle1.center.x = 100
circle1.center.y = 150
circle1.radius = 100

import polygon

def draw_circle(somecircle):
    turtle.pu()
    turtle.goto(somecircle.center.x, somecircle.center.y)
    turtle.setheading(90)
    turtle.left(90)
    turtle.backward(somecircle.radius)
    turtle.setheading(90)
    turtle.pd()
    turtle.circle(somecircle.radius)
    turtle.done()


draw_circle(circle1)
