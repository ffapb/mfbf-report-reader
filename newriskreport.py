import csv

data={}
with open('./newrisk.csv') as csvfile:
	reader=csv.reader(csvfile,delimiter=',')
	for row in reader:
		data[row[31]]={'initial':row[42],'maintenance':row[43]}

print data

		
'''ABC123 76678.05 76678.05
DEF123 (49.70) (49.70)'''
