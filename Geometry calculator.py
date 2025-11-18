import math

# Function to calculate area and perimeter of a circle
def circle():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius
    print(f"\nArea of Circle: {area:.2f}")
    print(f"Circumference of Circle: {perimeter:.2f}")

# Function to calculate area and perimeter of a rectangle
def rectangle():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    perimeter = 2 * (length + width)
    print(f"\nArea of Rectangle: {area:.2f}")
    print(f"Perimeter of Rectangle: {perimeter:.2f}")

# Function to calculate area and perimeter of a triangle
def triangle():
    a = float(input("Enter the first side of the triangle: "))
    b = float(input("Enter the second side of the triangle: "))
    c = float(input("Enter the third side of the triangle: "))
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    perimeter = a + b + c
    print(f"\nArea of Triangle: {area:.2f}")
    print(f"Perimeter of Triangle: {perimeter:.2f}")

# Function to calculate area and perimeter of a square
def square():
    side = float(input("Enter the side of the square: "))
    area = side ** 2
    perimeter = 4 * side
    print(f"\nArea of Square: {area:.2f}")
    print(f"Perimeter of Square: {perimeter:.2f}")

# Main program
while True:
    print("\n===== Geometry Calculator =====")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Square")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        circle()
    elif choice == '2':
        rectangle()
    elif choice == '3':
        triangle()
    elif choice == '4':
        square()
    elif choice == '5':
        print("Exiting Geometry Calculator. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")