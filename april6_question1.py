import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rent_list = [425,430,430,435,435,435,435,435,440,440,440,440,440,445,445,445,445,445,450,450,450,450,450,450,450,460,460,460,465,465,465,470,470,472,475,475,475,480,480,480,480,485,490,490,490,500,500,500,500,510,510,515,525,525,525,535,549,550,570,570,575,575,580,590,600,600,600,600,615,615]
sl_no = list(range(len(rent_list)))
plt.figure(1)
plt.scatter(sl_no,rent_list)

slope_intercept = np.polyfit(sl_no,rent_list,1)
new_rent_list = np.polyval(slope_intercept,sl_no)
plt.plot(sl_no,new_rent_list)

res = stats.relfreq(rent_list, numbins=10)
start = res.lowerlimit
gap = res.binsize
cumilative_frequency = res.frequency[0]
rent_range = []
freq = []
print("    Range       Frequency    CF")
for i in range(len(res.frequency)):
    rent_range.append(str(round(start,2))+"-"+str(round(start+gap,2)))
    freq.append(res.frequency[i]*70)
    print(str(round(start,2))+"-"+str(round(start+gap,2))+"    "+str(res.frequency[i]*70)+"    "+str(round(cumilative_frequency*70)))
    start += gap
    if((i+1)<len(res.frequency)):
        cumilative_frequency = cumilative_frequency+res.frequency[i+1]

plt.figure(2)        
plt.bar(rent_range,freq)