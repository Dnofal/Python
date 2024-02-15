

names = ['Diaa', 'Lennart', 'Mona', 'Johann' ]

print(names[1]) # Lennart

print(names[-1]) # Johann

print(names[-2]) # Mona

names[0] = 'Nofal'
print(names[0]) # Nofal

print(names[0:4]) # Johann will be not included 

names.insert(0, 'Ahmad') # Insert Ahmat to the begining 
print(names)

names.clear()
print(names)  # clear all

names.append('Diaa') # append diaa  at the end
print(names)

print( 'Diaa' in names)


names.append('Mona')   #Print all
for item in names:
    print(item)

i = 0
while i < len(names): #Print all
    print(names)
    i = i + 1

for num in range(5): # Print 0 - 4 
    print(num)

numbers = (1, 2, 3)  # These are touples and cannot be changed 
print(numbers)






