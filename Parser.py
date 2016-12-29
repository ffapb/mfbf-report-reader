import csv, re

class Parser:

  def __s2r(self,stream):
    return csv.reader(stream,delimiter=',')

  def _str2float(self,string):
    # https://docs.python.org/2/howto/regex.html
    p = re.compile('\((.*)\)')
    m = p.match(string)
    if m: return -1*float(m.group(1))
    return float(string)

  def _standard(self, stream):
    stream.seek(0)
    data = {}
    for row in self.__s2r(stream):
      data[row[31]]={
        'nav':     self._str2float(row[41]),
        'margin.initial.excess': self._str2float(row[42]),
        'margin.maintenance.excess': self._str2float(row[43]),
		'cash': self._str2float(row[40])
      }
    meta={'asof': row[2]}
    return {'meta':meta, 'data': data}
    
       
  def _detailed(self, stream):
    stream.seek(0)
    data= {}
    for row in self.__s2r(stream):
      if not row[30] in data:
        data [row[30]]={
          'nav': self._str2float(row[38]),
		  'cash': self._str2float(row[37]),
          'securities': {}
        }
      data[row[30]]['securities'][row[44]]={
        'margin.initial.excess': self._str2float(row[55]),
        'margin.maintenance.excess': self._str2float(row[56]),
        'positions.securities.long': self._str2float(row[33]),
        'positions.securities.short': self._str2float(row[34]),
        'positions.options.long': self._str2float(row[35]),
        'positions.options.short': self._str2float(row[36]),
        'margin.type': row[45]
      }
    
    meta={'asof': row[2]}
    return {'meta':meta, 'data': data}

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
