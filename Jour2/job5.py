def calculator(x, z, y):
  if z == "+":
    return x + y
  elif z == "-":
    return x - y
  elif z == "*":
    return x * y
  elif z == "/":
    return x / y
  elif z == "%":
    return x % y
  else:
    return "Invalid operator"

# Take input from the user
x = float(input("Enter first number: "))
z = input("Enter operator: ")
y = float(input("Enter second number: "))

# Call the calculator function
result = calculator(x, z, y)
print(result)
