# Applying a function to each item in a list
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4]
squared_numbers = list(map(square, numbers))
print(squared_numbers)
# output: [1, 4, 9, 16]
'''
This code defines a function named square that calculates the square of a number. 
Then, it creates a list of numbers [1, 2, 3, 4]. Using the map() function, it applies the square function to each item in the list,
resulting in a new list squared_numbers containing the squares of the original numbers. 
Finally, it prints the list of squared numbers.
'''

# Calculate cube:
def cube(x):
    return x ** 3

numbers = [1, 2, 3, 4]
cubed_numbers = list(map(cube, numbers))
print(cubed_numbers)
# Output: [1, 8, 27, 64]
'''
def cube(x): This line defines a function named cube that takes one argument x and returns the cube of x.

numbers = [1, 2, 3, 4]: This line creates a list named numbers containing the numbers [1, 2, 3, 4].

cubed_numbers = list(map(cube, numbers)): The map() function applies the cube function to each item in the list numbers. 
It returns an iterator containing the results, which are the cubes of the numbers in numbers. 
The list() function is then used to convert this iterator into a list, resulting in a list of cubed numbers stored in cubed_numbers.

print(cubed_numbers): A list of cubed numbers is printed.
'''

# Convert strings to uppercase:
strings = ['this', 'is', 'easy', 'right?!']
uppercase_strings = list(map(str.upper, strings))
print(uppercase_strings)
# Output: ['THIS', 'IS', 'EASY', 'RIGHT?!']
'''
strings = ['this', 'is', 'easy', 'right?!']: Creates a list named strings containing four strings: 'this', 'is', 'easy', and 'right?!'.

uppercase_strings = list(map(str.upper, strings)): 
map() function applies the str.upper function to each string in the list strings. 
str.upper function is a built-in method of string objects that converts a string to uppercase letters. It returns an iterator containing the results, which are the uppercase versions of the strings in strings. The list() function is then used to convert this iterator into a list, resulting in a list of uppercase strings stored in uppercase_strings.

print(uppercase_strings): A list of uppercase strings is printed.
'''

# Calculate length of strings:
strings = ['first', 'second', 'third']
string_lengths = list(map(len, strings))
print(string_lengths)
# Output: [5, 5, 5]
'''
strings = ['first', 'second', 'third']: Creates a list named strings containing three strings: 'first', 'second', and 'third'.

string_lengths = list(map(len, strings)): 
map() function applies the built-in len() function to each string in the list strings. 
The len() function returns the length of a string. 
Returns an iterator containing the results, which are the lengths of the strings in strings. 
The list() function is then used to convert this iterator into a list, resulting in a list of string lengths stored in string_lengths.

print(string_lengths): A list of string lengths is printed.
'''


# Convert strings to integers:
strings = ['1', '2', '3', '4', '5']
integers = list(map(int, strings))
print(integers)
# Output: [1, 2, 3, 4, 5]
'''
strings = ['1', '2', '3', '4', '5']: A list named strings containing five strings: '1', '2', '3', '4', and '5'.

integers = list(map(int, strings)): 
The map() function applies the built-in int() function to each string in the list strings. 
The int() function converts a string representation of an integer to an actual integer. 
Returns an iterator containing the results, which are the integers corresponding to the strings in strings. 
list() function is then used to convert this iterator into a list, resulting in a list of integers stored in integers.

print(integers): A list of integers is printed.
'''


# Check if numbers are even:
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5]
even_flags = list(map(is_even, numbers))
print(even_flags)
# Output: [False, True, False, True, False]
'''
def is_even(x):: This line defines a function named is_even that takes one argument x and returns True if x is even (i.e., divisible by 2) and False otherwise.

numbers = [1, 2, 3, 4, 5]: This line creates a list named numbers containing five integers: 1, 2, 3, 4, and 5.

even_flags = list(map(is_even, numbers)): The map() function applies the is_even function to each number in the list numbers. 
\It returns an iterator containing the results, which are boolean values indicating whether each number is even or not. 
The list() function is then used to convert this iterator into a list, resulting in a list of boolean values stored in even_flags.

print(even_flags): Finally, the list of boolean values indicating whether each number is even or not is printed.
'''
