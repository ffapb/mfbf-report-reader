import csv
import yaml

data={}
with open('./accounts.csv') as csvfile:
	reader=csv.reader(csvfile,delimiter=',')
	for row in reader:
		data[row[31]]={'initial':row[42],'maintenance':row[43]}

with open('accounts.yml', 'w') as outfile:
    yaml.dump(data, outfile, default_flow_style=False)
