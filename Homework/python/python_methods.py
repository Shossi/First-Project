# Python coding part:
#
# a) Write a method that receives a string (path of URL), and prints out the content of the URL.
#
# b) Write a method that receives a string (path of file of .csv format), and print only the second value of
# each line to data structure, for example:
# file.csv content:
# 1,hello
# 2,bye
# 3,nice
# You should print only “hello”, “bye”, “nice”.
#
# c) Write a method that receives a string (path of URL) and a string (path of file of .csv format) and prints out only
# the words that appear (exact match) in the content of the URL.
# (Theoretical- What is the runtime? How can we make this more efficient?)
#
# d) Theoretical- Assuming Yossi wants to use the method from part c with multiple URLs,
# what might be the issue here? How can we solve it?
#
#
# Show a working example for part c.
import urllib.request
file_name = "C:/Users/KoJoey/Desktop/test.txt"

def get_url_content(url):
    f = urllib.request.urlopen(url)
    my_file = f.read()
    return my_file


def print_second_value(file):
    f = open(file, "r")
    for line in f:
        li = list(line.split(" "))
        print(li[1])


def check_word_in_url(url, file):
    url_content = get_url_content(url)
    with open(file, "r") as f:
        for line in f:
            for word in line:
                if word in url_content:
                    print(word)












