#Task 1
# try:
#     firstNumber = int(input("Enter a first number:"))
#     operation = input("Enter an operation:")
#     secondNumber = int(input("Enter a second number:"))
#
#     if operation == "+":
#         print(firstNumber + secondNumber)
#     elif operation == "-":
#         print(firstNumber - secondNumber)
#     elif operation == "*":
#         print(firstNumber * secondNumber)
#     elif operation == "%":
#         print(firstNumber % secondNumber)
#     elif operation == "**":
#         print(firstNumber ** secondNumber)
#     elif operation == "//":
#         print(firstNumber // secondNumber)
#     elif operation == "/":
#         print(firstNumber / secondNumber)
#     else:
#         print("Invalid operation.")
# except ZeroDivisionError:
#     print("∞")
# except ValueError:
#     print("Invalid number.")

# #Task 2
# try:
#     number = int(input("Enter any number:"))
#     one = number % 10
#     two = number % 100 // 10
#     three = number % 1000 // 100
#     four = number % 10000 // 1000
#     five = number % 100000 // 10000
#     six = number % 1000000 // 100000
#
#     if number / 100000 < 1 or number / 100000 >= 10:
#        print("Your number isn`t six digit.")
#     elif one + two + three == four + five + six:
#         print("Your number is happy.")
#     elif one + two + three != four + five + six:
#         print("Your number is unhappy =(")
#     else:
#         print("Something get wrong...")
# except ValueError:
#     print("Invalid number.")

# print(123321 % 10)
# print(123321 % 100 // 10 )
# print(123321 % 1000 // 100)
# print(123321 % 10000 // 1000)
# print(123321 % 100000 // 10000)
# print(123321 % 1000000 // 100000)

#Task 3
#
# usersnumber = input("Enter a number of month:")
# if usersnumber == "1" or usersnumber == "2" or usersnumber == "12":
#     print("There is Winter!")
# elif usersnumber == "3" or usersnumber == "4" or usersnumber == "5":
#     print("There is Spring!")
# elif usersnumber == "6" or usersnumber == "7" or usersnumber == "8":
#     print("There is Summer!")
# elif usersnumber == "9" or usersnumber == "10" or usersnumber == "11":
#     print("There is Autumn!")
# else:
#     print("Incorrect month =(")
