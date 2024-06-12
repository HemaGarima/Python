thislist = ["apple" , "banana" , "cherry" , "orange" , "kiwi" , "mango"]
thislist[1] = "blackcurrant"
thislist[1:3] = ["blackcurrant" , "watermelon"]
print(thislist)

thislist = ["apple" , "banana" , "cherry"]
thislist[1:2] = ["blackcurrant" , "watermelon"]
print(thislist)

thislist = ["apple" , "banana" , "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

thislist = ["apple" , "banana" , "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thislist = ["apple" , "banana" , "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple" , "banana" , "cherry"]
tropical = ["mango" , "pineapple" , "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple" , "banana" , "cherry"]
thistuple = ("kiwi" , "orange")
thislist.extend(thistuple)
print(thislist)

# remove() method removes the first occurrence of the specified value.
thislist = ["apple" , "banana" , "cherry"]
thislist.remove("banana")
print(thislist)

# If you don't specify the index , the pop() method removes the last item
thislist = ["apple" , "banana" , "cherry"]
thislist.pop(1)
print(thislist)

# del keyword can also delete the list completely
thislist = ["apple" , "banana" , "cherry"]
del thislist[0]
print(thislist)
thislist = ["apple" , "banana" , "cherry"]
del thislist
# print(thislist) => gives error because list has deleted

# clear() method empties the list
thislist = ["apple" , "banana" , "cherry"]
thislist.clear()
print(thislist)

thislist = ["apple" , "banana" , "cherry"]
for x in thislist:
    print(x)

for i in range(len(thislist)):
    print(thislist[i])

i = 0
while i<len(thislist):
    print(thislist[i])
    i = i+1

print("   ")
[print(x) for x in thislist]

fruits = ["apple" , "banana" , "cherry" , "kiwi" , "mango"]
# newlist = []
# for x in fruits:
#     if "a" in x:
#         newlist.append(x)
# print(newlist)

newlist = [x for x in fruits if "a" in x]
newlist = [x for x in range(10)]
newlist = [x.upper() for x in fruits]
newlist = ['hello' for x in fruits]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)