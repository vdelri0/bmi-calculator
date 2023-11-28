height = input("Insert your height:\n")
weight = input("Insert your weight:\n")

bmi = int(weight) / float(height)**2

bmi_as_int = int(bmi)
print("Your Body Mass Index is:", bmi_as_int)