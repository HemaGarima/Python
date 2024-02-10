str1 = "AbcDEfghIJ"
print(str1.upper()) # it converts the string to uppercase
print(str1.lower()) # it converts the string to lowercase

str2 = "   Silver   Spoon        "
print(str2.strip()) # it removes white spaces

str3 = "Hello !!!"
print(str3.rstrip("!")) # it removes any trailing characters

str2 = "Silver Spoon"
print(str2.replace("Sp" , "M"))
print(str2.split(" ")) # splits the string at whitespace " "

str1 = "hello"
capStr1 = str1.capitalize()
print(capStr1)
str2 = "hello WorlD"
capStr2 = str2.capitalize() # it makes the first character of string capitalize
print(capStr2)

str1 = "Welcome to the Console!!!"
print(str1.center(50 , "-")) 

str2 = "Avracadabra"
countStr = str2.count("a")
print(countStr)

print(str1.endswith("!!!")) # returns true or false
print(str1.endswith("to" , 4 , 10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("is")) # it returns the index of the first occrence , if not finds given value then it returns -1
print(str1.find("Daniel"))

print(str1.index("Dan")) # it raises an exception when given value is absent where find returns -1
# print(str1.index("Daniel"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum()) # if value is alpha ie A-Z or a-z and numeric ie 0-9 then it returns true else it returns false
str1 = "Welcome To The Console"
print(str1.isalnum())
str2 = "Hurray!!!!"
print(str2.isalnum())

str1 = "Welcome"
print(str1.isalpha()) # it returns true if value has alpha characters else it returns false

str1 = "I'm 18 years old"
print(str1.isalpha())
print(str2.isalnum())

str1 = "hello world"
print(str1.islower()) # it returns true if all characters are in lowercase else it is uppercase

str1 = "We wish you a Merry Christmas"
print(str1.isprintable()) # it returns true if all the characters in the given string are printable else it returns false

str2 = "Hello , \t\t.Mike"
print(str2.isprintable())

str1 = "          "
print(str1.isspace()) # it returns true only and only if the string contains only white spaces else it returns false
str2 = "        "
print(str2.isspace())

str1 = "Hello World"
print(str1.isspace())

str1 = "World Health Organization"
print(str1.istitle()) # it returns true only if the first letter of each word of the string is capitalized , else it returns false

str2 = "To Kill a Mocking bird"
print(str2.istitle())

str1 = "WORLD HEALTH ORGANIZATION"
print(str1.isupper())
str2 = "To kill a Mocking bird"
print(str2.isupper())

str1 = "Python is a Compiled Language."
print(str1.replace("Compiled" , "Interpreted"))

print(str1.startswith("Python"))
print(str1.startswith("a"))
str1 = "Python is a Interpreted Language"
print(str1.startswith("Inter", 12 , 20))

str1 = "Python is a Interpreted Language"
print(str1.swapcase()) # it swaps the casing character of string ie it converts lower case characters to upper case and vice versa

str1 = "He's name is Dan . Dan is an honest man."
print(str1.title())