# To calculate radius whose Sphere area is given
import math
area=float(input("Enter the area of sphere in square.cm "))
radius=math.sqrt(area/(4*math.pi)) # math.pi can be replaced by value of pi(approx 3.14)
print("Radius of requires Sphere is:",radius)
