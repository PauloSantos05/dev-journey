import math

number = float(input("Type a number: "))
number2 = 30
number3 = 10

pi = math.pi
e = math.e

print('Pi: ', pi)  # value of pi
print('Euler\'s number: ', e)  # value of e
print('Square root: ', math.sqrt(number))  # square root
print('Power: ', math.pow(number, 2))  # power
print('Factorial: ', math.factorial(int(number)))  # factorial
print('Sine: ', math.sin(math.radians(number)))  # sine of 30 degrees
print('Cosine: ', math.cos(math.radians(number)))  # cosine of 60 degrees
print('Tangent: ', math.tan(math.radians(number)))  # tangent of 45 degrees
print('Logarithm: ', math.log(number))  # natural logarithm
print('Logarithm base 10: ', math.log10(number))  # logarithm base 10
print('Ceiling: ', math.ceil(number))  # ceiling of a number
print('Floor: ', math.floor(number))  # floor of a number
print('Round: ', round(number, 2))  # round to 2 decimal places
print('Absolute value: ', math.fabs(-number))  # absolute value
print('Greatest common divisor: ', math.gcd(int(number), int(number2)))  # greatest common divisor
print('Least common multiple: ', math.lcm(int(number), int(number3)))  # least common multiple
print('Max: ', max(number, number2, number3))  # maximum of three numbers
print('Min: ', min(number, number2, number3))  # minimum of three numbers