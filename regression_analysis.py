import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import xlrd
import numpy as np

data=pd.read_excel('data_music.xls',index_col='index')

#一共128个特征
datanum=128

#放置相关系数
relation_coefficient=[]
for i in range(0,datanum):
    i=str(i)
    y=data['like']
    x=data["特征"+i] # 线性回归拟合
    print(y)
    print(x)
    x_n = sm.add_constant(x) #statsmodels进行回归时，一定要添加此常数项
    model = sm.OLS(y.astype(float), x_n.astype(float)) #model是回归分析模型
    results = model.fit() #results是回归分析后的结果

    #输出回归分析的结果
    print(results.summary())
    print('Parameters: ', results.params)#两个参数分别是斜率和截距
    print('R2: ', results.rsquared)
    relation_coefficient.append(results.rsquared)
   
    if(i=='3'):
		# #以下用于画回归直线图
        plt.figure()
        plt.rcParams['font.sans-serif'] = ['Kaiti']
    # # 指定默认字体
        plt.title(u"线性回归预测点赞数和特征"+i+"的关系")
        plt.xlabel(u"特征"+i)
        plt.ylabel(u"点赞数")
        #plt.axis([50, 200, 0, 1000000])
        # plt.scatter(x, y, marker="o",color="b", s=10)
        plt.scatter(x,data['like'],s=10)
        # plt.plot(x_n, y, linewidth=3, color="r")
        plt.plot(x,results.params[0]+results.params[1]*x,'r')
        plt.show()
#以下用于画相关系数的图
data=pd.DataFrame({'r2':relation_coefficient,'feature':[j for j in range(0,datanum)]})
plt.figure()
plt.rcParams['font.sans-serif'] = ['Kaiti']
plt.title(u'线性回归预测128个特征的相关系数图')
plt.xlabel(u"特征序号")
plt.ylabel(u"相关系数R^2")
plt.scatter(data['feature'],data['r2'],s=10)
plt.show()