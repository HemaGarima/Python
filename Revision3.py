if(4>5):
    print("yes")
else:
    print("no")

print(bool("Hello"))
print(bool(15))

# Almost any value is evaluated to True.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list,tuple,set, and dictionary are True, except empty ones.

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# if you have an object that is made from a class with a __len__ function that returns 0 or False then the bool type of this object also returns false
class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj))

x = 200
print(isinstance(x,int)) # isintance() function checks if an object is of a certain data type.

'''
OPERATORS IN PYTHON
1. Arithmetic operators
2. Assignment operators
3. Comparison operators
4. Logical operators
5. Identity operators
6. Membership operators
7. Bitwise operators
'''

'''
ARITHMETIC OPERATORS
+ , - , * , / , % , ** -> Exponentiation , // -> floor division
'''

'''
ASSIGNMENT OPERATORS
= , += , -= , /= , *= , %= ,  //= , **= , &= , |= , ^= , >>= , <<= , :=
'''

'''
COMPARISON OPERATORS
== , != , > , < , >= , <=
'''

'''
LOGICAL OPERATORS
and , or , not
'''

'''
IDENTITY OPERATORS
is , is not
'''

'''
MEMBERSHIP OPERATORS
in , not in
'''

'''
BITWISE OPERATORS
& -> and , | -> or , ^ -> XOR , ~ -> NOT , << -> left shift , >> -> right shift
'''

'''
OPERATOR PRECEDENCE
() -> ** -> +x , -x , ~x -> * / // % -> + - -> << >> -> & -> ^ -> | -> == != > >= < <= is is not  in not in -> not -> and -> or
'''

thislist = ["apple" , "banana" , "cherry"]
print(thislist)
# list items are ordered , changeable and allow duplicate values.
print(len(thislist))

# a list can contain different data types
list1 = ["abc" , 34 , True , 40 , "male"]
print(list1)
print(type(list1))

thislist = list(("apple" , "banana" , "cherry"))
print(thislist)

# List is a collection which is ordered and changeable . Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered , unchangeable and unindexed. No duplicate members.
# Dictionary is a collection which is ordered and changeable. No duplicate members.

if "apple" in thislist:
    print("Yes , 'apple' is in the fruits list.")