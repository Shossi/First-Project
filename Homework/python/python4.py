# 1: when should you use the range function in a for loop?
# you should use the range function in a loop when you want to use jumps,
# when you want the for loop to go through the middle or a specific location in a list,
# or in the making of a long list of numbers.

# 2: how do you write a range function with steps? how do you write a range function in a descending order?
# range(start,stop,step)
# range(start,stop,step=-1) descending

# 3:make a list using the range function
# l1 = []
# for n in range(1,11):
#     l1.append(n)
#     print(l1)

# 4:why do need while and do-while loops?
# you need these kind of loops to reach a condition you want

# 5: what is the difference between while and do-while loops
# While loop is executed only when given condition is true.
# do-while loop is executed for first time without any condition.
# After executing the while loop once, the condition is checked.

# 6: how do you use do-while in python?
# l1 = []
# for num in range(100):
#     l1.append(num)
# # print(l1)
# sum1 = 0
# while True:
#     for num in l1:
#         sum1 += num
#         print(sum1)
#         if sum1 > 123:
#             break
#     if sum1 > 123:
#        break

# 7:what is the difference between break and continue? when should you use continue
# continue is used to skip the rest of the code in a loop.
# break is used to terminate the loop it is in.

# 8:write a program that prints all the integers between 200 to 2 in a descending order
# for num in range(200, 1, -1):
#     print(num)

# 9:write a program that prints all Multiples of 7 between 1 to 100
# for num in range(7, 100, 7):
#     print(num)

# 10:write a program that accepts and prints numbers until a negative number is sent
# l1 = [1, 2, 3, 4, 5, 6, 7, 8, -2]
# sum1 = 0
# for num in l1:
#     if num < 0 == True:
#         break
#     sum1 += num
# print(sum1)

# 11:write a program that accepts a number and prints its factorial
# num1 = int(input("Please select a number(int): "))
# if num1 == 1 or 0:
#     print(1)
# else:
#     fact = 1
#     for num in range(1, num1+1):
#         fact *= num
#         print(fact)

# 12: make a program that chooses 5 numbers out of a list (2-49), and the user needs to guess the numbers.
# when he guesses a correct one, remove that number from the list and continue until every number has been guessed
# if the users guesses a number outside the range continue(continue) to the next iteration
# at the end print how many guesses the user needed to guess all of the numbers
# if the user choooses

from random import seed
from random import choice
seed(1)
numbers = []
correct = []
guesses = []
num_guesses = 0
l2 = [i for i in range(2, 50)]
# for xd in range(5):
#     d = choice(l2)
#     l2.remove(d)
#     numbers.append(d)
for x in range(5):
    numbers.append(choice(l2))
# print(numbers)

while len(numbers) > 0:
    if num_guesses > 20:  # resetting
        num_guesses = 0
        numbers = []
        correct = []
        guesses = []
        # for xd in range(5):
        #     d = choice(l2)
        #     l2.remove(d)
        #     numbers.append(d)
        for x in range(5):
            numbers.append(choice(l2))
        print("you've used up all of your guesses, restarting!")
        continue

    guess = input("please enter you guess ('q' to quit): ")
    if guess.upper() == 'Q':
        break

    if int(guess) not in range(2, 50):
        print(f"this number isn't valid!")
        continue

    num_guesses += 1
    guesses.append(guess)

    if int(guess) in numbers:
        print(f"correct! {guess} is one of the 5 random numbers!")
        numbers.remove(int(guess))
        correct.append(guess)
        remaining_numbers = len(numbers)
        print(f'remaining numbers to guess: {remaining_numbers}')
        print(f'current number of guesses used: {num_guesses}')

    if guesses.count(guess) > 1:
        print("you can't guess the same number twice :( ")
        break

    if len(correct) == 5:
        print(f"congratulations you've done it! it took you {num_guesses} guesses this time")
        play_again = input("play again? (y/n): ")
        if play_again.upper() == "Y":
            num_guesses = 0
            numbers = []
            correct = []
            guesses = []
            for x in range(5):
                numbers.append(choice(l2))
            # for xd in range(5):
            #     d = choice(l2)
            #     l2.remove(d)
            #     numbers.append(d)
            continue
        else:
            break






