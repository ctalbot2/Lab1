import circle
import rectangle
from circle import calc_area as circle_area
from rectangle import calc_area as rectangle_area
""" 
Since both of these modules include a function named "calc_area", we cannot call "calc_area" in this file without using aliases
"""
while True:
    print("\nGeometry Calculator")
    print("\n1. Calculate Circle Area")
    print("\n2. Calculate Circle Circumference")
    print("\n3. Calculate Rectangle Area")
    print("\n4. Calculate Rectangle Perimeter")
    print("\n5. Exit")
    choice = input("\nEnter your choice (1-5): ")
    if choice == "1":
        radius = int(input("Enter the radius of your circle "))
        print(f"The area of the circle is {circle_area(radius)}")
    elif choice == "2":
        radius = int(input("Enter the radius of your circle "))
        print(f"The circumference of your circle is {circle.calc_circumference(radius)}")
    elif choice == "3":
        width = int(input("Enter the width of your rectangle "))
        height = int(input("Enter the height of your rectangle "))
        print(f"The area of your rectangle is {rectangle_area(width, height)}")
    elif choice == "4":
        width = int(input("Enter the width of your rectangle "))
        height = int(input("Enter the height of your rectangle "))
        print(f"The perimeter of your rectangle is {rectangle.calc_perimeter(width, height)}")
    elif choice == "5":
        break
    input("Press enter to continue...")