class Date:

    def __init__(self, y, m, d):
        if ((m == 4) or (m == 6) or (m == 9) or (m == 11)) and (d > 30) or (d > 31) or (d <= 0):
            print "Invalid date"
        elif m == 2:
            if (y % 4 == 0) and (y % 100 != 0) and (d > 29) or (d <= 0):
                print "Invalid date"
            elif (y % 400 == 0) and (d > 29) or (d <= 0):
                print "Invalid date"
            elif (d > 28) or (d <= 0):
                print "Invalid date"
            else:
                self.year = y
                self.month = m
                self.date = d
        else:
            self.year = y
            self.month = m
            self.date = d

    def isLeapYr (self): # return 1 if the year of the date is leap year
        if (self.year % 4 == 0) and (self.year % 100 != 0):
            return 1
        elif self.year % 400 == 0:
            return 1
        else:
            return 0

    def DaysinMon(self): #return the number of days in that month, you need to consider leap year here
        if (self.month == 4) or (self.month == 6) or (self.month == 9) or (self.month == 11):
            return 30
        if self.month == 2:
            if self.isLeapYr():
                return 29
            else:
                return 28
        else:
            return 31

    #  Implement the == function in myDate()
    def __eq__(self, other):
        if (self.date == other.date) and (self.month == other.month) and (self.year == other.year):
            return True
        else:
            return False

    # Implement comparison between two myDate type, this is used to sort an array of Dates in Sorted()
    def __cmp__(self, other): #return any negative integer if "self" is earlier than "other", zero if self == other, return a positive number if "self" is later than "other"
        if self == other:
            return 0
        elif self - other > 0:
            return 1
        else:
            return -1

    def DaysinYear(self):
        if self.isLeapYr():
            return 366
        else:
            return 365

    def totalDays(self):
        selfDays = 0
        for i in range(1, self.year - 1900):
            dd = myDate(1900 + i - 1, self.month, self.date)
            selfDays += dd.DaysinYear()
        for i in range(1, self.month-1):
            dd = myDate(self.year, i, self.date)
            selfDays += dd.DaysinMon()
        selfDays += self.date
        return selfDays

    # Implement subtraction between two myDate type, you may need to use the functions defined above
    def __sub__(self, other): # return the number of days between two myDate class, negative if "self" is earlier than "other", zero if self == other, positive if "self" is later than "other"
        return self.totalDays() - other.totalDays()

    # Implement the print method for myDate
    def __repr__(self):
        return "Month: "+str(self.month)+" Day: "+str(self.date)+" Year: "+str(self.year)
