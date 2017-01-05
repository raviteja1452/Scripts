import os,sys
from datetime import datetime

def readNotifications():
	notifiers = []
	with open('notifiers.txt') as f:
		for line in f:
			item = line.split(";")[:3]
			item[0] = datetime.strptime(item[0].strip(), '%d/%m/%Y %I:%M:%S %p')
			notifiers.append(item)
	notifiers.sort(key=lambda x: x[0])
	return notifiers
def printNotification(subject,message):
	return TRUE
if __name__ == '__main__':

	#List of Notifiers
	notifiers = readNotifications()
	printNotification('Ravi','Have a good time')
