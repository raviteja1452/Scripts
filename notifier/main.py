import os,sys
from datetime import datetime

if __name__ == '__main__':

	#List of Notifiers
	notifiers = []
	with open('notifiers.txt') as f:
		for line in f:
			item = line.split(";")[:3];
			print item[0]
			item[0] = datetime.strptime(item[0].strip(), '%d/%m/%Y %I:%M:%S %p')
			print item[0]
			notifiers.append(item)
	print notifiers
