## creating list 
import random
names= ['sanip','bibek','deepak']

##add item to list
names.append('ananta')
names.append('auman')

for name in names:
    print(name)

##Remove last item from lis 
# names.pop()

names.sort()
# print(names)

print(random.choice(names))

names2=names
print(names2)
