import os,sys

if __name__ == '__main__':

	#List of Notifiers
	notifiers = []
	with open('notifiers.txt') as f:
		for line in f:
			notifiers.append(line.split("%%%")[:3])
	print notifiers
