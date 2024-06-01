# Open a file for reading
with open('data.txt', 'r') as file:
    data = file.read()

# Open a file for writing
with open('output.txt', 'w') as file:
    file.write('Hello, World!')
