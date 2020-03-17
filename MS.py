import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

##
#Biophysics lab AGH - Mossbauer spectroscopy
#Fitting theoretical curve to measurement points
#Bartek Lukasik
##

def lorentz6P(x, y0, amp1, cen1, wid1, amp2, cen2, wid2, amp3, cen3, wid3, amp4, cen4, wid4, amp5, cen5, wid5, amp6, cen6, wid6):
    return y0+2*amp1/np.pi*wid1/(4*(x-cen1)**2+wid1**2)+\
2*amp2/np.pi*wid2/(4*(x-cen2)**2+wid2**2)+\
2*amp3/np.pi*wid3/(4*(x-cen3)**2+wid3**2)+\
2*amp4/np.pi*wid4/(4*(x-cen4)**2+wid4**2)+\
2*amp5/np.pi*wid5/(4*(x-cen5)**2+wid5**2)+\
2*amp6/np.pi*wid6/(4*(x-cen6)**2+wid6**2)

data = pd.read_csv("moss.csv", delimiter='_', names=['args','vals'])

args = list()
vals = list()

for i in range(0,len(data)):
    vals.append(data.iloc[i][1])
    args.append(data.iloc[i][0])

popt, pcov = curve_fit(lorentz6P, args, vals, p0=[4435, 3538, 60, 1, 3736, 88, 1, 3999, 116, 1, 3962, 138, 1, 3658, 166, 1, 3540, 194, 1])

plt.figure(figsize=(20,10))
plt.plot(args, vals, 'r.')
plt.plot(args, lorentz6P(args, *popt), 'b-')
plt.xlabel("Channel")
plt.ylabel("Counts")
plt.show()

#regression parameters

print("y0:", popt[0])
j=1
for i in range(1,18,3):
    while j<7:
        print("peak amplitude ", j , "  ", popt[i])
        j+=1
        break
j=1    
for i in range(2,19,3):
    while j<7:
        print("peak central point ", j , "  ", popt[i])
        j+=1
        break
j=1   
for i in range(3,20,3):
    while j<7:
        print("peak width ", j , "  ", popt[i])
        j+=1
        break

#standard error calculations
perr = np.sqrt(np.diag(pcov))

j=1
print("niepewnosc wyznaczenia y0:", perr[0])
for i in range(1,18,3):
    while j<7:
        print("peak amplitude error ", j , "  ", perr[i])
        j+=1
        break
j=1    
for i in range(2,19,3):
    while j<7:
        print("peak central point error ", j , "  ", perr[i])
        j+=1
        break
j=1   
for i in range(3,20,3):
    while j<7:
        print("peak width error ", j , "  ", perr[i])
        j+=1
        break
##EOF