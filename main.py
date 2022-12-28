# print("Hello World")
# Name = "John Smith"
# Age = "20"
# newPatient = True
# name = input("What is your name? ")
# color = input("What is your favourite color? ")
# print(name + " likes " + color)

# weight_lbs = input("Enter Your Weight in pound ")
# weight_kg = int(weight_lbs) * 0.45
# print(weight_kg)

# first = "Syed"
# last = "Wirzan"
# msg = f'{first} [{last}] is a coder'
# print(msg)

# .upper()
# .lower()
# .title()
# .find()
# .replace()
# in operator

# ARITHMETIC OPERATORS
# +
# -
# *
# /
# for int // divide
# % for remainder
# ** for power

# Sum order
# parentheses Always win
# exponentiation 2 ** 2
# multiplication or division
# addition or subtraction

# CONDITIONS
# is_hot = False
# is_cold = False
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")

# print("Enjoy your day")

# price = 1000000
# good_credit = False

# if good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f"Down payment ${down_payment}")

# LOGICAL OPERATORS
# if both are true use AND
# if one of them is true use OR

# has_good_credit = True
# has_criminal_record = False

# if has_good_credit and not has_criminal_record:
#     print("Eligible for loan")

# COMPARISON OPERATORS
# <
# >
# <=
# >=
# ==
# !=

# name = "wirzan"
# if len(name) < 3:
#     print("name must be at least 3 characters")
# elif len(name) > 50:
#     print("name can be a maximum of 50 characters")
# else:
#     print("name looks good")

# weight = int(input("Weight: "))
# unit = input("(L)bs or (K)g: ")

# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f"Your weight is {converted} kgs")
# else:
#     converted = weight // 0.45
#     print(f"Your weight is {converted} pounds")

# *****WHILE LOOP*****

# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print("Congratulations you win!")
#         break
# else:
#     print("You filed!")

# *****EXERCISE******
# command = ""
# started = False
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("Car is already started")
#         else:
#             started = True
#             print("Car Started.....")
#     elif command == "stop":
#         if not started:
#             print("Car is already stopped")
#         else:
#             started = False
#             print("Car stopped")
#     elif command == "help":
#         print('''
# start - for start the car
# stop - for stop the car
# quit - for quit
#         ''')
#     elif command == "quit":
#         break
#     else:
#         print("Sorry, I don't understand that")


# *****FOR LOOP******
# for item in range(1, 11, 2):
#     print(item)


# prices = [10, 20, 30, 40, 50, 60]
# total = 0
# for price in prices:
#     total += price
# print(f"Total: {total}")


# *****NESTED LOOP******
# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output += 'x'
#     print(output)

# ******LISTS******
# names = ['Mosh', 'Jack', 'John', 'Jerry', 'Marry']
# names[0] = "Jon"
# print(names[1:])
# print(names)

# FINDING LARGE NUMBER

# numbers = [1, 4, 5, 6, 20, 90, 100, 1000]
# max_number = max(numbers)
# print(max_number)

# 2nd METHOD
# numbers = [1, 4, 5, 6, 20, 90, 100, 1000]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)

# ******2d LIST******
# matrix = [
#     [1, 2, 3],
#     [3, 4, 5],
#     [6, 7, 8]
# ]
# matrix[0][2] = 90
# print(matrix[0][2])

# *****LIST METHOD******

# numbers = [5, 6, 5, 9, 8, ]
# numbers.append(25)  # for adding item at the end of list
# numbers.insert(3, 5)  # for adding item beginning and middle of list
# numbers.remove(5)  # for removing items
# numbers.clear() # for remove all items
# numbers.pop()  # for removing last item of list
# print(80 in numbers)
# print(numbers.count(5)) #for counting items in lists
# numbers.sort()  # for sorting items in ascending order
# numbers.reverse() # for sorting items in descending order
# numbers2 = numbers.copy() # for copying list
# print(numbers)

# ***EXERCISE***
# letters = ['a', 'b', 'a', 'c', 'd', 'e', 'f', 'g']
# letters = list(dict.fromkeys(letters))
# print(letters)
# ****2nd METHOD****
# letters = ['a', 'b', 'a', 'c', 'd', 'e', 'f', 'g']
# unique = []
# for letter in letters:
#     if letter not in unique:
#         unique.append(letter)
# print(unique)

# ***TUPLE***
# numbers = (1, 2, 3)
# print(numbers[0])

# ****UNPACKING****
# coordinates = (1, 2, 3)
# x, y, z = coordinates
# print(x)

# ****DICTIONARY****
# customer = {
#     "name": "Syed Wirzan",
#     "Age": 17,
#     "is_verified": True
# }
# customer["birthdate"] = "Aug 23 2005"
# print(customer)
'''
phone = input("Phone: ")
digits_mapping = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",

}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)
'''
s = "string"
number = 1
print(s)
print(number)

dummy_list = ['mango', 'app', 'banana', ]

# for index in range(0, 100):
#     print(index)


# for item in dummy_list:
#     print(item)


def print_dummy_list(count: int = 22):
    print(dummy_list, count)


total_items: int = len(dummy_list)
if total_items > 1 == True:
    print_dummy_list(count=total_items)


name = "wirzan"
if len(name) < 3:
    print("name must be at least 3 characters")
elif len(name) > 50:
    print("name can be a maximum of 50 characters")
else:
    print("name looks good")

stars_count = 5
for i in range(0, stars_count):
    if i == stars_count-1:
        break
    for i in range(i+1):
        print("*", end='')

    else:
        print('')
