import circle
import rectangle
from circle import calc_area as circle_area
from rectangle import calc_area as rectangle_area
""" 
Since both of these modules include a function named "calc_area", we cannot call "calc_area" in this file without using aliases
"""
finished_calculate = False

while finished_calculate == False:
    print("Geometry Calculator")
    print("\n1. Calculate Circle Area")
    print("\n2. Calculate Circle Circumference")
    print("\n3. Calculate Rectangle Area")
    print("\n4. Calculate Rectangle Perimeter")
    print("\n5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        radius = int(input("Enter the radius of your circle "))
        print(f"The area of the circle is {circle_area(radius)}")
    finished_calculate = True