import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

##
#Biophysics lab AGH - Mossbauer spectroscopy
#Fitting theoretical curve to measurement points
#Bartek Lukasik
##

def lorentz6P(x, y0, A1, cen1, wid1, A2, cen2, wid2, A3, cen3, wid3, A4, cen4, wid4, A5, cen5, wid5, A6, cen6, wid6):
    return y0+2*A1/np.pi*wid1/(4*(x-cen1)**2+wid1**2)+\
2*A2/np.pi*wid2/(4*(x-cen2)**2+wid2**2)+\
2*A3/np.pi*wid3/(4*(x-cen3)**2+wid3**2)+\
2*A4/np.pi*wid4/(4*(x-cen4)**2+wid4**2)+\
2*A5/np.pi*wid5/(4*(x-cen5)**2+wid5**2)+\
2*A6/np.pi*wid6/(4*(x-cen6)**2+wid6**2)

data = pd.read_csv("moss.csv", delimiter='_', names=['args','vals'])

args = list()
vals = list()

for i in range(0,len(data)):
    vals.append(data.iloc[i][1])
    args.append(data.iloc[i][0])
#predicted parameters
y0_pred = 4435
A1_pred = 3538
cen1_pred = 60
A2_pred = 3736
cen2_pred = 88
A3_pred = 3999
cen3_pred = 116
A4_pred = 3962
cen4_pred = 138
A5_pred = 3658
cen5_pred = 166
A6_pred = 3540
cen6_pred = 194

popt, pcov = curve_fit(lorentz6P, args, vals, p0=[y0_pred, A1_pred, cen1_pred, 1, A2_pred, cen2_pred, 1, A3_pred, cen3_pred, 1, A4_pred, cen4_pred, 1, A5_pred, cen5_pred, 1, A6_pred, cen6_pred, 1])
#1 is default value for p0 in curve_fit

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
        print("area ", j , "  ", popt[i])
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
print("y0 error:", perr[0])
for i in range(1,18,3):
    while j<7:
        print("area error ", j , "  ", perr[i])
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
