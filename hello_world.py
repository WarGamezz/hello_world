# This is my introduction to programming. I have no previous programming experience.
# Created using multiple sources including: tutorialspoint.com; python-course.eu; w3schools.com; Corey Schafer's YouTube tutorial. I do not mean to infringe any copyright laws, this file was compiled to put all of the knowledge required in one place. If there's any issue with the copyrights, please message me and I will delete requested data immediately.
# Using Visual Studio Code on Windows machine, using better comments extension for better visuals
# Word wrap is set.
# Git https://github.com/WarGamezz/hello_world

#from docs.python.org
#Print objects to the text stream file, separated by sep and followed by end. sep, end, file and flush, if present, must be given as keyword arguments.

#All non-keyword arguments are converted to strings like str() does and written to the stream, separated by sep and followed by end. Both sep and end must be strings; they can also be None, which means to use the default values. If no objects are given, print() will just write end.

#The file argument must be an object with a write(string) method; if it is not present or None, sys.stdout will be used. Since printed arguments are converted to text strings, print() cannot be used with binary mode file objects. For these, use file.write(...) instead.

#Whether output is buffered is usually determined by file, but if the flush keyword argument is true, the stream is forcibly flushed.

#? print syntax
# print(object(s), separator=separator, end=end, file=file, flush=flush)
# "separator" - Specify how to separate the objects, if there is more than one. Default is ' '
print("Hello", "how are you?", sep=" --- ")
# "end" - Specify what to print at the end. Default is '\n' (line feed)
print("Hello", "how are you?", end = " **************** ")
# file An object with a write method. Default is sys.stdout (output to screen), but file=open('file.txt', 'w')) can be use to write to file
print('Hello', 'World', 2+3, file=open('file.txt', 'w'))


print('Hello world. This works') #single quoatation works, you can use it if you want to use double quotation in the string without escaping anything
print("Hello world. This also works.") #double quoatation works, you can use it if you want to use single quotation in the string without escaping anything
print("""Printing over multiple lines 
requires triple quotation
and it works and works and works""") #triple quotation (whether single or double) allows you to wrinte strings over multiple lines
string1 = "Hello "
string2 = "world"
print(string1 + string2) #you can simply add strings together by using + signs in between
print(len(string1)) # you can figure out the length of the string using len(string)

#! Slice
string1 = "Hello World"
#Return a slice object representing the set of indices specified by range(start, stop, step)
#The slicing operator [] is actually being used in the above code with a slice() object using the : notation (which is only valid within []), i.e.:
#a[start:stop:step] is equivalent to a[slice(start, stop, step)]
print(string1[0:3]) # you can access individual index or range of indexes. First index is inclusive, second one is not. 
print(string1[2]) #here we acces 3 character (3rd index)
print(string1[::2]) #print from the first index to the last, every other character
#step might be a negative number for example
print(string1[::-1])    # all items in the array, reversed
print(string1[1::-1])   # the first two items, reversed
print(string1[:-3:-1])  # the last two items, reversed
print(string1[-3::-1])  # everything except the last two items, reversed

#! String methods
string1 = "thIs Is the soNg that neVer enDs"
#str.capitalize Return a copy of the string with its first character capitalized and the rest lowercased.
print(string1.capitalize())
#str.count Return the number of non-overlapping occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation.
print(string1.count("e")) # letter e shows up for time
#endswith Return True if the string ends with the specified suffix, otherwise return False. (don't have good example yet)
#str.expandtabs Return a copy of the string where all tab characters are replaced by one or more spaces, depending on the current column and the given tab size.
print('01\t012\t0123\t01234'.expandtabs())
print('01\t012\t0123\t01234')
#str.find Return the lowest index in the string where substring sub is found within the slice s[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.
print('Tell me where is the first l in this string'.find('l')) #using index
#The find() method should be used only if you need to know the position of sub. To check if sub is a substring or not, use the in operator:
print('first' in 'Tell me where is the first l in this string')
