# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 10:23:59 2022

@author: Viki
"""

import pandas as pd
import numpy as  np
#需要加载的数据集
io=r'C:\Users\**\Desktop\测试集.xlsx'
data_df=pd.read_excel(io,sheet_name='测试数据集') 
x_自变量='自变量'
y_因变量='因变量'
io_1=r'C:\Users\**\Desktop\临时文件'
fw=np.arange(1,100,1)
 
 
answer=analysis_of_regression(data_df,x_自变量,y_因变量,fw,io_1)