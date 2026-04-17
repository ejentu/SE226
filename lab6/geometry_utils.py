import math


def circle_area(radius):
    if radius < 0:
        return "The radius cannot be less than 0"
    else:
        return math.pi * radius**2


def circle_perimeter(radius):
    if radius < 0:
        return "The radius cannot be less than 0"
    else:
        return radius*2*math.pi

def rectangle_area(width, height):
    if width < 0 or height < 0:
        return "The width or height cannot be less than 0"
    else:
        return width*height

def rectangle_perimeter(width, height):
    if width < 0 or height < 0:
        return "The width or height cannot be less than 0"
    else:
        return (width+height)*2

def triangle_area(base, height):
    if base < 0 or height < 0:
        return "The width or height cannot be less than 0"
    else:
        return base*height/2


