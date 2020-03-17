import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

##
#Biophysics lab AGH - Mossbauer spectroscopy
#Fitting theoretical curve to measurement points
#Bartek Lukasik
##

def lorentz2P(x, y0, amp1, cen1, wid1, amp2, cen2, wid2):
    return y0+2*amp1/np.pi*wid1/(4*(x-cen1)**2+wid1**2)+2*amp2/np.pi*wid2/(4*(x-cen2)**2+wid2**2)


data = pd.read_csv("oxy.csv", sep=',', names=['args','vals'])

args = list()
vals = list()

for i in range(0,len(data)):
    vals.append(data.iloc[i][1])
    args.append(data.iloc[i][0])

#predicted parameters
amp1_pred = 3.35278e+06
cen1_pred = -0.869
amp2_pred = 3.35101e+06
cen2_pred = 1.217

popt, pcov = curve_fit(lorentz2P, args, vals, p0=[1,amp1_pred,cen1_pred,1,amp2_pred,cen2_pred,1])
#1 is default value for p0 in curve_fit

plt.figure(figsize=(20,10))
plt.plot(args, vals, 'r.')
plt.plot(args, lorentz2P(args, *popt), 'b-')
plt.xlabel("Prędkosć [mm/s]")
plt.ylabel("Liczba zliczeń")
plt.show()

#regression parameters

print("y0:", popt[0])
j=1
for i in range(1,7,3):
    while j<3:
        print("peak amplitude ", j , "  ", popt[i])
        j+=1
        break
j=1    
for i in range(2,8,3):
    while j<3:
        print("peak central point ", j , "  ", popt[i])
        j+=1
        break
j=1   
for i in range(3,9,3):
    while j<3:
        print("peak width ", j , "  ", popt[i])
        j+=1
        break

#standard error calculations
perr = np.sqrt(np.diag(pcov))

j=1
print("y0 error:", perr[0])
for i in range(1,7,3):
    while j<3:
        print("peak amplitude error ", j , "  ", perr[i])
        j+=1
        break
j=1    
for i in range(2,8,3):
    while j<3:
        print("peak central point error ", j , "  ", perr[i])
        j+=1
        break
j=1   
for i in range(3,9,3):
    while j<3:
        print("peak width error ", j , "  ", perr[i])
        j+=1
        break
##EOF