from scipy import stats
import matplotlib.pyplot as plt

birthday_card_price = [1.45, 2.20, 0.75, 1.23, 1.25, 1.25, 3.09, 1.99, 2.00, 0.78, 1.32, 2.25, 3.15, 3.85, 0.52, 0.99, 1.38, 1.75, 1.22, 1.75]
res = stats.relfreq(birthday_card_price, numbins=10)
print(res)
start = res.lowerlimit
gap = res.binsize
x_axis = []
frequency = []
cumilative_frequency = res.frequency[0]
print("    Range       Frequency    CF")
for i in range(len(res.frequency)):
    x_axis.append(str(round(start,2))+"-"+str(round(start+gap,2)))
    frequency.append(res.frequency[i]*20)
    print(str(round(start,2))+"-"+str(round(start+gap,2))+"    "+str(res.frequency[i]*20)+"    "+str(round(cumilative_frequency*20)))
    start += gap
    if((i+1)<len(res.frequency)):
        cumilative_frequency = cumilative_frequency+res.frequency[i+1]
plt.bar(x_axis,frequency)        
