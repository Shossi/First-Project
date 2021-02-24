# ** When should you use a loop? **
# a loop is used when you want to execute a line, or multiple lines of code, a couple of times.
# ** what is the syntax of a loop in python? **
# there are several types of loops: for while and do-while,
# for loop is written as such:
# for x in list:
# print x
# and break whenever you want to exit the loop
# while loop is written as such:
# while x:
# do something
# and break sometime
# do-while loops are the same as while loops with the addition of condition that stops or alters the loop.
# **print half a list**
# lst = [1, 2, 3, 4, 5, 6]
# half_lst = lst[:len(lst)//2]
# second_half = lst[len(lst)//2:]
# print(half_lst)
# print(second_half)
# **write a loop that prints every variable in a list** + add a break point**
# lst = ["coding of world", "pen", 'python', 'hello']
# for word in lst:
#     word = word.upper()
#     print(word)
#     if len(word) < 4:
#         break
# ** a bunch of list functions **
# name = "yossi shlomov"
# print(name[-5:])  # last 5 letters of the string
# print(name[:len(name)//3])  # first third of the string
# print(name.count('o'))  # count the number of times the letter (o) is in the string
# print("o" in name)  # check if (o) is in the string and return a bool
# lst = name.split()  # divide the string into a list
# # print(lst)
# lst.reverse()  # reverse the order of strings in the list
# # print(lst)
# lst[0] = lst[0].upper()  # change one string to uppercase letters
# # print(lst)
# a = lst[1]
# first_half = a[:len(a)//2]
# # print(first_half)
# second_half = a[len(a)//2 + 1:]
# # print(second_half)
# no_middle = first_half + second_half  # remove the middle letter from the string
# # print(no_middle)
# lst[1] = no_middle
# lst.reverse()
# # print(lst)
# name = ' '.join(lst)  # recreate the string after the changes
# print(name)
# ** string indexing **
# a = "HELLO world!"
# a = a.lower()
# first_o = a.find('o')
# last_o = a.rfind('o')
# print(first_o)
# print(last_o)
# print(a[:first_o])  # print the sentence from the beginning  to the first o
# print(a[last_o:])  # print the sentence from the last o to the end
# print(a.replace('o', ''))  # print the sentence without o's
# ** list of numbers **
# lst = [8, 1000, -3, 2, 5]
# sum1 = 0
# for num in lst:
#     sum1 += num
# # print(sum1)
# # print(sum(lst))
# # print(max(lst))
# # print(min(lst))
# mean = sum(lst) / len(lst)
# # print(mean)
# del lst[len(lst)//2]
# print(lst)
# lst.sort()
# # print(lst)
# # print(lst * 5)
# del lst[0]
# # print(lst)
# a = []
# for num in lst:
#     if num < mean:
#         a.append(num)
# print(a)
# **use a loop to find the biggest number in a list (without using the max function)**
# lst = [1, 5, 7, 8, 100]
# max_num = 0
# for num in lst:
#     if num > max_num:
#         max_num = num
# print(max_num)
# ** same as the last one, but using list of lists and finding the smallest one(without min)**
# list_of_lists = [[4, 8, 200], [4, -3000, -1], [5, -87, 12]]
# min_num = 0
# for lst in list_of_lists:
#     for num in lst:
#         if num < min_num:
#             min_num = num
# print(min_num)
#


