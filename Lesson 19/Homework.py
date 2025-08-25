import math

angle = float(input("Enter the angle"))
radians = math.radians(angle)

cos = math.cos(radians)
tan = math.tan(radians)
sin = math.sin(radians)

print(f"sin({angle}) = {sin}")
print(f"cos({angle}) = {cos}")
print(f"tan({angle}) = {tan}")