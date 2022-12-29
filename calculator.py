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
