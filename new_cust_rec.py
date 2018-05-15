# -*- coding: utf-8 -*-
"""
Created on Tue May 15 09:12:07 2018

@author: karthik
"""

# =============================================================================
# Importing necessary Libraries
# =============================================================================

import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.cluster import KMeans

# =============================================================================
# Importing necessary Libraries
# =============================================================================

# =============================================================================
# Start of Data Cleaning and Modification
# =============================================================================

data = pd.read_excel('C:\\Users\\user\\Desktop\\store-dataset.xlsx')
quater16 = pd.datetime(2017,12,31)
quater15 = pd.datetime(2017,9,30)
quater14 = pd.datetime(2017,6,30)
quater13 = pd.datetime(2017,3,31)
quater12 = pd.datetime(2016,12,31)
quater11 = pd.datetime(2016,9,30)
quater10 = pd.datetime(2016,6,30)
quater09 = pd.datetime(2016,3,31)
quater08 = pd.datetime(2015,12,31)
quater07 = pd.datetime(2015,9,30)
quater06 = pd.datetime(2015,6,30)
quater05 = pd.datetime(2015,3,31)
quater04 = pd.datetime(2014,12,31)
quater03 = pd.datetime(2014,9,30)
quater02 = pd.datetime(2014,6,30)
quater01 = pd.datetime(2014,3,31)

data_q16 = data.loc[data['Order Date'] <= quater16]
data_q15 = data.loc[data['Order Date'] <= quater15]
data_q14 = data.loc[data['Order Date'] <= quater14]
data_q13 = data.loc[data['Order Date'] <= quater13]
data_q12 = data.loc[data['Order Date'] <= quater12]
data_q11 = data.loc[data['Order Date'] <= quater11]
data_q10 = data.loc[data['Order Date'] <= quater10]
data_q09 = data.loc[data['Order Date'] <= quater09]
data_q08 = data.loc[data['Order Date'] <= quater08]
data_q07 = data.loc[data['Order Date'] <= quater07]
data_q06 = data.loc[data['Order Date'] <= quater06]
data_q05 = data.loc[data['Order Date'] <= quater05]
data_q04 = data.loc[data['Order Date'] <= quater04]
data_q03 = data.loc[data['Order Date'] <= quater03]
data_q02 = data.loc[data['Order Date'] <= quater02]
data_q01 = data.loc[data['Order Date'] <= quater01]

quaterly_data = [data_q16, data_q15, data_q14, data_q13, data_q12, data_q11, data_q10, data_q09, data_q08, data_q07, data_q06, data_q05, data_q04, data_q03, data_q02, data_q01]

for i in quaterly_data:
    i = i.drop(columns=['Row ID','Ship Date', 'Ship Mode','Country','State', 'Postal Code','Profit per piece', 'MRP', 'MRP per price','Factory Price per piece'],inplace=True)

# =============================================================================
# End of Data Cleaning and Modification
# =============================================================================

# =============================================================================
# Start of similarity function
# =============================================================================
    
def pearson_cosine(x,y):
    import math
    sum_x_i = 0
    sum_y_i = 0
    sum_yi_2 = 0
    sum_xi_2 = 0
    sumx = 0
    sumy = 0
    sum_x_y = 0
    sumx_2 = 0
    sumy_2 = 0
    sumxy = 0
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    for i in range(len(x)):
        sum_x_i += x[i] - x_mean
        sum_y_i += y[i] - y_mean
        sum_x_y += (x[i] - x_mean)*(y[i] - y_mean)
        sum_xi_2 += (x[i] - x_mean)**2
        sum_yi_2 += (y[i] - y_mean)**2
        sumx += x[i]
        sumy += y[i]
        sumxy += x[i]*y[i]
        sumx_2 += x[i]*x[i]
        sumy_2 += y[i]*y[i]
    pearson_correlation = sum_x_y/(math.sqrt(sum_xi_2)*math.sqrt(sum_yi_2))
    cosine_similarity = sumxy/(math.sqrt(sumx_2)*math.sqrt(sumy_2))
    return(pearson_correlation,cosine_similarity)

# =============================================================================
# End of Similarity functions
# =============================================================================

# =============================================================================
# Best Product
# =============================================================================
best_products = data_q01.sort_values(['Profit'],ascending=False).iloc[0:np.shape(data_q01)[0]//20,:]    
# =============================================================================
# End of Best Product    
# =============================================================================
data_q01_kmeans = data_q01.drop(columns=['Order ID','Order Date','Customer Name','Category','Product ID','Region'])
data_q01_kmeans = data_q01_kmeans.dropna()
le = preprocessing.LabelEncoder()

cat_cols = ['Customer ID','Gender','Segment','Sub-Category','City','Product Name']

for x in cat_cols:
    data_q01_kmeans[x] = le.fit_transform(data_q01_kmeans[x])
    

list_product_unique_customer = {}
temp = []
for i in pd.unique(data_q01['Customer ID']):
    temp.append(data_q01[data_q01['Customer ID'] == i]['Product Name'].tolist())
    list_product_unique_customer[i] = list(set(temp[0]))
    temp = []
client_product_matrix = pd.DataFrame(columns = pd.unique(data_q01['Product Name']))    
prods = pd.unique(data_q01['Product Name'])
a = 0
for i in pd.unique(data_q01['Customer ID']):
    VEC = []
    l = list_product_unique_customer[i]
    for j in range(len(prods)):
        if(prods[j] in l):
            VEC.append(1)
        else:
            VEC.append(0)
    #v = pd.DataFrame(VEC, columns=prods)
    #print(v)
    client_product_matrix.loc[a] = VEC
    a += 1
    
kmeans = KMeans(n_clusters=5, random_state=0).fit(client_product_matrix)