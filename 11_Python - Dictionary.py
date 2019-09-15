#########################
	#Dictionary
########################
# Creating an empty Dictionary 
Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 
  
# Creating a Dictionary with Integer Keys 
Dict = {1: 'Python', 2: 'For', 3: 'Coding'} 
print("\nDictionary with the use of Integer Keys: ") 
print(Dict) 
  
# Creating a Dictionary with Mixed keys 
Dict = {'Name': 'Python', 1: [1, 2, 3, 4]} 
print("\nDictionary with the use of Mixed Keys: ") 
print(Dict) 

# Creating a Dictionary with dict() method 
Dict = dict({1: 'Python', 2: 'For', 3:'Coding'}) 
print("\nDictionary with the use of dict(): ") 
print(Dict) 
  
# Creating a Dictionary with each item as a Pair 
Dict = dict([(1, 'Python'), (2, 'For')]) 
print("\nDictionary with each item as a pair: ") 
print(Dict) 

print('\n')

######################Nested Dictionary
# Creating a Nested Dictionary as shown in the below image 
Dict = {1: 'Python', 2: 'For',  
        3:{'A' : 'Welcome', 'B' : 'To', 'C' : 'Python'}} 
  
print(Dict)  

#####################Adding elements to a Dictionary

# Creating an empty Dictionary 
Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 
  
# Adding elements one at a time 
Dict[0] = 'Python'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ") 
print(Dict) 
  
# Adding set of values to a single Key 
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ") 
print(Dict) 
  
# Updating existing Key's Value 
Dict[2] = 'Welcome'
print("\nUpdated key value: ") 
print(Dict) 
  
# Adding Nested Key value to Dictionary 
Dict[5] = {'Nested' :{'1' : 'Life', '2' : 'Python'}} 
print("\nAdding a Nested Key: ") 
print(Dict) 

print('\n')

########################Accessing elements from a Dictionary
# Creating a Dictionary  
Dict = {1: 'Python', 'name': 'For', 3: 'Coding'} 
  
# accessing an element using key 
print("Acessing an element using key:") 
print(Dict['name']) 

print('\n')
  
# accessing an element using key 
print("Acessing an element using key:") 
print(Dict[1]) 

print('\n')
  
# accessing an element using get() method 
print("Acessing an element using get:") 
print(Dict.get(3)) 

print('\n')

##################Removing Elements From a Dictionary
# Initial Dictionary
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Python', 
        'A' : {1 : 'Python', 2 : 'For', 3 : 'Coding'}, 
        'B' : {1 : 'Python', 2 : 'Life'}} 
print("Initial Dictionary: ") 
print(Dict) 
  
print('\n')

# Deleting a Key value 
del Dict[6] 
print("\nDeleting a specific key: ") 
print(Dict) 

print('\n')

# Deleting a Key from Nested Dictionary 
del Dict['A'][2] 
print("\nDeleting a key from Nested Dictionary: ") 
print(Dict) 

print('\n')

# Deleting a Key using pop() 
Dict.pop(5) 
print("\nPopping specific element: ") 
print(Dict) 

print('\n')

# Deleting an arbitrary Key-value pair using popitem() 
Dict.popitem() 
print("\nPops an arbitrary key-value pair: ") 
print(Dict) 

print('\n')

# Deleting entire Dictionary 
Dict.clear() 
print("\nDeleting Entire Dictionary: ") 
print(Dict) 

print('\n')































