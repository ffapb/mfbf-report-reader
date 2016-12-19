# https://docs.python.org/2/library/unittest.html#basic-example

import csv, unittest, os, yaml
from Parser import Parser

ROOT=os.path.dirname(os.path.abspath(__file__))

class TestParser(unittest.TestCase):

  def doCommon(self, expectedFn, inputFn, expectedFormat):
    expectedFn = os.path.join(ROOT,"test",expectedFn)
    inputFn = os.path.join(ROOT,"test",inputFn)

    with open(expectedFn, 'r') as expectedStream:
      expectedContent = yaml.load(expectedStream)

      with open(inputFn) as inputStream:
        prs = Parser()
        actualFormat = prs._detect(inputStream)
        self.assertEquals(expectedFormat,  actualFormat  )

        actualContent = None
        if expectedFormat=='standard':
          actualContent = prs._standard(inputStream)
        elif expectedFormat=='detailed':
          actualContent = prs._detailed(inputStream)

        self.assertEquals(expectedContent, actualContent)

        self.assertEquals(expectedContent, prs.parse(inputStream))

  def testStandard(self):
    self.doCommon('standard.yml', 'standard.csv', 'standard')

  def testDetailed(self):
    self.doCommon('detailed.yml', 'detailed.csv', 'detailed')

if __name__ == '__main__':
    unittest.main()
