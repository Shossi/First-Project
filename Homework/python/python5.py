# 1.What is a function?
# its a block of code, which needs to be called in order to run.

# 2.How do you define and call a function?
# def amaz():  -- define the function
#   print("amaz is amazing")
# amaz()  -- call the funtion

# 3: How do you add parameters to a function? why would you add parameters?
# how can you give a default value to the parameters? what is the rule when giving a default value? (alignment)
# def sqr(number):
#     x = number * number / number ** 2
#     print(x)
#
#
# sqr(6):
# prints 36
# you add parameters to a function to make it so the function can be run on various occasions in the script and not
# just once, if it runs just once there's no reason to make it a function in the first place.
# default values  --  def sqr(number = 3):
# rule when giving a default value is - the name of the parameter is always to the left (parameter = x)

# 4: How do you assign a value to a specific parameter when calling a function?
# def printSum(a=0, b=0):
#     print(a+b)
#
#
# printSum(a=6)

# 5: How does a function return a value
# def printSum(a=0, b=0):
#     return a + b
#
#
# x = printSum(a=6)
# print(x)

# 6: What is the meaning of "pass" in python? When do you use this in functions?
# pass is a command in python that is used as a placeholder.
# You use it when you write a function and don't want to fill yet, doing so lets the code be complied normally and does
# not show a mistake as an empty function will.

# 7: How do you generate a random number? what library will you use? how do you call said library?
# a random number can be generated using the random library in python.
# import random
# print(random.randint(1, 7))

# 8: Write a function that accepts a radius of a circle and returns the perimeter
# def perimeter(radius):
#     return 3.14 * radius * 2

# 9: Write div, mul, sub and add functions that accept 2 parameters x and y.
# then add user input and default values of 0
# def add(x=0, y=0):
#     print(f'addition: {x + y}')
#     return x+y
#
#
# def sub(x=0, y=0):
#     print(f'subtraction: {x - y}')
#     return x-y
#
#
# def mul(x=0, y=0):
#     print(f'multiplication: {x * y}')
#     return x*y
#
#
# def div(x=0, y=0):
#     print(f'division: {x / y}')
#     return x/y
#
#
# num1, num2 = [int(num) for num in input("Enter two numbers please: ").split()]
# add(num1, num2)
# sub(num1, num2)
# mul(num1, num2)
# div(num1, num2)

# 10: Write a function named getInRange that accepts two parameters (min, max)
# the function should ask the user for a number until the number will between the min and the max
# when the users sends a legal response the function returns the number the user sent using return
# def getInRange(min1, max2):
#     while True:
#         x = int(input("Please enter a number: "))
#         if min1 < x < max2:
#             return x
#
#
# # getInRange(10, 100)
# print(getInRange(10, 100))

# 11: Write a function that accepts 3 numbers and returns the smallest one.
# def smallest(a, b, c):
#     if a < b and a < c:
#         return a
#     elif b < a and b < c:
#         return b
#     else:
#         return c
#
#
# print(smallest(10, 20, 3))






























