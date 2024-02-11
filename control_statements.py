# pass , continue and break keywords

i = 1
while(i<5):
    i = i+1
    pass


for j in range(5):
    pass

if ( i == 2):
    pass

for i in range(1 , 10):
    if(i%2 == 0):
        continue
    print(i)

i = 1
while(i<=10):
    i = i+1
    if(i%2 != 0):
        continue
    print(i)

i = 1
while(i<=10):
    i = i+1
    if(i == 5):
        break
    print(i)