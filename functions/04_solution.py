import math
def circle_stats(radius):
    area =  math.pi*radius ** 2
    circum = 2 * math.pi * radius
    
    area = math.floor(area * 100 + 0.5) / 100
    circum = math.floor(circum * 100 + 0.5) / 100
    return area, circum
a,c = circle_stats(3)
print("Area:", a)
print("Circumference:", c)
# print(f"Area of circle : {a:.2f}" '\n' f"And Circumference of cricle is: {c:.2f}")
"Since Python's math module doesn't provide decimal rounding directly, "
"we multiply the number by 100, apply math.floor with +0.5 for correct rounding, and divide back by 100."