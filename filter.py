# Filtering elements from a list
# In this I choose to see if a number is even or odd.

# Filtering elements from a list
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(is_even, numbers))
for num in numbers:
    if num in even_numbers:
        print(f'[Even>] {num}')
    else:
        print(f'[Odd>] {num}')
