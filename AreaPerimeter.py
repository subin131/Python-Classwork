#input from user
import math
radius=int(input("Enter the radius: "))

def areaPerimeter(radius):
    area=math.pi * (radius**0.5)
    perimeter=2*math.pi*radius
    
    print(f"The perimter of cricle is {perimeter} and area is {area}.")
    
areaPerimeter(radius)
