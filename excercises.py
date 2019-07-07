# This is my introduction to programming. I have no previous programming experience.
# Created using multiple sources including: tutorialspoint.com; python-course.eu; w3schools.com; Corey Schafer's YouTube tutorial. I do not mean to infringe any copyright laws, this file was compiled to put all of the knowledge required in one place. If there's any issue with the copyrights, please message me and I will delete requested data immediately.
# Using Visual Studio Code on Windows machine, using better comments extension for better visuals
# Word wrap is set.
# Git https://github.com/WarGamezz/hello_world (excercises)
# Excercises taken from w3resource.com/python_excercises

#! Write a Python program to calculate the length of a string

Solution #1

def string_length(test):
    length = 0
    for char in test:
        length += 1
    return length
print('Length of the inputed string = ' + str(string_length(input('Input random string here: '))))

Solution #2 (I think this one is more elegant)
string = input('Input random string here: ')
print('Length of the inputed string = ' + str(len(string)))


#! Write a python program to count the number of the characers (character frequency) in a string
#sample string google.com
#expected result {'o':3, 'g':2, '.':1, 'e':1, 'l':1, 'm':1, 'c':1}

