# https://docs.python.org/2/library/unittest.html#basic-example

import csv, unittest, os, yaml
from Parser import Parser

ROOT=os.path.dirname(os.path.abspath(__file__))

class TestParser(unittest.TestCase):

  def doCommon(self,fn1,fn2):
    expectedFn = os.path.join(ROOT,"test",fn1)

    with open(expectedFn, 'r') as stream:
      expected = yaml.load(stream)

      filename = os.path.join(ROOT,"test",fn2)
      with open(filename) as fh:
        prs = Parser()
        return prs.standard(fh)
        self.assertEquals(expected, prs.standard(fh))

  def testStandard(self):
    self.doCommon('standard.yml','standard.csv')

  def testStandard(self):
    self.doCommon('detailed.yml','detailed.csv')

if __name__ == '__main__':
    unittest.main()
