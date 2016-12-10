import csv
import yaml



with open('./newriskdetail.csv') as csvfile:
        reader=csv.reader(csvfile,delimiter=',')
        data= {}
        for row in reader:
                if not row[30] in data:
                        data [row[30]]={}               
                data[row[30]][row[44]]={'initial':row[55],'maintenance':row[56]}
               
               
        print (data)
            
      
                
with open('newriskdetail.yml', 'w') as outfile:
   yaml.dump(data, outfile, default_flow_style=False)           
                                    
                        
        
                         
                
        
