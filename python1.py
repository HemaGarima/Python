# print("Hello World!!")

# for i in range(5):
#     print(i)

# icecream = "Vanilla"
# def foods():
#     vegetable = "Potato"
#     fruit = "Lichi"
#     print(vegetable + " is a local variable value.")
#     print(icecream + " is a global variable value.")
#     print(fruit + " is a local variable value.")

# foods()


icecream = "Vanilla"
def foods():
    vegetable = "Potato"
    fruit = "Lichi"
    print(vegetable + " is a local variable value.")
    
foods()
print(icecream + " is a global variable value.")
# print(fruit + " is a local variable value.") # fruit is a local variable for function foods so this is not defined here.