from traffic.Vehicle import Vehicle
from traffic.Pattern import Pattern
from arrivalTime.Time import Time
from arrivalTime.Date import Date
from IO.WriteBeDIT import writeBeDIT
from Generator import ApplyCopula
import os.path
import random
import time

def GenVeh(number, pattern, directory):

    fileName = os.path.join(directory, "simulation result.txt")
    start = time.clock()

    v = []
    axlegwp = []
    gvm = []
    parameter = []
    #Generate by pattern
    for i in pattern:
        veh = []
        pattern = Pattern(i)
        parameter.append(pattern.patternPara)
        agwp = []
        g = []
        for j in range(0, int(number*float(pattern.proportion))):
            veh.append(Vehicle(Date(15, 6, 1), Time(1, 1, 1), 1001, 10, 1, 1, 0, pattern))
        for i in range(0, veh[0].patt.axlegn):
            agwp.append([])
            for j in range(0, len(veh)):
                agwp[i].append(veh[j].axlegwp[i])
        for j in range(0, len(veh)):
            g.append(veh[j].gvm)
        # Apply Copula Correlation
        v += ApplyCopula(veh[len(veh)-int(number*float(pattern.proportion)):len(veh)])

        axlegwp.append(agwp)
        gvm.append(g)
    random.shuffle(v)
    writeBeDIT(v, fileName)

    end = time.clock()
    # print "Run time: "+str(end - start)+" s"
    return axlegwp, gvm, parameter
