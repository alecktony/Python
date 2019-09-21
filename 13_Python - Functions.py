########################
	#FUNCTIONS
########################
def evenOdd(x):
	if (x % 2 == 0):
		print 'even'
	else:
		print 'odd'

evenOdd(2)
evenOdd(3)

def myFun(x):
	x[0] = 20
lst = [10, 11, 12, 13, 14, 15]
myFun(lst);
print(lst)

print('\n')

def myFun(y):
	y = [20, 30, 40]
lst = [10, 11, 12, 13, 14, 15]
myFun(lst);
print(lst)

print('\n')

def myFun(x, y = 50):
	print('x: ', x)
	print('y: ', y)
myFun(10)

print('\n')

def person(firstname, lastname):
	print(firstname, lastname)
person(firstname = 'Amani', lastname = 'Lecktony')
person(lastname = 'Lecktony', firstname = 'Amani')

print('\n')

def myFun(*argv):  
    for arg in argv:  
        print (arg) 
    
myFun('Hello', 'Welcome', 'to', 'NOTTECH')  

print('\n')

quatro = lambda x: x*x*x
print(quatro(5))

print('Goodbye')