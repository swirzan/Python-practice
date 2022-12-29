num1 = float(input("Enter a number: "))
opearate = input("Enter an operator: ")
num2 = float(input("Enter a second number: "))

if opearate == "+":
    print(num1 + num2)
elif opearate == "-":
    print(num1 - num2)
elif opearate == "/":
    print(num1 / num2)
elif opearate == "*":
    print(num1 * num2)
else:
    print("Invalid opearator")


# Output
# 12 + 5 = 17.0
# 12 - 5 = 7.0
# 12 / 5 = 2.4
# 12 * 5 = 60.0
