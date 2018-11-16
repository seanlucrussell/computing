from math import factorial
width,height = int(raw_input("Desired width: ")), int(raw_input("Desired height: "))
print factorial(width + height) / (factorial(width)*factorial(height))