expression = input("Expression: ")
x, y, z = expression.split() # splits into 2 integers and the arithmetic function
x = int(x)
z = int(z)
if y == "+":
    answer = float(x + z)
elif y == "-":
    answer = float(x - z)
elif y == "/":
    answer = float(x / z)
elif y == "*":
    answer = float(x * z)
print(answer)
