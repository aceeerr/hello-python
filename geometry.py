import math
from math import sqrt
# def area_circle (radius):
#     return math.pi*radius**2

# if __name__ == "__main__":
#     print("this is from geometry.py")

def triangle_perimeter (a,b,c):
    return a+b+c 
    

def triangle_heronsarea (a,b,c):
    s = triangle_perimeter(a,b,c)/2
    A = sqrt(s*((s-a)*(s-b)*(s-c)))
    return A