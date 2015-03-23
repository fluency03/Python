#!/usr/bin/python
# continue

while True:
	s = raw_input('Enter something: ')
	if s == 'quit':
		break
	if len(s) == 3:
		continue
	print 'Input length is not \'quit\''
