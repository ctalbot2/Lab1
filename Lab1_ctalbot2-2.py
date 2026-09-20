import circle.py
import rectangle.py
from circle import calc_area as circle_area
from rectangle import calc_area as rectangle_area
""" 
Since both of these modules include a function named "calc_area", we cannot call "calc_area" in this file without using aliases
"""