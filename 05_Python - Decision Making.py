######################
	#If Statement
######################
i = 26
if (i > 20):
	print('20 is less than 26')
print('Bye!!!!')

print('\n')

######################
	#If-Else Statement
######################
i = 26
if (i < 15):
	print('i is smaller than 15')
	print('I\'m in IF block')
else:
	print('i is greater than 15')
	print('I\'m in ELSE block')
print('I\'m neither in IF nor in ELSE block')

print('\n')

######################
	#Nested-If Statement
######################
i = 10
if (i == 10):
	# First if statement
	if (i < 15):
		print('i is smaller than 15')
	# Nested - if statement will only be executed if statement above is true
	if (i < 12):
		print('i is smaller than 12 too')
	else:
		print('i is greater than 15')

print('\n')

######################
	#if-elif-else ladder Statement
######################
i = 20
if (i == 10):
	print('i is 10')
elif (i == 15):
	print('i is 15')
elif (i == 20):
	print('i is 20')
else:
	print('i is not present')

print('\n')

print('Goodbye')