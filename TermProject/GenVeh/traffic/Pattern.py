from IO.ParameterReader import *

class Pattern:

    def __init__(self, pts):
        self.patstr = pts
        self.axlen = 0
        self.genan()
        self.axlegn = 0
        self.genagn()
        self.patternPara = parameterReader(pts)
        self.axlewPara = self.axlewParaReader(self.axlegn, self.patternPara)
        self.axlesPara = self.axlesParaReader(self.axlegn, self.patternPara)
        self.proportion = self.patternPara[2][2+self.axlegn]

# Generate Number of Axle Groups
    def genagn(self):
        self.axlegn = len(self.patstr)

# Generate Number of Axles
    def genan(self):
        self.axlen = 0
        for i in range(0, len(self.patstr)):
            self.axlen += int(self.patstr[i])

# Read Axle Weight Parameters
    def axlewParaReader(self, axlegn, patternPara):
        para = []
        for i in range(0, axlegn):
            fname = patternPara[0][3 + i]
            para.append(parameterReader(fname))
        return para

# Read Axle Spacing Parameters
    def axlesParaReader(self, axlegn, patternPara):
        para = []
        for i in range(0, axlegn-1):
            fname = patternPara[2][3 + i]
            para.append(parameterReader(fname))
        return para
