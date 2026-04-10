name = input("Type your name: ")
height = float(input("Type your height in centimeters: "))
weight = float(input("Type your weight in kilograms: "))
imc = weight / (height / 100) ** 2
#imc = weight / (height * height)  # if height is in meters, otherwise use height / 100 to convert to meters
#why ** 2? because we need to square the height in meters to calculate the IMC (BMI) correctly. The formula for BMI is weight (kg) divided by height (m) squared. So, if height is given in centimeters, we first convert it to meters by dividing by 100, and then we square that value to get the correct denominator for the BMI calculation.

print(f"Your IMC is: {imc:.2f}")

if imc < 18.5:
    print("You are underweight.")
elif 18.5 <= imc < 25:
    print("You are normal weight.")
elif 25 <= imc < 30:
    print("You are overweight.")
else:
    print("You are obese.")