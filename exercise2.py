# x = 100
# y = 200
# z = 300
# if x < y and y < z:
#     print("x is less than y and y is less than z")

# number1 = input("Enter a 1st number: ")
# number2 = input("Enter a 2nd number: ")
# operator = input("Enter an operator (+, -, *, /): ")
# if operator == "+":
#     print(int(number1) + int(number2))
# elif operator == "-":
#     print(int(number1) - int(number2))
# elif operator == "*":
#     print(int(number1) * int(number2))
# elif operator == "/":
#     print(int(number1) / int(number2))
# else: 
#     print("Invalid operator")



# try:
#   x = 2 + "help"
#   print(x)
# except TypeError:
#   print("inappropriate type")

# try:
#   x = float("hello")
#   print(x)
# except ValueError:
#   print("wrong value")

number = float(input("Enter a number: "))
print(number) 

number = str(number)
print(number, type(number)) 

print(len(input("Enter a number: ")))