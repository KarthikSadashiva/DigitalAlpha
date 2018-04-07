import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import matplotlib.pyplot as plt
import numpy
 
df = pd.read_excel('beer.xlsx', sheetname='Sheet1')
 
print("Column headings:")
print(df.columns)

p12 = df['PRICE 12PK']
p18 = df['PRICE 18PK']
p30 = df['PRICE 30PK']

c12 = df['CASES 12PK']
c18 = df['CASES 18PK']
c30 = df['CASES 30PK']

plt.figure(1)
plt.subplot(321)
plt.plot(range(len(p12)),p12,'g')
plt.subplot(323)
plt.plot(range(len(p12)),p18,'r')
plt.subplot(325)
plt.plot(range(len(p12)),p30,'b')
plt.subplot(322)
plt.plot(range(len(c12)),c12,'g')
plt.subplot(324)
plt.plot(range(len(c12)),c18,'r')
plt.subplot(326)
plt.plot(range(len(c12)),c30,'b')

plt.figure(2)
plt.plot(range(len(p12)),p12,'g')
plt.plot(range(len(p12)),p18,'r')
plt.plot(range(len(p12)),p30,'b')

#p12_c12_corrcoef = numpy.corrcoef(p12,c12)
#p18_c18_corrcoef = numpy.corrcoef(p18,c18)
#p30_c30_corrcoef = numpy.corrcoef(p30,c30)

plt.figure(3)
p12_norm = p12/numpy.max(p12)
c12_norm = c12/numpy.max(c12)
plt.plot(p12_norm,marker='o')
plt.plot(c12_norm,marker='o')

plt.figure(4)
p18_norm = p18/numpy.max(p18)
c18_norm = c18/numpy.max(c18)
plt.plot(p18_norm,marker='o')
plt.plot(c18_norm,marker='o')

plt.figure(5)
p30_norm = p30/numpy.max(p30)
c30_norm = c30/numpy.max(c30)
plt.plot(p30_norm,marker='o')
plt.plot(c30_norm,marker='o')
#plt.scatter(range(len(p12)),p12_norm)
#plt.scatter(range(len(c12)),c12_norm)

print(p12_c12_corrcoef,p18_c18_corrcoef,p30_c30_corrcoef)

plt.figure(6)
p1 = numpy.polyfit(p12,c12,1)
plt.plot(p12,c12,'o')
plt.plot(p12,numpy.polyval(p1,p12))

price_corr_mat1 = numpy.corrcoef([p12,c12,c18,c30])
price_corr_mat2 = numpy.corrcoef([p18,c12,c18,c30])
price_corr_mat3 = numpy.corrcoef([p30,c12,c18,c30])


print(price_corr_mat1)
print(price_corr_mat2)
print(price_corr_mat3)