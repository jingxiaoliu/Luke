import random
import numpy as np
import sys

# Gross Vehicle Mass Generator
def genGVM(parameter):
    return lnwGenerator(parameter)

# Apply Copula Correlation to Axle group weight percentage
def ApplyCopula(veh):

    axlegwp = [[]]*veh[0].patt.axlegn
    for i in range(0, veh[0].patt.axlegn):
        for j in range(0, len(veh)):
            axlegwp[i].append(veh[j].axlegwp[i])
    for i in range(0,veh[0].patt.axlegn-1):# sort agwp in the same order as copula samples
        u,v = copulaGenerator(len(axlegwp[i]), abs(float(veh[0].patt.patternPara[1][3+i])))# copula samples
        uIndex = sorted(range(len(u)), key=lambda k: u[k])# sort a list and then return a list with the index of the sorted items in the list
        vIndex = sorted(range(len(v)), key=lambda k: v[k])
        x = [[0]]*(i+1)
        for j in range(0,i+1):
            x[j] = axlegwp[j]
        xIndex = sorted(range(len(x[i])), key=lambda k: x[i][k])
        for j in range(0, i+1):
            t = [0]*len(x[j])
            for q in range(0, len(x[i])):
                t[uIndex[q]] = x[j][xIndex[q]]
            axlegwp[j] = t
        if float(veh[0].patt.patternPara[1][3+i]) < 0:
            y = [100-x for x in axlegwp[i+1]]
        else:
            y = axlegwp[i+1]
        yIndex = sorted(range(len(y)), key=lambda k: y[k])
        t = [0] * len(y)
        for j in range(0, len(y)):
            t[vIndex[j]] = y[yIndex[j]]
        if float(veh[0].patt.patternPara[1][3+i]) < 0:
            axlegwp[i + 1] = [100-x for x in t]
        else:
            axlegwp[i + 1] = t
    for i in range(0, len(veh)):
        for j in range(0, veh[0].patt.axlegn):
            veh[i].axlegwp[j] = axlegwp[j][i]
        veh[i].axlew = genAW(veh[i].axlegwp, veh[0].patt, veh[i].gvm)

    return veh

# Axle Group Weight Percentage Generator
def genAGWP(pattern):
    axlegwp = []
    for i in range(0, pattern.axlegn):
        axlegwp.append(lnwGenerator(pattern.axlewPara[i]))
    return axlegwp

# Axle Weight Generator
def genAW(axlegwp, pattern, GVM):
    axlewp = [0]*20
    count = 0
    for i in range(0, pattern.axlegn):
        for j in range(0, int(pattern.patstr[i])):
            axlewp[count] = axlegwp[i]/int(pattern.patstr[i])
            count += 1
    AW = []
    for i in axlewp:
        AW.append(i * GVM / 100)

    return AW

# Axle Spacing Generator
def genAS(pattern):
    axles = [0]*19
    count = 0
    for i in range(0,pattern.axlegn-1):
        for j in range(0, int(pattern.patstr[i])-1):
            axles[count] = 1.3
            count += 1
        axles[count] = lnwGenerator(pattern.axlesPara[i])
        count += 1
    for i in range(1, int(pattern.patstr[pattern.axlegn-1])):
        axles[count] = 1.3
        count += 1
    return axles

# LNW Generator
def lnwGenerator(parameter):
    r = []
    t = random.uniform(0, 1)
    if t < float(parameter[0][0]):
        r = random.lognormvariate(float(parameter[0][1]), float(parameter[0][2]))
    elif t < (float(parameter[0][0]) + float(parameter[1][0])):
        r = random.gauss(float(parameter[1][1]), float(parameter[1][2]))
    else:
        r = random.weibullvariate(float(parameter[2][1]), float(parameter[2][2])) + float(parameter[2][0])
    return r

# Gumbel Copula Generator
def copulaGenerator(n, theta):
    if theta <= 1:
        raise ValueError('the parameter for GUMBEL copula should be greater than 1')
    if theta < 1 + sys.float_info.epsilon:
        U = np.random.uniform(size=n)
        V = np.random.uniform(size=n)
    else:
        u = np.random.uniform(size=n)
        w = np.random.uniform(size=n)
        w1 = np.random.uniform(size=n)
        w2 = np.random.uniform(size=n)

        u = (u - 0.5) * np.pi
        u2 = u + np.pi / 2
        e = -np.log(w)
        t = np.cos(u - u2 / theta) / e
        gamma = (np.sin(u2 / theta) / t) ** (1 / theta) * t / np.cos(u)
        s1 = (-np.log(w1)) ** (1 / theta) / gamma
        s2 = (-np.log(w2)) ** (1 / theta) / gamma
        U = np.array(np.exp(-s1))
        V = np.array(np.exp(-s2))
    return U,V

# Percentage Scale
def scale(agwp,pattern):
    Sum = 0
    for i in range(0, pattern.axlegn):
        Sum += agwp[i]
    for i in range(0, pattern.axlegn):
        agwp[i] /= (Sum/100)

    return agwp
