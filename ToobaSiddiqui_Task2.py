# BMI Calculator
# Oasis Infobyte - Python Programming Internship (Project 1)

print("BMI Calculator")
print()

# Ask the user for weight and height
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height * height)

# Decide the category
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

# Show the result
print()
print("Your BMI is:", round(bmi, 1))
print("Category:", category)
