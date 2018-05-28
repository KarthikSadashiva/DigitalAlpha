# -*- coding: utf-8 -*-
"""
Created on Mon May 28 11:32:14 2018

@author: user
"""

import pandas as pd
from sklearn import linear_model
import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

root = tk.Tk()
root.geometry('900x600')
root.resizable(0,0)
root.title('DM - Sales and Profit Prediction')

yearLabel = tk.Label(root, text='Select Year')
yearLabel.place(relx = 0.1, rely = 0.1)

monthLabel = tk.Label(root, text='Select Month')
monthLabel.place(relx = 0.3, rely = 0.1)

SubcategoryLabel=tk.Label(root,text='Select Sub-Category')
SubcategoryLabel.place(relx=0.5,rely =0.1)

predictedSalesLabel = tk.Label(root, text = 'Predicted Sales')
predictedSalesLabel.place(relx=0.25, rely=0.25)
#predictedSalesText = tk.StringVar(root)
#predictedSalesEntry = tk.Entry(root,textvariable=predictedSalesText)
#predictedSalesEntry.place(relx=0.25, rely=0.33)
predictedProfitLabel = tk.Label(root, text = 'Predicted Profit')
predictedProfitLabel.place(relx=0.5, rely=0.25)
#predictedProfitText = tk.StringVar(root)
#predictedProfitEntry = tk.Entry(root, textvariable=predictedProfitText)
#predictedProfitEntry.place(relx=0.5, rely=0.33)

Month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
Year = ['2017','2016','2015','2014']
Subcategory =['Art', 'Phones', 'Binders', 'Furnishings', 'Paper', 'Appliances','Tables', 'Accessories', 'Chairs', 'Envelopes', 'Fasteners','Storage', 'Copiers', 'Machines', 'Labels', 'Supplies', 'Bookcases']

month = tk.StringVar(root) 
year = tk.StringVar(root)
subcategory =tk.StringVar(root)

month.set('Jan')
year.set('2017')
subcategory.set('Art')

monthOP = tk.OptionMenu(root,month,*Month)
yearOP = tk.OptionMenu(root,year,*Year)
subcategoryOP =tk.OptionMenu(root,subcategory,*Subcategory)

monthOP.place(relx = 0.3, rely = 0.15)
yearOP.place(relx = 0.1, rely = 0.15)
subcategoryOP.place(relx=0.5,rely =0.15)

def getSalesProfit():
    yearSelected = int(year.get())
    monthSelected = Month.index(month.get())+1
    sub_category_selected = subcategory.get()
    
    data=pd.read_excel(r'C:\Users\user\Desktop\store-dataset.xlsx')
    predict_year_month = pd.datetime(yearSelected,monthSelected,1)
    data_sub = data[(data['Order Date']<predict_year_month) & (data['Sub-Category']==sub_category_selected)]
    
    input_features = data_sub[['Order Date', 'Sales', 'Profit']]
    input_features.sort_values(by = ['Order Date'])
    input_features['Order Date'] = pd.to_datetime(input_features['Order Date'])
    input_features = input_features.reset_index(drop=True)
    input_features.index = input_features['Order Date']
    input_features = input_features.drop(['Order Date'])
    
    input_features_month = input_features.resample('M').sum()
    
    monthly_sales = input_features_month['Sales']
    monthly_profit = input_features_month['Profit']
    
    predicted_profit_regressor = linear_model.LinearRegression()
    predicted_profit_regressor.fit(monthly_sales.values.reshape(-1,1),monthly_profit.values.reshape(-1,1))
    
    length_of_input_feature_month = len(input_features_month)
    input_sales_list = list(range(length_of_input_feature_month))
    input_sales_series = pd.Series(input_sales_list)
    predicted_sale_regressor = linear_model.LinearRegression()
    predicted_sale_regressor.fit(input_sales_series.values.reshape(-1,1),monthly_sales.values.reshape(-1,1))
    
    predicted_sales = predicted_sale_regressor.predict(length_of_input_feature_month+1)
    predicted_profit = predicted_profit_regressor.predict(predicted_sales)
    #plt.scatter(sub_category_selected,)
    #plt.plot(monthly_sales,predicted_sales)
    #plt.show()
    #predictedSalesText.set(str(round(predicted_sales,2)))
    #predictedProfitText.set(str(round(predicted_profit,2)))
    predictedSalesText = tk.Label(root,text=str(round(predicted_sales[0][0],2)))
    predictedProfitText = tk.Label(root,text=str(round(predicted_profit[0][0],2)))
    predictedSalesText.place(relx=0.25, rely=0.33)
    predictedProfitText.place(relx=0.5, rely=0.33)
    
    f1 = plt.figure()
    plt.plot(input_features_month['Sales'][0:-2],'yo-')
    plt.xticks(rotation=90)
    plt.xlabel('Month')
    plt.ylabel('Sales in USD')
    plt.title('Actual Sales of '+str(sub_category_selected))
    plt.show()
    
    canvas = FigureCanvasTkAgg(f1,root)
    canvas.show()
    canvas.get_tk_widget().place(relx=0.03,rely=0.45)
    
    f2 = plt.figure()
    plt.plot(input_features_month['Profit'][0:-2],'go-')
    #plt.xticks(rotation=90)
    plt.xlabel('Month')
    plt.ylabel('Profit in USD')
    plt.title('Actual Profit of '+str(sub_category_selected))
    plt.show()
    """f2 = Figure(figsize=(4,3), dpi=100)
    b = f2.add_subplot(111)
    b.plot(input_features_month['Profit'][0:-2],'go-')
    #b.xticks(rotation=90)
    #b.xlabel('Month')
    #b.ylabel('Profit in USD')
    #b.title('Actual Profit of '+str(sub_category_selected))
    #b.show()"""
   
    canvas = FigureCanvasTkAgg(f2,root)
    canvas.show()
    canvas.get_tk_widget().place(relx=0.52,rely=0.45)
    
predictSalesProfitButton = tk.Button(root, text = 'Predict Sales and Profit', command = getSalesProfit)
predictSalesProfitButton.place(relx=0.8,rely=0.13)


root.mainloop()
# =============================================================================
# 
# 
# 
# 
# 
# # -*- coding: utf-8 -*-
# """
# Created on Fri May  4 17:03:47 2018
# 
# @author: user
# """
# 
# # The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# # License: http://creativecommons.org/licenses/by-sa/3.0/	
# 
# import matplotlib
# matplotlib.use("TkAgg")
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# from matplotlib.figure import Figure
# 
# import tkinter as tk
# from tkinter import ttk
# 
# 
# LARGE_FONT= ("Verdana", 12)
# 
# 
# class SeaofBTCapp(tk.Tk):
# 
#     def __init__(self, *args, **kwargs):
#         
#         tk.Tk.__init__(self, *args, **kwargs)
# 
#         tk.Tk.iconbitmap(self)#, default="clienticon.ico")
#         tk.Tk.wm_title(self, "Sea of BTC client")
#         
#         
#         container = tk.Frame(self)
#         container.pack(side="top", fill="both", expand = True)
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)
# 
#         self.frames = {}
# 
#         for F in (StartPage, PageOne, PageTwo, PageThree):
# 
#             frame = F(container, self)
# 
#             self.frames[F] = frame
# 
#             frame.grid(row=0, column=0, sticky="nse
# class PageThree(tk.Frame):
# 
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
#         label.pack(pady=10,padx=10)
# 
#         button1 = ttk.Button(self, text="Back to Home",
#                             command=lambda: controller.show_frame(StartPage))
#         button1.pack()
# 
#         f = Figure(figsize=(5,5), dpi=100)
#         a = f.add_subplot(111)
#         a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
# 
#         
# 
#         canvas = FigureCanvasTkAgg(f, self)
#         canvas.show()
#         canvas.get_tk_widget().place(relx=0.1,rely=0.1)
#         #canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
# 
#         toolbar = NavigationToolbar2TkAgg(canvas, self)
#         toolbar.update()
#         canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
# 
#         
# 
# app = SeaofBTCapp()
# app.mainloop()
# =============================================================================
