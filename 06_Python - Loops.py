######################
	#While Loop
######################

#Simple While
count = 0
while (count < 3):
	count = count + 1
	print('Hello Python')

print('\n')

#Using else statement with while loops
count = 0
while (count < 3):
	count = count + 1
	print('Hello Python')
else:
	print('In else block')

print('\n')

#Single statement while block
count = 0
#while (count == 0): print('Hello Python')

print('\n')

######################
	#For Loop
######################
# Iterating over a list
print('List Iteration')
l = ['Python', 'Programming', 'Language']
for i in l:
	print(i)

print('\n')

# Iterating over a tuple (immutable)
print('Tuple Iteration')
t = ('Python', 'Programming', 'Language')
for i in t:
	print(i)

print('\n')

# Iterating over a String
print('String Iteration')
s = 'Python'
for i in s:
	print(i)

print('\n')

# Iterating over dictionary 
print('\nDictionary Iteration')
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
	print('%s %d' %(i, d[i]))

print('\n')

######################
	#Iterating by index of sequences
######################
list = ['Python', 'for', 'Programming']
for index in range(len(list)):
	print list[index]

print('\n')

######################
	#Using else statement with for loops
######################
list = ['Python', 'for', 'Programming']
for index in range(len(list)):
	print list[index]
else:
	print 'Inside Else Block'

print('\n')

######################
	#Nested Loops
######################
from __future__ import print_function
for i in range(1, 5):
	for j in range(i):
		print(i, '\n')
	print()

print('\n')

######################
	#Loop Control Statements
######################
#Continue Statement
for letter in 'PythonforProgramming':
	if letter == 't' or letter == 's':
		continue
	print 'Current Letter : ', letter
	var = 10

print('\n')

#Break Statement
for letter in 'PythonforProgramming':
	if letter == 't' or letter == 's':
		break
print 'Current Letter : ', letter

print('\n')

#Pass Statement
for letter in 'PythonforProgramming':
	pass
print 'Last Letter : ', letter

print('Goodbye')