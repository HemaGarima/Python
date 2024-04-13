import random
print(random.randrange(1,10))

a = "Hello , World!!!"
print(len(a))

txt = "The best things in life are free!!"
print("free" in txt)
if "free" in txt:
    print("Yes, free is present in txt.")
print("expensive" not in txt)


txt = "The best, things in l,ife are free!!"
print(txt.split(","))
print(txt.replace("T","H"))
print(txt.strip()) # removes whitespaces from beginning or end of the string
print(txt.upper())
print(txt.lower())
if "expensive" not in txt:
    print("expensive not in txt")

age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)


txt = "Its\r all right!!"
print("Its \rall right!!")
print(txt)

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

x = 200.0
print(isinstance(x, int))