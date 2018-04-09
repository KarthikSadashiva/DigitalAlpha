import pandas as pd
import matplotlib.pyplot as plt
import numpy
import seaborn as sns 
df = pd.read_excel('C:\\Users\\user\\.spyder-py3\\beer.xlsx', sheetname='Sheet1')
 
print("Column headings:")
#print(df.columns)

p12 = df['PRICE 12PK']
p18 = df['PRICE 18PK']
p30 = df['PRICE 30PK']

c12 = df['CASES 12PK']
c18 = df['CASES 18PK']
c30 = df['CASES 30PK']

#Analysis of the data
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
#price comparison
plt.figure(2)
plt.subplot(211)
plt.plot(range(len(p12)),p12,marker='o')
plt.plot(range(len(p12)),p18,marker='o')
plt.plot(range(len(p12)),p30,marker='o')

plt.subplot(212)
plt.plot(range(len(c12)),c12)
plt.plot(range(len(c12)),c18)
plt.plot(range(len(c12)),c30)

#p12_c12_corrcoef = numpy.corrcoef(p12,c12)
#p18_c18_corrcoef = numpy.corrcoef(p18,c18)
#p30_c30_corrcoef = numpy.corrcoef(p30,c30)


#Normalizing of data
#To find corelation between price and sales volume
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
print("Normalized")
print(p30_norm)
print(c30_norm)
plt.plot(p30_norm,marker='o')
plt.plot(c30_norm,marker='o')
plt.show()
#plt.scatter(range(len(p12)),p12_norm)
#plt.scatter(range(len(c12)),c12_norm)

#print(p12_c12_corrcoef,p18_c18_corrcoef,p30_c30_corrcoef)
#finding the line of best fit between p12 and c12
 
"""plt.figure(6)
p1 = numpy.polyfit(p12,c12,1)
plt.plot(p12,numpy.polyval(p1,p12))
plt.show()"""
plt.figure(6)
price_corr_mat1 = numpy.corrcoef([p12,p18,p30,c12,c18,c30])
total_corr=numpy.corrcoef([p12,p18,p30,c12,c18,c30])
print(df.dropna().corr())
print(sns.heatmap(df.corr()))
plt.figure(7)
p1=numpy.polyfit(p12,c12,1)
p2=numpy.polyfit(p18,c18,1)
p3=numpy.polyfit(p30,c30,1)
plt.plot(p12,numpy.polyval(p1,p12),'r-')
plt.plot(p12,c12,'o')
plt.show()
plt.plot(p18,numpy.polyval(p2,p18),'r-')
plt.plot(p18,c18,'o')
plt.plot(p18,numpy.polyval(p2,p18))
plt.show()
plt.plot(p30,numpy.polyval(p3,p30),'r-')
plt.plot(p30,c30,'o')
plt.show()

print("Perfect polyfit")
#print(p1)
#print(p2)
#print(p3)
print(price_corr_mat1)
#finding prediction p12
a=list(range(1,53))
price_predict12=p12
price_fit_predict=numpy.polyfit(a,price_predict12,1)
print(price_fit_predict)
plt.plot(a,price_predict12,'o')
plt.plot(a,numpy.polyval(price_fit_predict,a),'r-')
plt.show()
list_of_prediction_price=[]
list_of_sale_prediction=[]
for i in range(53,100):
    list_of_prediction_price.append(i*price_fit_predict[0]+price_fit_predict[1])
print(list_of_prediction_price)
for i in list_of_prediction_price:
    list_of_sale_prediction.append((i*p1[0])+p1[1])

print(list_of_sale_prediction)

#price predict p18
price_predict18=p18
price_fit_predict=numpy.polyfit(a,price_predict18,1)
print(price_fit_predict)
plt.plot(a,price_predict18,'o')
plt.plot(a,numpy.polyval(price_fit_predict,a),'r-')
plt.show()
list_of_prediction_price=[]
list_of_sale_prediction=[]
for i in range(53,100):
    list_of_prediction_price.append(i*price_fit_predict[0]+price_fit_predict[1])
print(list_of_prediction_price)
for i in list_of_prediction_price:
    list_of_sale_prediction.append((i*p2[0])+p2[1])

print(list_of_sale_prediction)

#price predict p30
price_predict30=p30
price_fit_predict=numpy.polyfit(a,price_predict30,1)
print(price_fit_predict)
plt.plot(a,price_predict30,'o')
plt.plot(a,numpy.polyval(price_fit_predict,a),'r-')
plt.show()
list_of_prediction_price=[]
list_of_sale_prediction=[]
for i in range(53,100):
    list_of_prediction_price.append(i*price_fit_predict[0]+price_fit_predict[1])
print(list_of_prediction_price)
for i in list_of_prediction_price:
    list_of_sale_prediction.append((i*p3[0])+p3[1])

print(list_of_sale_prediction)
#mp.plot(x,np.polyval(p2,x),'g-')
#mp.show()
