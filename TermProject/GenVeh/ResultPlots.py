import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
from statsmodels.distributions.empirical_distribution import ECDF
plt.style.use('ggplot')

# Data and histograms
def plotData(x, y, parameter):

    fig0 = plt.figure(num=1,figsize=(12, 5))
    fig0.add_subplot(1,2,1)
    plt.hist(x, bins=50, color='blue', alpha=0.8, align='mid')
    plt.title('GVW histogram')
    # val, cnt = np.unique([round(t) for t in x], return_counts=True)
    # pmf = cnt / float(len(x))
    # PMF = np.column_stack((val, pmf))
    ecdf = ECDF(x)
    cx = np.linspace(0.0,max(x),100)
    fig0.add_subplot(1,2,2)
    eCDF, = plt.plot(cx,ecdf(cx),'r*-')
    cdfy = cdf(parameter,cx)
    CDF, = plt.plot(cx,cdfy,'blue')
    plt.legend([eCDF, CDF],['ECDF','CDF'], loc=2)
    plt.title('Empirical CDF and Parametric CDF')
    ks,p = stats.ks_2samp(ecdf(cx),cdfy)#K-S Test
    rms = rmse(ecdf(cx),cdfy)# Root mean-square error
    plt.text(30,0.2,'K-S statistic: '+str(round(ks,2)))
    plt.text(30,0.1,'Root Mean-Square Error: '+str(round(rms,2)))

    for i in range(0,len(y)-1):
        fig = plt.figure(num=i+2)
        fig.add_subplot(2,2,2)
        plt.hist(y[i],bins=20,color='blue',alpha=0.8,align='mid')
        plt.title('AGWP '+str(i+1)+' histogram')
        fig.add_subplot(2,2,4)
        plt.scatter(y[i],y[i+1],marker="o",alpha=0.8)
        plt.text(max(y[i])-5,min(y[i+1])+1,"alpha: "+str(round(float(parameter[1][i+3]),2)))
        plt.title('Scatter Plot')
        fig.add_subplot(2,2,3)
        plt.title('Joint AGWP')
        plt.hist(y[i+1],bins=20,orientation='horizontal',color='red',alpha=0.8,align='mid')
        plt.title('AGWP '+str(i+2)+' histogram')

    plt.show()

# CDF
def cdf(parameter,x):

    y = float(parameter[0][0])*stats.lognorm.cdf(x,float(parameter[0][2]),0,np.exp(float(parameter[0][1])))\
        +float(parameter[1][0])*stats.norm.cdf(x,float(parameter[1][1]),float(parameter[1][2]))\
        +(1-float(parameter[0][0])-float(parameter[1][0]))*(stats.exponweib.cdf([t-float(parameter[2][0]) for t in x],1,float(parameter[2][2]),0,float(parameter[2][1])))

    return y

# Root Mean Square Error
def rmse(a, b):
    return np.sqrt(((a - b) ** 2).mean())

