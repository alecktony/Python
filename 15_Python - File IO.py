# a file named "geek", will be opened with the reading mode.
file = open('nottech.txt', 'r')
# This will print every line one by one in the file
for each in file:
    print(each)

print('\n')

file = open('nottech.txt', 'r')
print file.read()

print('\n')

file = open('nottech.txt', 'r')
print file.read(6)

print('\n')

# Python code to illustrate append() mode
file = open('nottech.txt', 'a')
file.write("This will add this line")
file.close()

######## Write file
file = open('amani.txt', 'w')
file.write('I\'m Amani Lecktony')
file.write('I like JavaScript')
file.write('I am currently learning Python')
file.close()

with open('amani.txt', 'w') as f:
    f.write('Python Programming')

# Python code to illustrate split() function
with open("amani.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print word
