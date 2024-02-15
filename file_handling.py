file = open("someText.txt")
print(file.read())
file.close()

# read(r) , write(w) , append(a) , create(x)

# CREATE A FILE

# file = open("Text.txt", "x") # a file named Text.txt is created with no content

# WRITE ONTO A FILE
file = open("Text.txt" , "w")
file.write("This is an example of file creation.")
file.close()

file = open("Text.txt" , "w")
file.write("This is overwritten text.")
file.close()

# READ A FILE
file = open("someText.txt" , "r")
print(file.read())
file.close()

# APPEND A FILE
file = open("newText.txt" , "a")
file.write("This is an example of file appending.")
file.close()

file = open("Text.txt" , "a")
file.write("Hello , I'm appending.")
file.close()