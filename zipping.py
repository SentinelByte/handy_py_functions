# Zipping together iterables
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print(list(zipped))

'''
# list1 = [1, 2, 3]: This line creates a list named list1 containing three integer elements: 1, 2, and 3.

# list2 = ['a', 'b', 'c']: This line creates another list named list2 containing three string elements: 'a', 'b', and 'c'.

# zipped = zip(list1, list2): Here, the zip() function takes two iterables (list1 and list2) and zips them together into tuples containing corresponding elements. 
# In this case, it pairs the first element of list1 with the first element of list2, the second element of list1 with the second element of list2, and so on. 
# The result is an iterator of tuples.

# print(list(zipped)): Finally, the zipped iterator is converted to a list using the list() function and printed. 
# This prints a list of tuples where each tuple contains one element from list1 paired with one element from list2.
'''
