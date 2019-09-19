a = [1, 2, 3]
try:
    print 'Second element = %d' %(a[1])

    print 'Fourth elements = %d' %(a[3])

except IndexError:
    print 'An error has occured'

#A try statement can have more than one except clause, to specify handlers for different exceptions. Please note that at most one handler will be executed.
# Program to handle multiple errors with one except statement
try:
    a = 3
    if a < 4 :
        b = a / ( a - 3 )

    print 'Value of b = ', b

except(ZeroDivisionError, NameError):
    print ('\nError has occured and Handled')

try:
    a = 3
    if a > 4:
        b = a / (a - 3)

    print 'Value of b = ', b

except(ZeroDivisionError, NameError):
    print('\nError has occured and Handled')


#Else Clause:
def fun(a, b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print "a/b result in 0"
    else:
            print c

fun(2, 3)
fun(3, 3)

# Program to depict Raising Exception

try:
    raise NameError("Something is Wrong")  # Raise Error
except NameError:
    print "An exception"
    raise  # To determine whether the exception was raised or not
