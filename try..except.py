# try....except blocks are used in python to handle errors and exceptions. The code in try block runs when there is no error. If the try block catches the error , then the except block is executed.

# try:
#     num = int(input("Enter an integer : "))
# except ValueError:
#     print("Number entered is not an integer.")

# The code in else block is executed when there is no error in try block.

# try:
#     num = int(input("Enter an integer : "))
# except ValueError:
#     print("Number entered is not an integer.")
# else:
#     print("Integer Accepted.")

# The finally block is executed whatever is the outcome of try...except..else blocks.

try:
    num = int(input("Enter an integer : "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")