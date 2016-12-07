import csv

with open('./newrisk.csv') as csvfile:
	reader=csv.reader(csvfile,delimiter=',')
	for row in reader:
		print(row[31],row[42],row[43])

		
'''ABC123 76678.05 76678.05
DEF123 (49.70) (49.70)'''
