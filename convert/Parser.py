import csv

class Parser:

  def s2r(self,stream):
    return csv.reader(stream,delimiter=',')

  def standard(self, stream):
    data = {}
    for row in self.s2r(stream):
      data[row[31]]={'initial':row[42],'maintenance':row[43]}

    return data

  def detailed(self, stream):
      data= {}
      for row in self.s2r(stream):
        if not row[30] in data:
          data [row[30]]={}
        data[row[30]][row[44]]={'initial':row[55],'maintenance':row[56]}

      return data


    def detect(self,stream):
            for row in stream:
                if row[11]=='SC':
                    print ('the file is standard');
                    return
                elif row[11]=='OVL':
                    print ('the file is detailed');
                    return
                else:
                    print ('error file');
                    return


