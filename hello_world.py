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

#! Slicning
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0  1  2  3  4  5  6  7  8  9             positive index
#        -10 -9 -8 -7 -6 -5 -4 -3 -2 -1             negative index
# 
# list[start:end:step] - positive and negative indexes can be mixed and matched

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
#str.capitalize() Return a copy of the string with its first character capitalized and the rest lowercased.
print("caPiTalize thiS sentence".capitalize())

#str.casefold() Convert string into lower case
print('GiVe me Some Lower CasEs'.casefold())

#str.center() Return center string. For example print the word banana taking up the space of 20 chars with banana in the middle
print("Banana".center(30))

#str.count() Return the number of non-overlapping occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation.
print("How many times does the letter e show up in this sentence?".count("e")) # letter e shows up nine times // can also be used to see how many times does string show up in other string.

#str.endswith() - Return True if the string ends with the specified suffix, otherwise return False. 
print("Let's see if this sentence ends up with a punctuation mark at the end.".endswith('.')) #yes it does

#str.expandtabs() Return a copy of the string where all tab characters are replaced by one or more spaces, depending on the current column and the given tab size.
print('01\t012\t0123\t01234'.expandtabs())
print('01\t012\t0123\t01234')

#str.find - Return the lowest index in the string where substring sub is found within the slice s[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.
print('Tell me where is the first l in this string'.find('l')) #using index
#The find() method should be used only if you need to know the position of sub. To check if sub is a substring or not, use the in operator (returns true/false)
print('where' in 'Tell me where is the first l in this string')

#str.format() - Format specified value and insert them inside the string's placeholder. The placeholder is defined using curly brackets: {}.
print("For only {price:.2f} dollars!".format(price = 49)) #in this case format price to be fixed point, two-decimal format
#Here's the actual example of when that'd be usefull. instead of writing print(variable + ' ' + variable2 + ' ' + variable3 ' ' + variable4) we can use formating and variable placeholders:
variable, variable2, variable3, variable4, variable5 = 'Hello', 'darkness', 'my', 'old', 'friend'
print('{} {} {} {}'.format(variable, variable2, variable3, variable4, variable5))

#str.isalnum() - Returns True if all the characters are alphanumeric, meaning alphabet letters (a-z) and numbers (0-9). Not alphanumeric examples: (space)!@#$%^&?
print('Is this string alphanumbeic? I gues not ^_^'.isalnum()) #returns false

#str.isalpha() - Returns True if all the characters are are alphabet letters (a-z)
print('Is this string alphanumbeic? Nope because of the question mark'.isalpha()) #returns false

#str.isdecimal() - Returns True if all characters in the string are decimals
print("3".isdecimal()) #returns true

#str.isidentifier() - Returns True if the string is a valid identifier (only alphanumeric (a-z) and (0-9) or underscores. Valid identifier cannot start with the number or contain any spaces)
print("1_i_AM_not_VALID".isidentifier()) #returns false since it begins with the number

#str.islower() - Returns True if all characters in the string are lower case
print("all sentence in lower cases".islower()) #returns true

#str.isnumeric() - Returns True if all characers in the string are numeric
print("12345six789".isnumeric()) #returns false

#str.isprintable() - Returns True if all characters are printable. Non-printable characters are for example carriage return and line feed
print("Hello! Are you #1?".isprintable())

#str.isspace() - Returns True if all characters in the string are whitespaces.
print("           ".isspace())

#str.istitle() - Returns true if all words in a text start with a upper case letter, AND the rest of the words are lower case letter
print("Hello! Welcome To My Title".istitle())

#str.isupper() - Returns true if all characters in the string are upper case
print("This will not return true since there are some lower case characters".isupper())

#str.join() - Takes all items in iterable and joins them into one string, a string must be specified as a separator. Syntax - string.join(iterable)
list = ('One', 'Two', 'Three') #tuple = sequence of immutable python objets named list with 3 objects named "One", "Two" and "Three"
print("*".join(list)) #join all objects from above tuple into one string using '*' as a separator

#str.ljust() - This method will left aligh the string, using a specified character (space is default) as the fill character. Syntax - string.ljust(length, character)
print("banana".ljust(20, "*")) #banana (6 characters), and another 14 characters of * to fill 20 char void

#str.lower() - Converts string into lower case
print("All of the Upper CasEs go into lower case".lower())

#str.lstrip() - Remove any leading characters (space by default) to the left of the string
print('My favourite fruit is ' + '                     banana'.lstrip()) #default space
print("abcde abcdefg abcdefgh".lstrip("abcdf")) # will remove all first instances of a, b, c, d

#str.partition() - Searches for specified string and splits the string into a tuple containing 3 elements. (1) everything before searched string, (2) searched string, (3) everything past searched string. This method search for the FIRST occurenece of the string.
print('I like to eat bananas and oranges'.partition('bananas'))
print('I like to eat bananas and oranges'.partition('apples')) #if the specified value is not found, method returns a tuple containig (1) the whole string (2) empty string (3) empty string

#str.replace() - Replaces a specified phrase with another specified phrase. Syntax string.replace(oldvalue, new_value, count). Count specifies hoe many occurences you want to replace. Default is all.
print("I like bananas.".replace('bananas', 'apples'))

#str.rfind() - Finds the last occurence of the specified value. Returns index. Returns -1 if calue not found. Almost the same as rindex. Syntax string.rfind(value, beginning - default is 0, end - default is the end of the string)
print('Mi casa, su casa'.rfind('casa')) #last casa starts at 12th index (13 character since index counts from 0)
print('Hello, welcome to my world'.rfind('e', 5, 10)) #where is the last time we see the letter e in range 5-10 = 8 index, 9 letter

#str.rindex - Essentially identical to rfind. However, if the value is not found, the rfind() method returns -1, but the rindex() method will raise an exception
print('Hello, welcome to my world'.rfind('q', 5, 10)) #value not found - returns -1
print('Hello, welcome to my world'.rindex('q', 5, 10)) #value not found - exception (ValueError)

#str.rjust() - Right align the string, using a specified character (space by default), as the fill character
print('banana'.rjust(20, '*')) #exactly 14 * and 6 letters in banana

#str.rpartition() - Searches for specified string and splits the string into a tuple containing 3 elements. (1) everything before searched string, (2) searched string, (3) everything past searched string. This method search for the LAST occurenece of the string.
print('I could eat banans all day, but just only if those bananas are fresh'.rpartition('bananas')) #if the specified value is not found, method returns a tuple containig (1) the whole string (2) empty string (3) empty string

#str.rsplit() - Split a string into a list, starting from the right. If no "max" is specified, this method will return the same as str.split() method. When max is specified, the list will contain a specific number of elements PLUS ONE.
print('comptuter, orange, banana, pencil, paper'.rsplit(', ')) #no max defined so output = str.split(), it will "split" everything into individual elements
print('comptuter, orange, banana, pencil, paper'.rsplit(', ', 1)) #max parameter set to 1, so it will create 2 elements, (1) comptuter, orange, banana, pencil (2) paper
print('comptuter, orange, banana, pencil, paper'.rsplit(', ', 2)) #max parameter set to 2, so it will create 3 elements, (1) comptuter, orange, banana (2) pencil (3) paper
print('comptuter, orange, banana, pencil, paper'.rsplit(', ', 3)) #max parameter set to 3, so it will create 4 elements, (1) comptuter, orange (2) banana (3) pencil (4) paper

#str.rstrip() - Returns a right trim version of the string. Syntax string.rstrip(characters)
print('banana7ujm&UJM7ujm&UJM'.rstrip('7ujm&UJM')) #will strip down all instances of characters 7, u, j, m, &, U, J, M

#str.split() - Splits the string at the specified separator and returns a list. When max is specified the list will contain specified number of elements plus one
print('comptuter, orange, banana, pencil, paper'.split(', ')) #no max defined so output = str.split(), it will "split" everything into individual elements
print('comptuter, orange, banana, pencil, paper'.split(', ', 1)) #max parameter set to 1, so it will create 2 elements, (1) comptuter, (2) orange, banana, pencil, paper
print('comptuter, orange, banana, pencil, paper'.split(', ', 2)) #max parameter set to 2, so it will create 3 elements, (1) comptuter, (2) orange, (3) banana, pencil, paper
print('comptuter, orange, banana, pencil, paper'.split(', ', 3)) #max parameter set to 3, so it will create 4 elements, (1) comptuter, (2) orange, (3) banana, (4) pencil, paper

#str.splitlines() - Splits a string into a list. The splitting is done at the line breaks. Optionally (keeplinebreaks) can be set to true - specifies if line breaks should be included. It's False by default.
print('Split that string here\nand here\nand maybe over here'.splitlines())
print('Split that string here\nand here\nand maybe over here'.splitlines(True))

#str.startswith() - Returns true if string starts with specified value. Possible to limit to start and end. Syntax string.startswith(value, start, end)
print('Hello, welcome to my world'.startswith('He')) #true
print('Hello, welcome to my world'.startswith('we', 7)) #true

#str.strip() - Removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
print("...;rtghbananaoplk9999".strip('.;rtghoplk9'))

#str.swapcase() - Swaps cases, lower case becomes upper case and vice versa
print("UppeR anD Lower Cases swAp".swapcase())

#str.title() - Returns a string where the first character in every word is upper case. Like a header or a title.
print('not at all titled string that will be converted to a title styled string'.title())

#str.upper() - Returns a string where all characters are upper case
print('all lower case string that will be converted to all uper case'.upper())

#str.zfill() - adds zeros (0) at the beginning of the string, until it reaches the specified length. If the value of the len parameter is less than the length of the stringm no filling is done
print('This is the string of few characters'.zfill(50))

#! Operators
#The following tokens are operators
#   +   -   *   **  /   //  %   @   <<  >>  &   |   ^   ~   <   >   <=  >=  ==  !=

#! Delimiters
#The following tokens serve as delimiters in the grammar
# (     )   [   ]   {   }   ,   :   .   ;   @   =   ->   +=     -=   *=     /=    //=    %=   @=     &=      |=      ^=      >>=     <<=      **=  


#! String Formatting
# Some simple format string examples:
# "First, thou shalt count to {0}"  # References first positional argument
# "Bring me a {}"                   # Implicitly references the first positional argument
# "From {} to {}"                   # Same as "From {0} to {1}"
# "My quest is {name}"              # References keyword argument 'name'
# "Weight in tons {0.weight}"       # 'weight' attribute of first positional arg
# "Units destroyed: {players[0]}"   # First element of keyword argument 'players'.
#As of Python 3.6, f-strings are a great new way to format strings. Not only are they more readable, more concise, and less prone to error than other ways of formatting, but they are also faster!

#? printf-style String Formatting
# String objects have one unique built-in operation: the % operator (modulo). This is also known as the string formatting or interpolation operator. Given format % values (where format is a string), % conversion specifications in format are replaced with zero or more elements of values. The syntax goes like that. 'Apple, banana, and %s are the best %s ever!' % ('orange', 'fruits')
print('Apple, banana, and %s are the best %s ever' % ('orange', 'fruits'))
# The more variables/operators is there, the more convoluted the entire thing becomes.

#? str.format String Formatting
# As described above it's the most commonly used way of formatting. Format strings contain “replacement fields” surrounded by curly braces {}. Anything that is not contained in braces is considered literal text, which is copied unchanged to the output. The syntax goes like that str.format(args). For example 'There two types of {}, blue and {}.'.format('flowers', 'yellow')
print('There two types of {}, blue and {}'.format('flowers', 'yellow'))
# You can reference variables in any order by referencing their index:
name = 'Eric'
age = 27
print('Hello {}. you are {}'.format(name, age))
# But if you insert the variable names, you get the added perk of being able to pass objects and then reference parameters and methods in between the braces:
person = {'name': 'Eric', 'age': 27}
print("Hello {name}. You are {age}.".format(name=person['name'], age=person['age']))
# You can allso pass the dictionary in a different way
person = {'name': 'Eric', 'age': 27}
print("Hello {0[name]}. You are {1[age]}.".format(person, person))
# You can also use ** to do this neat trick with dictionaries. If you had the variables you wanted to pass to .format() in a dictionary, then you could just unpack it with .format(**some_dict) and reference the values by key in the string, like this:
person = {'name': 'Eric', 'age': 27}
print("Hello {name}. You are {age}.".format(**person))
# This is actually quite usefull for repeateable values for example (placeholders {positional arguments} are numbered from 0 up):
tag = 'h1'
sentence = 'This is the headline'
print('<{0}>{1}</{0}>'.format(tag, sentence))
# Instead dictionaries you can also use lists:
l = ['Eric', '27']
print('Hello, {0[0]}. Your are {0[1]}.'.format(l))
# You can also pass on key words values directly like so:
print('Hello {name}. You are {age}'.format(name='Eric', age='27'))

#? Formatted string literals
#A formatted string literal or f-string is a string literal that is prefixed with 'f' or 'F'. These strings may contain replacement fields, which are expressions delimited by curly braces {}. While other string literals always have a constant value, formatted strings are really expressions evaluated at run time.
name = 'Eric'
age = 27
print(f'Hello {name}. You are {age}')

#Because f-strings are evaluated at runtime, you can put any and all valid Python expressions in them. This allows you to do some nifty things. Like calling functions:
name = 'Eric'
age = 27
def lowercase (input):
    return input.lower()
print(f'Hello {lowercase(name)}. You are {age}.')
# Or methodes directly
print(f'Hello {name.lower()}, you are {age}.')

# Dictionaries.
# Speaking of quotation marks, watch out when you are working with dictionaries. If you are going to use single quotation marks for the keys of the dictionary, then remember to make sure you’re using double quotation marks for the f-strings containing the keys. This will work:
comedian = {'name': 'Eric Idle', 'age': 74}
print(f"The comedian is {comedian['name']}, aged {comedian['age']}.")
# But this will not
comedian = {'name': 'Eric Idle', 'age': 74}
print(f'The comedian is {comedian['name']}, aged {comedian['age']}.') #single quotation will close out the string.

#Braces
#In order to make a brace appear in your string, you must use double braces. Note that using triple braces will result in there being only single braces in your string. However, you can get more braces to show if you use more than triple braces.
print(f"{{74}}") #shall print {74}
print(f"{{{74}}}") #shall print {74}
print(f"{{{{74}}}}") #shall print {{74}}

#! Format Specification Mini-Language

# The grammar for a replacement field is as follows:

# replacement_field ::=  "{" [field_name] ["!" conversion] [":" format_spec] "}"
# field_name        ::=  arg_name ("." attribute_name | "[" element_index "]")*
# arg_name          ::=  [identifier | integer]
# attribute_name    ::=  identifier
# element_index     ::=  integer | index_string
# index_string      ::=  <any source character except "]"> +
# conversion        ::=  "r" | "s"
# format_spec       ::=  <described in the next section> #https://docs.python.org/2/library/string.html#formatspec

# In less formal terms, the replacement field can start with a field_name that specifies the object whose value is to be formatted and inserted into the output instead of the replacement field. The field_name is optionally followed by a conversion field, which is preceded by an exclamation point '!', and a format_spec, which is preceded by a colon ':'. These specify a non-default format for the replacement value.

#The general form of a standard format specifier is:

# format_spec ::=  [[fill]align][sign][#][0][width][,][.precision][type]
# fill        ::=  <any character>
# align       ::=  "<" | ">" | "=" | "^"
# sign        ::=  "+" | "-" | " "
# width       ::=  integer
# precision   ::=  integer
# type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
# The ',' option signals the use of a comma for a thousands separator.


print("Eric's {} is {:^20}".format('age', 27)) #prints Eric's age is (9 empty spaces) 27 (9 empty spaces) for a total of 20 and centers 27 in the middle
print("Eric's {} is {:>20}".format('age', 27)) #prints Eric's age is (18 empty spaces) 27 to fill up the width
print("Eric's {} is {:.2f}".format('age', 27)) # : - format spec, . - precission, 2 - how many digits should be displayed after the decimal point for a floating point value formatted with 'f', and type f - Displays the number as a fixed-point number. The default precision is 6.
print(("Eric's {} is {:06}".format('age', 27))) #fill up 4 zeros prior to 27 to achieve total padding of 6

#! Showing all methods available to the string
name = 'Eric'
print(dir(name)) #dir function will show all methods available for that string
print(help(str)) #will show you everything about the class string
print(help(str.upper)) #will print help regarding upper method of str class