#Creating a List
List = []
print('Initial Blank List : ')
print(List)

#Create with the use of Strings
List = ['Python', 'For', 'Coding'];
print('\nList with the use of Strings : ')
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

print('\n')

###########Adding Elements to a List
#Creating a List
List = []
print('Initial Blank List : ')
print(List)

#Adding Elements
List.append(1)
List.append(2)
List.append(3)
List.append(4)
print("\nList after Addition of FOUR elements: ") 
print(List) 

#Adding Using Iterator
for i in range(1, 4):
	List.append(i)
print("\nList after Addition of elements from 1-3: ") 
print(List)

#Adding Tuples to List
List.append((5, 6))

# Python program to demonstrate  
# Addition of elements in a List 
  
# Creating a List 
List = [] 
print("Intial blank List: ") 
print(List) 
  
# Addition of Elements  
# in the List 
List.append(1) 
List.append(2) 
List.append(4) 
print("\nList after Addition of Three elements: ") 
print(List) 
  
# Adding elements to the List using Iterator 
for i in range(1, 4): 
    List.append(i) 
print("\nList after Addition of elements from 1-3: ") 
print(List) 
  
# Adding Tuples to the List 
List.append((5, 6)) 
print("\nList after Addition of a Tuple: ") 
print(List) 

# Addition of List to a List
List2 = ['For', 'Coding']
List.append(List2)
print("\nList after Addition of a List: ") 
print(List)

# Addition of Element at specific Position (using Insert Method)
List.insert(3, 12)
List2.insert(0, 'Coding')
print("\nList after performing Insert Operation: ") 
print(List) 

# Addition of multiple elements to the List at the end (using Extend Method) 
List.extend([8, 'Coding', 'Always'])
print("\nList after performing Extend Operation: ") 
print(List)

print('\n')

############Accessing elements from the List
# Creating a List with the use of multiple values 
List = ["Python", "For", "Coding"] 

# accessing a element from the list using index number 
print("Accessing a element from the list") 
print(List[0])
print(List[2])

print('\n')

# Creating a Multi-Dimensional List (By Nesting a list inside a List)
List = [['Python', 'For'], ['Coding']]

# accessing a element from the Multi-Dimensional List using index number 
print("Acessing a element from a Multi-Dimensional list") 
print(List[0][1])
print(List[1][0])

List = [1, 2, 'Python', 3, 'For', 'Coding']

print('\n')

# accessing an element using negative indexing 
print("Acessing element using negative indexing") 

# print the last element of list 
print(List[-1]) 
  
# print the third last element of list  
print(List[-2]) 

#########################Removing Elements from the List
# Creating a List 
List = [1, 2, 3, 4, 5, 6,  
        7, 8, 9, 10, 11, 12] 
print("Intial List: ") 
print(List) 

# Removing elements from List using Remove() method 
List.remove(5) 
List.remove(6) 
print("\nList after Removal of two elements: ") 
print(List)

# Removing elements from List using iterator method 
for i in range(1, 5): 
    List.remove(i) 
print("\nList after Removing a range of elements: ") 
print(List) 

# Removing element from the Set using the pop() method 
List.pop() 
print("\nList after popping an element: ") 
print(List)


# Removing element at a specific location from the Set using the pop() method 
List.pop(2) 
print("\nList after popping a specific element: ") 
print(List) 

#####################Slicing of a List
# Creating a List 
List = ['P','Y','T','H','O','N', 
        'F','O','R','C','O','D','I','N','G'] 
print("Initial List: ") 
print(List) 

# Print elements of a range using Slice operation 
Sliced_List = List[3:8] 
print("\nSlicing elements in a range 3-8: ") 
print(Sliced_List)

# Print elements from beginning to a pre-defined point using Slice 
Sliced_List = List[:-6] 
print("\nElements sliced till 6th element from last: ") 
print(Sliced_List)

# Print elements from a pre-defined point to end 
Sliced_List = List[5:] 
print("\nElements sliced from 5th "
      "element till the end: ") 
print(Sliced_List) 

# Printing elements from beginning till end 
Sliced_List = List[:] 
print("\nPrinting all elements using slice operation: ") 
print(Sliced_List) 

# Printing elements in reverse using Slice operation 
Sliced_List = List[::-1] 
print("\nPrinting List in reverse: ") 
print(Sliced_List) 