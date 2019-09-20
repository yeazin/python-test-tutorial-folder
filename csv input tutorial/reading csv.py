#reading CSV file 

import csv

with open('csvfile.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	dates=[]
	colors=[]
	for row in readCSV:
		'''
		print('')
		print(row[0],row[1],row[2],row[3])
		'''
		color=row[3]
		date=[0]

		dates.append(date)
		colors.append(color)

	print(dates)
	print(colors)

	askcolor=input('what color do u want to know the date of?:')
	coldex= colors.index(askcolor.lower())

	thedate = dates[coldex]

	print('the date of ',askcolor,'is',thedate)


