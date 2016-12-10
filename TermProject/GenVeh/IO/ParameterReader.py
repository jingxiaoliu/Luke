import csv
import os.path

def parameterReader(pattern):
    Str = []
    fname = str(pattern)+".csv"
    with open(fname, 'rb') as f:
        reader = csv.reader(f, delimiter=',', quotechar='|')
        for row in reader:
            Str.append(row)
    return Str
