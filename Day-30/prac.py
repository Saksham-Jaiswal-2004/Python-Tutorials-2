height = float(input("Height(m): "))
weight = float(input("Weight(kg): "))
bmi = weight / height ** 2

if height>3:
    raise ValueError("Human height should be within 0 to 3 meters!")
else:
    print(f"BMI: {bmi}")