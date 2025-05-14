height = float(input("Height (in meters): "))
weight = int(input("Weight (in Kg): "))

if height > 3:
    raise ValueError("That does not look like a normal human height")

bmi = weight/ height
print(f" The BMI is {bmi: .2f}")