colors = ["violet" , "indigo" , "blue" , "green"]
colors.sort() # sort in ascending order
print(colors)

num = [4 , 2 , 5 , 3 , 6 , 1, 2 , 1 , 2 , 8 , 9 , 7]
num.sort() # sort in ascending order
print(num)

colors.sort(reverse=True) # sort in descending order
num.sort(reverse=True) # sort in descending order
print(colors)
print(num)

colors = ["voilet" , "indigo" , "blue" , "green"]
colors.reverse()
print(colors)

num = [4 , 2 , 5 , 3 , 6 , 1 , 2 , 1 , 2 , 1 , 8 , 9 , 7]
num.reverse()
print(num)

print(colors.index("green"))
print(num.index(3))

colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.count("green"))
print(num.count(1))

newlist = colors.copy()
print(colors , newlist)