########################
	#Tuples
#######################
# Creating an empty tuple 
Tuple1 = () 
print("Initial empty Tuple: ") 
print (Tuple1) 

# Creating a Tuple with the use of Strings 
Tuple1 = ('Python', 'For', 'Coding') 
print("\nTuple with the use of String: ") 
print(Tuple1) 

# Creating a Tuple with the use of list 
list1 = [1, 2, 4, 5, 6] 
print("\nTuple using List: ") 
print(tuple(list1)) 

# Creating a Tuple with the use of loop 
Tuple1 = ('Python') 
n = 5
print("\nTuple with a loop") 
for i in range(int(n)): 
    Tuple1 = (Tuple1,) 
    print(Tuple1) 

# Creating a Tuple with the use of built-in function 
Tuple1 = tuple('Python') 
print("\nTuple with the use of function: ") 
print(Tuple1) 

# Creating a Tuple with Mixed Datatypes 
Tuple1 = (5, 'Welcome', 7, 'Coding') 
print("\nTuple with Mixed Datatypes: ") 
print(Tuple1) 

# Creating a Tuple with nested tuples 
Tuple1 = (0, 1, 2, 3) 
Tuple2 = ('python', 'programmers') 
Tuple3 = (Tuple1, Tuple2) 
print("\nTuple with nested tuples: ") 
print(Tuple3) 
  
# Creating a Tuple with repetition 
Tuple1 = ('Coding',) * 3
print("\nTuple with repetition: ") 
print(Tuple1) 

print('\n')

#######################Concatenation of Tuples
# Concatenaton of tuples 
Tuple1 = (0, 1, 2, 3) 
Tuple2 = ('Python', 'For', 'Coding') 
  
Tuple3 = Tuple1 + Tuple2 
  
# Printing first Tuple 
print("Tuple 1: ") 
print(Tuple1) 
  
# Printing Second Tuple 
print("\nTuple2: ") 
print(Tuple2) 
  
# Printing Final Tuple 
print("\nTuples after Concatenaton: ") 
print(Tuple3) 

print('\n')
#######################Slicing of Tuple
# Slicing of a Tuple with Numbers 
Tuple1 = tuple('PYTHONFORCODING') 
  
# Removing First element 
print("Removal of First Element: ") 
print(Tuple1[1:]) 
  
# Reversing the Tuple  
print("\nTuple after sequence of Element is reversed: ") 
print(Tuple1[::-1]) 
  
# Printing elements of a Range 
print("\nPrinting elements between Range 4-9: ") 
print(Tuple1[4:9]) 

print('\n')

#########################Deleting a Tuple
# Deleting a Tuple 
  
#Tuple1 = (0, 1, 2, 3, 4) 
#del Tuple1 
  
#print(Tuple1) 