#!/usr/bin/python
# while

number = 23
running = True

while running:
	guess = int(raw_input('Enter an integer: '))
	
	if guess == number:
		print 'Congratulations!'
		running = False
	elif guess < number:
		print 'Higher'
	else:
		print 'Lower'
else:
	print 'While loop is over.'

print 'Done'
