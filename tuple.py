#STUDY TUPLES

# Tuples are immutable → once created, you cannot change their elements (no append, remove, or direct value change)

# Tuples can store multiple data types → int, str, float, bool, lists, other tuples, etc.

# Tuples support indexing and slicing → you can access elements by index (tuple[0]) and slice them (tuple[1:3])

# Tuples can be used for "unpacking values" → a, b, c = (1, 2, 3), useful for functions returning multiple values

#example:
snacks = ('hamburguer', 'hot dog', 'potatoes') #tuple
print(snacks) #print all items in tuple
print(snacks[0]) #print the first item in snacks
print(snacks[-1]) #print the last item in snacks
print(snacks[0:2]) #print item[x] in tuple to item[y] in tuple
print(snacks[0:]) #print all elements in tuple starting from element [x:]
print(snacks[:2]) #print all elements in tuple and finish in element [:y]

for s in range(0, len(snacks)):
    print(f'{snacks[s]} is delicious! position: {s}') #print tuple with organization
    
for s in snacks:
    print(f'i will eat {s}') #simple print tuple
    
#sum tuples:
age = (10, 25, 35, 12)
height = (1.80, 1.57, 1.70, 1.74)
a_h = age + height
print(a_h)