from Generator import *
class Vehicle:

    def __init__(self, d, t, h, s, dire, la, tl, pat):
        self.date = d
        self.time = t
        self.head = h # default head 1001
        self.speed = s # default speed 10
        self.patt = pat
        self.axlen = pat.axlen
        self.pattern = pat.patstr
        self.direction = dire # default direction 1
        self.lane = la # default lane 1
        self.tlit = tl #default TLiT 0
        self.gvm = genGVM(pat.patternPara)
        self.axlegwp = genAGWP(pat)
        self.axlew = genAW(self.axlegwp, pat, self.gvm)
        self.axles = genAS(pat)
        self.length = self.length(self.axles)

    def length(self, axles):
        len = 0
        for i in axles:
            len += i
        return len
