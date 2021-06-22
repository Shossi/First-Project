# Scope Set files
# 1. write a program that accepts integers from the user until he enters -1.
# At the end of all inputs, print all of the numbers the user entered
# how many numbers were entered(without duplicates) and how many numbers had duplicates.
# l1 = []
# while True:
#     x = input("please enter a number (-1 to quit): ")
#     l1.append(int(x))
#     if int(x) == -1:
#         print(l1)
#         inputted_numbers = len(set(l1))
#         print("The amount of numbers entered, without duplicates: " + str(inputted_numbers))
#         amount_of_dups = 0
#         for num in l1:
#             if l1.count(num) > 1:
#                 l1.remove(num)
#                 amount_of_dups += 1
#         print(f"{amount_of_dups} numbers had duplicates.")
#         break
#     else:
#         continue

# 2. write a program that accepts strings from the user until he enters exit
# every word that the user enters will be written into a txt file, at the end print the file at the end.
# with open("C:/text.TXT", "r+") as f1:
#     while True:
#         x = input("enter a str (exit to quit): ")
#         if x.upper() == "EXIT":
#             f1.seek(0)
#             print(f1.readlines())
#             break
#         else:
#             f1.writelines(x)
#             continue

# 3. write a function that get a file name as a parameter (the file will contain only numbers)
# the function will add the sum of all numbers to the file.
# def add_sum_to_file(file):
#     sum1 = 0
#     with open(file, "r+") as f1:
#         for line in f1.readlines():
#             sum1 += int(line)
#             print(sum1)
#         f1.writelines("\n")
#         f1.writelines(str(sum1))
#
#
# add_sum_to_file("C:/text.TXT")

# 4.write a function that accepts a file name and a word as parameters
# and return True if the file contains the word or False if it isn't.
# def check_word_in_file(file, word):
#     with open (file, "r+") as f1:
#         pass
#














