str4 = "Captain"
str5 = "America"
str6 = str4 + " " + str5 # concatenation of strings
print(str6)

name = "Guzman"
age = 18
# print("My name is " + name + " and my age is " + age) # this gives an error saying that we can concatenate only strings and can't concatenate string to other data types

statement = "My name is {} and my age is {}"
print(statement.format(name , age))

quantity = 2
fruit = "Apples"
cost = 130.0
statement = "I want to buy {2} dozen {0} for {1}$"
print(statement.format(fruit , cost , quantity))
