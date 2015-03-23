#!/usr/bin/python
# if test

number = 23
guess = int(raw_input('Please input an integer: '))

if guess == number:
	print 'Congratulations, you guessed it right. '
	ha = 'ha'*3
	print 'ha*3', ha
elif guess < number:
	print 'No, it is higher!'
else:
	print 'No, it is lower!'

print 'Done'