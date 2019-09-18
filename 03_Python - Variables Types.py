# Python Numbers

num1 = 10
num2 = 20

print num1+num2

a = 27
b = 3.245879
c = 0xDEFABCECBDAECBFBAEl

print a, b, c

# Python Strings
fname, lname = 'Amani', 'Lecktony'

print fname[0]
print fname[2:]
print lname
print lname[3:6]
print 'My name is ' + fname, lname + ' and I\'m working with NOTTECH LAB.' 

# Python Lists
list1 = [12, 35, 46, 50, 'Wikedzi', 3.147]
list2 = ['I am ', fname]
list3 = [' and I\'m with NOTTECH LAB']

print list1
print list1[4]
print list2 + list3

# Creating a List
List = []
print('\nInitial blank List: ')
print(List)

# Creating a List with the use of a String
List = ['NOTTECH LAB']
print('\nList with the use of String: ')
print(List)

# Creating a List with the use of multiple values
List = ['NOTTECH', 'LAB']
print('\nList containing multiple values: ')
print(List[0])
print(List[1])

# Creating a Multi-Dimensional List (By Nesting a list inside a List)
List = [['NOTTECH'], ['LAB']]
print('\nMulti-Dimensional List: ')
print(List)

# Creating a List with the use of Numbers (Having duplicate values)
List = [1, 2, 3, 3, 3, 6, 8, 9, 9]
print('\nList with the use of Numbers: ')
print(List)

# Creating a List with mixed type of values (Having numbers and strings)
List = [1, 3, 'Python', 8, 'JavaScript', 4, 'ReactJS']
print('\nList with mixed values: ')
print(List)

# Python Tuples
tuple1 = (1, 2, 3, 4)
tuple2 = ('Python is so interesting at the beginning')
tuple3 = (12)

print tuple1
print tuple2
# print tuple1 + tuple3

# Python Dictionary
dictionary = {}
dictionary['value_one'] = 'Associative Array'
# student_marks[] = 

# Python Data Conversion
s = '10010'

# print string converting to int base 2
c = int(s,2)
print ("\nAfter converting to integer base 2 : ") 
print(c)

# printing string converting to float
e = float(s)
print ('\nAfter converting to float : ')
print(e)

print('\nGoodbye!!!')









