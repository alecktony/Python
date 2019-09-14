##################
	#Arithmetic Operators
################## Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication and division.
a = 9
b = 4

# Addition of Numbers
add = a + b

# Substraction of Numbers
sub = a - b

# Multiplication of Numbers
mult = a * b

# Division_in_float of Numbers
div = a / b

# Division_in_floor of Numbers
div1 = a // b

# Modulo of both number
mod = a % b

# Printing results
print(add)
print(sub)
print(mult)
print(div)
print(div1)
print(mod)
print('\n')

##################
	#Relational Operators
################## Relational operators compares the values. It either returns True or False according to the condition.
a = 13
b = 33

# a > b is False
print(a > b)

# a < b is True
print(a < b)

# a == b is False
print(a == b)

# a != b is True
print(a != b)

# a >= b is False
print(a >= b)

# a <= b is True
print(a <= b)

print('\n')

##################
	#Logical Operators
################## Logical operators perform Logical AND, Logical OR and Logical NOT operations.
a = True
b = False

# Print a & b is False
print(a and b)

# Print a / b is True
print(a or b)

# Print not b is True
print(not b)

print('\n')

##################
	#Bitwise Operators
################## Bitwise operators acts on bits and performs bit by bit operation.
a = 10
b = 4

# Print bitwise AND operation
print(a & b)

# Print bitwise OR operation
print(a | b)

# Print bitwise NOT operation
print(~a)

# Print bitwise XOR operation
print(a ^ b)

# Print bitwise right shift operation
print(a >> 2)

# Print bitwise left shift operation
print(a << 2)

print('\n')

##################
	#Assignment Operators
##################  Assignment operators are used to assign values to the variables.
a = 1
b = 2
c = 3

print(a)
print(b)
print(c)

print('\n')

##################
	#Identity Operators
################## is and is not are the identity operators both are used to check if two values are located on the same part of the memory. Two variables that are equal does not imply that they are identical.
a1 = 3
b1 = 3
a2 = 'Python'
b2 = 'Python'
a3 = [1, 2, 3]
b3 = [1, 2, 3]

print(a1 is not b1)

print(a2 is b2)

print(a3 is b3) # False b'cos lists are mutable

print('\n')

##################
	#Membership Operators
################## in and not in are the membership operators; used to test whether a value or variable is in a sequence.
x = 'NOTTECH LAB'
y = {3: 'a', 4: 'b'}

print('N' in x)

print('NOTTECH' not in x)

print('nottech' not in x)

print(3 in y)

print('b' in y)

print('\n')






















































































