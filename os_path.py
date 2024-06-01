import os

# Prompt for components of the file path (folders, etc,)
folder = input("Enter the folder name: ")
subfolder = input("Enter the subfolder name: ")
filename = input("Enter the filename: ")

# Constructing file paths ising os.path.join method
path = os.path.join(folder, subfolder, filename)
print("File path:", path)
