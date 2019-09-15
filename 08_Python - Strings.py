#Creating String with single Quotes
String1 = 'Welcome to Python Programming with NOTTECH'
print('String with the use of Single Quotes : ')
print(String1)

#With Double Quotes
String1 = "I\'m coding"
print('\nString with the use of Double Quotes : ')
print(String1)

#With Triple Quotes
String1 = '''I\'m coding using Python and using my "Laptop"'''
print('\nString with the use of Triple Quotes : ')
print(String1)

#With Multiple Lines
String1 = '''Python
				For
					Programming'''
print('\nCreating a multiple String')
print(String1)

print('\n')


#################### Accessing characters in Python ##############################

# Python Program to Access characters of String
String1 = 'Python For Programming'
print('Initial String : ')
print(String1)

# Print First Character
print('\nFirst character of String is : ')
print(String1[0])

# Print Last Character
print('\nLast character of String is : ')
print(String1[-1])

# Print 3rd to 12th Character
print('\nSlicing characters from 3-12 : ')
print(String1[3:12])

# Print Characters btn 3rd and 2nd Last Character
print('\nSlicing characters btn ' + '3rd and 2nd last character')
print(String1[3:-2])

#################### Deleting/Updating from a String ##############################
String1 = 'Hello, I\'m a Programmer'
print('\nInitial String : ')
print(String1)

#Updating a character to a string
#String1[2] = 'p'
#print('\nUpdating character at 2nd Index : ')
#print(String1)

#Updating Entire String
String1 = 'Hello, I\'m a Programmer'
print('\nInitial String : ')
print(String1)

#Updating a String
String1 = 'Welcome to the Programming World'
print('Updated String : ')
print(String1)

print('\n')

#Deletion of a character
#String1 = 'Hello'
#print('Initial String : ')
#print(String1)

#Deleting a character of the String
#del String1[2]
#print('\nDeleting character at 2nd Index : ')
#print(String1)

#Deleting Entire String
#String1 = 'Hello, I\'m a Programmer'
#print('Initial String : ')
#print(String1)

#Delete with the use of del
#del String1
#print('\nDeleting entire String : ')
#print(String1)

#Escape Sequencing in Python
#Initial String
String1 = '''I\'m a "Programmer"'''
print('Initial String with the use of Triple Quotes')
print(String1)

#Escaping Single Quote
String1 = 'I\'m a "Programmer"'
print("\nEscaping Single Quote: ")
print(String1)

#Escaping Double Quotes
String1 = "I\'m a \"Programmer\""
print("\nEscaping Double Quotes: ") 
print(String1)

#Using Escape Sequences To Print Paths
String1 = "C:\\Python\\Programmer\\"
print("\nEscaping Backslashes: ")
print(String1)

print('\n')

##################Formatting of Strings 
#Default Order
String1 = "{} {} {}".format('Python', 'For', 'Programming')
print('Print String in default order : ')
print(String1)

#Positional Formatting
String1 = "{1} {0} {2}".format('Python', 'For', 'Programming')
print("\nPrint String in Positional order: ")
print(String1)

# Keyword Formatting
String1 = '{p} {f} {c}'.format(p = 'Python', f = 'For', c ='Programming')
print("\nPrint String in order of Keywords: ")
print(String1)

# Formatting of Integers
String1 = "{0:b}".format(16) 
print("\nBinary representation of 16 is ") 
print(String1)

# Formatting of Floats 
String1 = "{0:e}".format(165.6458) 
print("\nExponent representation of 165.6458 is ") 
print(String1)

print('\n')

#Old formatting
Integer1 = 12.3456789
print("Formatting in 3.2f format: ") 
print('The value of Integer1 is %3.2f' %Integer1) 
print("\nFormatting in 3.4f format: ") 
print('The value of Integer1 is %3.4f' %Integer1) 


































