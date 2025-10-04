# File Modes:
# r - Read
# w - Write
# a - Append
# w+ - Write + Read
# a+ - Append + Read

file = open("my_file.txt") # Default mode for this open() method is r - read
print(file.read())
file.close()

# Using this format we don't have to close the file manually everytime
with open("my_file.txt") as file:
    print(file.read())

with open("my_file.txt", 'w+') as file:
    file.write("Hola Amigo!")
    file.seek(0) # Moving cursor to the start of file
    print(file.read())

with open("my_file.txt", 'a+') as file:
    file.write("\nMi Nemro es Saksham.")
    file.seek(0) # Moving cursor to the start of file
    print(file.read())