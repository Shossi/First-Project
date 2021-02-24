# **split**
# x = 'baby3no3money'
# y = x.split('3', 1)
# print(y)
# **input**
# player_input = input("please enter your number of choice(1-10): ")
# player_input = int(player_input)
# x = 2.5
# player_input = int(float(player_input))
# print(player_input)
# **format**
# x = 2
# y = "dylan"
# print(f'the number in the variable "x" is: {x}')
# print('the number in the variable "x" is: {1:^3} and not {0:_>6}'.format(y, x))
# print('the number in the variable "x" is: {1:3} and not {0:.2}'.format(y, x))
# ** in **
# x = [6, 2, 1, 0]
# y = 3
# if y in x:
#     print("the number 3 is in the given list")
# else:
#     print("you're a dumb ass")
# **else and elif**
# x = [6, 2, 1, 0]
# z = [1, 2, 6, 4, 5]
# y = 3
# if y in x:
#     print(f"the number {y} is in the given list:{x}")
# elif y in z:
#     print(f"the number {y} is in the given list:{z}")
# else:
#     print("you're a dumb-ass")
# **how does python know if the line of code belong to the if command**
# after calling an if command you start each life with 4 spaces, which separates the rest of the code
# from the code that is related to the if command
# **write a python script that accepts two numbers and print the bigger one out them.**
# x, y = 1, 2
# if x > y:
#     print(f'the bigger number is {x}')
# else:
#     print(f"the bigger number is {y}")
# **write a python script that takes 3 numbers and prints the biggest one.**
# x, y, z = 1123, 9022, 903
# if x > y and x > z:
#     print(f'the biggest number is {x}')
# elif y > z and y > x:
#     print(f'the biggest number is {y}')
# else:
#     print(f'the biggest number is {z}')
# **write a python script that checks if an addition equation is correct
# print("you will need to provide the script with 3 numbers which create an addition equation,"
#       "it does not have to be correct, its the scripts job to check if it is.")
# first = int(input("first number: "))
# second = int(input("second number: "))
# x = int(input("sum of both of them: "))
# sum1 = first + second
# if first + second == x:
#     print(f"correct! :the sum of both numbers is {x}")
# else:
#     print(f"False, this is not the correct sum, the correct one is: {sum1}")
# **in addition to the last task, write a script that can check multiplication, subtraction, addition and division
# print("you will need to provide the script with 3 numbers which create an equation,"
#       "it does not have to be correct, its the scripts job to check if it is.")
# print("you will also need to provide the script with the mathematical sign intended to be used in the equation ")
# first = int(input("first number: "))
# second = int(input("second number: "))
# sign = input("mathematical sign(+, -, /, *: ")
# answer = int(input("chosen answer: "))
#
# if sign == "+":
#     if first + second == answer:
#         print(f"correct! :the sum of both numbers is {answer}")
#     else:
#         x = first + second
#         print(f"False, {answer} is not the correct answer.the correct answer is: {x}")
# if sign == "-":
#     if first - second == answer:
#         print(f"correct! :the sum of both numbers is {answer}")
#     else:
#         x = first - second
#         print(f"False, {answer} is not the correct answer.the correct answer is: {x}")
# if sign == "*":
#     if first * second == answer:
#         print(f"correct! :the sum of both numbers is {answer}")
#     else:
#         x = first * second
#         print(f"False, {answer} is not the correct answer.the correct answer is: {x}")
# if sign == "/":
#     if first / second == answer:
#         print(f"correct! :the sum of both numbers is {answer}")
#     else:
#         x = first / second
#         print(f"False, {answer} is not the correct answer.the correct answer is: {x}")
# ** another solution: accept an entire equation **
equation = input("please input your equation: (1 + 2 = 3)")
equation = equation.split()
# print(equation)
number1 = equation[0]
sign = equation[1]
number2 = equation[2]
answer = equation[4]
if sign == '+':
    if number1 + number2 == answer:
        print("TRUE")
    else:
        print("FALSE")
elif sign == '-':
    if number1 - number2 == answer:
        print("TRUE")
    else:
        print("FALSE")
elif sign == '/':
    if number1 / number2 == answer:
        print("TRUE")
    else:
        print("FALSE")
elif sign == '*':
    if number1 * number2 == answer:
        print("TRUE")
    else:
        print("FALSE")

