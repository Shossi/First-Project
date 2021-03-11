# 1.What does string slicing mean?
# string1 = "wasabi"
# string1[start:stop:step]
# print(string1[2:1:-1])
# slicing is a method to "play around" with a string,
# you can give parameters where to start the print for example, where to end,
# the steps and work around with it.

# 2.What does string concatenation mean?
# string concat is to add strings together.
# string2 = "sup sup?"
# string3 = "beautiful"
# print(string3 + ', ' + string2)

# 3.what is list comprehension?
# list comp is a different way to create a new list using an existing one.
# without list comp:
# l1 = [1, 2, 3, 4, 5, 6, 7]
# l2 = []
# for num in l1:
#     if num % 2 == 0:
#         l2.append(num)
# print(l2)
# with list comp:
# l2 = [num for num in l1 if num % 2 == 0]
# print(l2)

# 4.what is a dict? when will you use it? why should you use it?
# dictionary is basically a list that has 1 value and 1 key, for each value you add, you also add a key.
# you use it when you have a set unique of keys that you associate to values and you don't care about order.
# you should use it because it stores values like a map,
# which unlike other Data Types that hold only single value as an element.

# 5.what types can a key be in a dict? value?
# key can be either int, float ,string or bool
# a value can be any type.
# dict1 = {
#     2.2: "hamshlock"
# }
# print(dict1.get(2.2))

# 7. what format is dict written in? json or xml?
# it was xml in the past and changed to json around the year 2000

# 8.how to [create, add, overwrite, delete] an item on a dict?
#
# dict1 = {  # create
#     "a": 1,
#     "b": 2,
#     "c": 3
# }
# dict1.pop("c")  # remove
# dict1["d"] = 4  # add
# dict1['a'] = 11  # rewrite
#
# print(dict1)

# 9. how can you get all keys from a dict?
# for key in dict1.keys():
#     print(key)

# 10.how can you get  all values withing a dict?
# for d, v in dict1.items():
#     print(d, ":", v)
# for value in dict1.values():
#     print(value)

# # 11.list comp:
# str1 = "i love to eat ice cream in the beach"
# l1 = str1.split()
# # print(l1)
# # caps
# l2 = [word.upper() for word in l1]
# print(l2)
# # first letter in every word
# l3 = [word[0] for word in l1]
# print(l3)
# # third letter where possible
# l4 = [word[2] for word in l1 if len(word) > 2]
# print(l4)
# # list of numbers that represent the len of each word
# l5 = [len(word) for word in l1]
# print(l5)

# 12. list of the number 10 in the power of the numbers 1-10
# l1 = [num for num in range(1, 11)]
# # print(l1)
# l2 = [num ** 10 for num in l1]
# print(l2)

# 13. write a function that accepts a key and a dict and returns its value or None respectively
# dict1 = {
#     "a": 1,
#     "b": 2,
#     "h": 8,
#     "d": 4,
#     "e": 5
#
# }
#
#
# def try_get_value(key, dictionary):
#     if key in dictionary.keys():
#         return dictionary[key]
#     else:
#         return None
#
#
# print(try_get_value("a", dict1))
# print(try_get_value("h", dict1))

# 14. def get sorted keys: accepts a dict and returns a sorted list of the keys
#
#
# def get_sorted_keys(dictionary):
#     return sorted(dictionary.keys())
#
#
# print(get_sorted_keys(dict1))

# 15.def merge dict: accepts two dicts and returns a merged one.
# dict2 = {
#     "c": 3,
#     "f": 6,
#     "g": 7,
#     "i": 9
# }
#
# dict3 = dict(dict1, **dict2)  # python 3.5 +
# dict4 = dict1 | dict2  # python 3.9 +
# print(dict3)
# print(dict4)
#
#
# def merge_dict(d1, d2):
#     merged_dict = d1 | d2
#     return merged_dict
#
#
# print(merge_dict(dict1,dict2))

# 16.write a program that accepts two values from the user: name and no.id
# the id will be used as the key and the name as the value
# check if the name is already in the dict if it does rewrite it to the new value provided
# if it doesnt exist already add it normally. repeat this process until the user enters "1"
# when the user is done print all the keys and values in the created dict.
# dict1 = {}
# while True:
#     key = input("please enter an id number:(1 to exit) ")
#     if key == "1":
#         break
#     value = input("Please enter a name: ")
#     dict1[key] = value
# print(dict1.items())
