import numpy as np
# Creating a numpy array
degree = float(input("ENTER THE DEGREE YOU WANT TO CALCULATE : "))
# Convert degree to radians since trigonometric functions in numpy use radians
radian = degree * (np.pi / 180)
# Calculate sine value
sine_value = np.sin(radian)
# Calculate cosine value
cosine_value = np.cos(radian)
# Calculate tangent value 
tan_value = sine_value / cosine_value
# Calculate cotangent value as reciprocal of tangent
cot_value = 1 / tan_value
# Calculate secant value as reciprocal of cosine
sec_value = 1 / cosine_value
# Calculate cosecant value as reciprocal of sine
cosec_value = 1 / sine_value

# Print all calculated values
print(f"The sine of {degree} degrees is: {sine_value}")
print(f"The cosine of {degree} degrees is: {cosine_value}")
print(f"The tan of {degree} is : {tan_value}")
print(f"The cot of {degree} is : {cot_value}")
print(f"The sec of {degree} is : {sec_value}")
print(f"The cosec of {degree} is : {cosec_value}")

# Add comments to explain specific conditions
if (cot_value) == (tan_value):
    print(f"The cotangent and tangent values are equal. This occurs at an angle of π/4 radians or 45 degrees.")
else:
    print("The cotangent and tangent values are not equal.")