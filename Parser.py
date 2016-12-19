import csv

class Parser:

  def __s2r(self,stream):
    return csv.reader(stream,delimiter=',')

  def _standard(self, stream):
    stream.seek(0)
    data = {}
    for row in self.__s2r(stream):
      data[row[31]]={'initial':row[42],'maintenance':row[43]}

    return data

  def _detailed(self, stream):
    stream.seek(0)
    data= {}
    for row in self.__s2r(stream):
      if not row[30] in data:
        data [row[30]]={}
      data[row[30]][row[44]]={'initial':row[55],'maintenance':row[56]}

    return data

  def _detect(self,stream):
    stream.seek(0)
    for row in self.__s2r(stream):
      if row[11]=='SC':
        return 'standard'
      elif row[11]=='OVL':
        return 'detailed'
      else:
        return 'other'

  def parse(self,stream):
    fileFormat = self._detect(stream)

    if fileFormat=='standard':
      return self._standard(stream)
    elif fileFormat=='detailed':
      return self._detailed(stream)
