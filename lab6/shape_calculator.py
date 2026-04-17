import geometry_utils
from geometry_utils import circle_area, circle_perimeter, rectangle_area, rectangle_perimeter, triangle_area


operations = {
    "circle_area":geometry_utils.circle_area,
    "rectangle":geometry_utils.rectangle_area,
    "rectangle_perimeter":geometry_utils.rectangle_perimeter,
    "rectangle_area":geometry_utils.rectangle_area,
    "triangle_area":geometry_utils.triangle_area,
}

print("Available shapes: circle,rectangle,triangle")
print("Available calculations: _area, _perimeter, (e.g., circle_area)")

operation = input("Enter the shape type: ")

if operation == "circle_perimeter":
    radius = float(input("Enter the radius of the circle: "))
    print(circle_perimeter(radius))


elif operation == "circle_area":
    radius = float(input("Enter the radius of the circle: "))
    print(circle_area(radius))


elif operation == "rectangle_perimeter":
    width = float(input("Enter the width of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))
    print(rectangle_perimeter(width, height))


elif operation == "rectangle_area":
    width = float(input("Enter the width of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))
    print(rectangle_area(width, height))



elif operation == "triangle_area":
    base = float(input("Enter the width of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    print(triangle_area(base, height))


else:
    print("Invalid operation0")

