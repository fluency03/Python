#!/usr/bin/python3

import re
import sys

class Report_timing():
	def arrival_time(self):
		pattern = re.compile(r'(-\sArrival Time\s*)(\d\.\d{3})')
		output = open('output.txt', 'w')
		count = 0
		with open('report_timing_setup.rpt') as f:
			for line in f:
				match = pattern.search(line)
				if match:
					count += 1
					output.write('PATH' + str(count) + ' ' +line)
					# print (match.group(1), match.group(2))
				if count == 5:
					output.close()
					return 0
		output.close()
		return 1

solution = Report_timing()

solution.arrival_time()



