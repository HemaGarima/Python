# Iterators in python are used to iterate over iterable objects or container datatypes like lists,tuples,dictonaries,sets,etc.

# __iter__() --> to initialize an iterator
# __next__() --> this method returns the next item of the sequence

# USING INBUILT ITERATORS

# string = 'Hello World'
# iterObj = iter(string)

# while True:
#     try:
#         char1 = next(iterObj)
#         print(char1)
#     except StopIteration:
#         break

# CREATING CUSTOM ITERATORS:

class multipleOf4:
    def __iter__(self):
        self.count = 0
        return  self
    
    def __next__(self):
        if self.count <= 24:
            x = self.count
            self.count += 4
            return x
        else:
            raise StopIteration
    
    
obj1 = multipleOf4()
number = iter(obj1)

for x in number:
    print(x)