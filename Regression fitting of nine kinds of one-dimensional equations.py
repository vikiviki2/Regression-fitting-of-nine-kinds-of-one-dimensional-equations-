# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 10:23:50 2022

@author: Viki
"""

def analysis_of_regression(data_df,x_自变量,y_因变量,fw,io_1):     
    import matplotlib.pyplot as plt
    
    import pandas as pd
    from sklearn.metrics import r2_score
    plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
    
    #%%需要外部加载的变量
    
    
    # df_a = pd.DataFrame( columns=['标签','类型', 'r2', '航司','公式']) 
    df_a = pd.DataFrame() 
    df_d = pd.DataFrame(columns=('标签','类型','r2','系数'))
    
    
  
    data_array = np.array(data_df[['标签']])
    b=data_array.tolist()
    a=[x for tup in b for x in tup]
 
    a = list(set(a))
    
    
    #开始进行函数拟合
    for i in a:    
    # for i in [1]:
        jj=data_df[(data_df['标签']==i)]
        # jj=data_df
        ##线性
        x_cz_2=jj[['自变量']].values.tolist()
        y_cz_2=jj[['因变量']].values.tolist()
        x_cz_2=sum(x_cz_2,[])
        y_cz_2=sum(y_cz_2,[])
        L=np.polyfit(x_cz_2, y_cz_2, 1)
        print(L)
        Z=np.polyval(L,x_cz_2,)
        score = r2_score(y_cz_2, Z, multioutput='raw_values')
        print('线性：'+str(score))
        new=pd.DataFrame({'标签':i,
                          '类型':'线性',
                          'r2':score,
                          '系数':[L]})
        
        df_d=df_d.append(new,ignore_index=(True))
        
        
        ##指数
        x_cz_2=jj[['自变量']].values.tolist()
        y_cz_2=jj[['因变量']].values.tolist()
        x_cz_2=sum(x_cz_2,[])
        y_cz_2=sum(y_cz_2,[])
        L=np.polyfit(x_cz_2, np.log(y_cz_2), 1)
        Z=np.polyval(L,x_cz_2)
        true=np.exp(Z)
        score = r2_score(y_cz_2,true, multioutput='raw_values')
        print('指数：'+str(score))
        new=pd.DataFrame({'标签':i,
                          '类型':'指数',
                          'r2':score,
                          '系数':[L]})
        
        df_d=df_d.append(new,ignore_index=(True))
        
        
        
        
        # ##二次
        # x_cz_2=jj[['自变量']].values.tolist()
        # y_cz_2=jj[['因变量']].values.tolist()
        # x_cz_2=sum(x_cz_2,[])
        # y_cz_2=sum(y_cz_2,[])
        # L=np.polyfit(x_cz_2, y_cz_2, 2)
        # print(L)
        # Z=np.polyval(L,x_cz_2,)
        # score = r2_score(y_cz_2, Z, multioutput='raw_values')
        # print('二次：'+str(score))
        
        # new=pd.DataFrame({'标签':i,
        #                   '类型':'二次',
        #                   'r2':score,
        #                   '系数':[L]})
        
        # df_d=df_d.append(new,ignore_index=(True))
        
        
        ##幂函数
        x_cz_2=jj[['自变量']].values.tolist()
        y_cz_2=jj[['因变量']].values.tolist()
        x_cz_2=sum(x_cz_2,[])
        y_cz_2=sum(y_cz_2,[])
        L=np.polyfit(np.log(x_cz_2), np.log(y_cz_2), 1)
        Z=np.polyval(L,np.log(x_cz_2))
        true=np.exp(Z)
        score = r2_score(y_cz_2,true, multioutput='raw_values')
        print('幂函数：'+str(score))
        
        new=pd.DataFrame({'标签':i,
                          '类型':'幂函数',
                          'r2':score,
                          '系数':[L]})
        
        df_d=df_d.append(new,ignore_index=(True))
    
        ##对数
        x_cz_2=jj[['自变量']].values.tolist()
        y_cz_2=jj[['因变量']].values.tolist()
        x_cz_2=sum(x_cz_2,[])
        y_cz_2=sum(y_cz_2,[])
        L=np.polyfit(np.log(x_cz_2), y_cz_2, 1)
        Z=np.polyval(L,np.log(x_cz_2))
        score = r2_score(y_cz_2,Z, multioutput='raw_values')
        print('对数：'+str(score))
        
        new=pd.DataFrame({'标签':i,
                          '类型':'对数',
                          'r2':score,
                          '系数':[L]})
        
        df_d=df_d.append(new,ignore_index=(True))
    
    
        ##复合函数
        x_cz_2=jj[['自变量']].values.tolist()
        y_cz_2=jj[['因变量']].values.tolist()
        x_cz_2=sum(x_cz_2,[])
        y_cz_2=sum(y_cz_2,[])
        L=np.polyfit(x_cz_2,np.log(y_cz_2), 1)
        Z=np.polyval(L,x_cz_2)
        true=np.exp(Z)
        score = r2_score(y_cz_2,true, multioutput='raw_values')
        print('复合函数：'+str(score))
        
        new=pd.DataFrame({'标签':i,
                          '类型':'复合函数',
                          'r2':score,
                          '系数':[L]})
        
        df_d=df_d.append(new,ignore_index=(True))
        
        ##生长
        x_cz_2=jj[['自变量']].values.tolist()
        y_cz_2=jj[['因变量']].values.tolist()
        x_cz_2=sum(x_cz_2,[])
        y_cz_2=sum(y_cz_2,[])
        L=np.polyfit(x_cz_2, np.log(y_cz_2), 1)
        Z=np.polyval(L,x_cz_2)
        true=np.exp(Z)
        score = r2_score(y_cz_2,true, multioutput='raw_values')
        print('生长：'+str(score))
        
        new=pd.DataFrame({'标签':i,
                          '类型':'生长',
                          'r2':score,
                          '系数':[L]})
        
        df_d=df_d.append(new,ignore_index=(True))
        
        # ##三次
        # x_cz_2=jj[['自变量']].values.tolist()
        # y_cz_2=jj[['因变量']].values.tolist()
        # x_cz_2=sum(x_cz_2,[])
        # y_cz_2=sum(y_cz_2,[])
        # L=np.polyfit(x_cz_2, y_cz_2, deg=3)
        # Z=np.polyval(L,x_cz_2)
        # score = r2_score(y_cz_2,Z,multioutput='raw_values')
        # print('三次：'+str(score))
        
        # new=pd.DataFrame({'标签':i,
        #                   '类型':'三次',
        #                   'r2':score,
        #                   '系数':[L]})
        
        # df_d=df_d.append(new,ignore_index=(True))
        
        # ##S函数
        # x_cz_2=jj[['自变量']].values.tolist()
        # y_cz_2=jj[['因变量']].values.tolist()
        # x_cz_2=sum(x_cz_2,[])
        # x_cz_3 = [1/x for x in x_cz_2]
        # y_cz_2=sum(y_cz_2,[])
        # L=np.polyfit(x_cz_3, np.log(y_cz_2), 1)
        # Z=np.polyval(L,x_cz_3)
        # true=np.exp(Z)
        # score = r2_score(y_cz_2,true,multioutput='raw_values')
        # print('S函数：'+str(score))
        
        # new=pd.DataFrame({'标签':i,
        #                   '类型':'S函数',
        #                   'r2':score,
        #                   '系数':[L]})
        
        # df_d=df_d.append(new,ignore_index=(True))
        
        ##逆函数
        x_cz_2=jj[['自变量']].values.tolist()
        y_cz_2=jj[['因变量']].values.tolist()
        x_cz_2=sum(x_cz_2,[])
        x_cz_3 = [1/x for x in x_cz_2]
        y_cz_2=sum(y_cz_2,[])
        L=np.polyfit(x_cz_3, y_cz_2, 1)
        Z=np.polyval(L,x_cz_3)
        score = r2_score(y_cz_2,true,multioutput='raw_values')
        print('逆函数：'+str(score))
        
        new=pd.DataFrame({'标签':i,
                          '类型':'逆函数',
                          'r2':score,
                          '系数':[L]})
        
        df_d=df_d.append(new,ignore_index=(True))
    
    df_zh=df_d.sort_values('r2', ascending=False).groupby('标签', as_index=False).first()
    
 
    
    ff=df_zh
    # second=df_e[(df_e['类型']=='二次')]
    j=0
    while  j < len(a):
        gg=ff.iloc[[j]].values.tolist()
        gg =sum(gg,[]) 
        
   
        if gg[1] == '二次':
            x=fw
            y_sh=gg[3][0]*x**2+gg[3][1]*x+gg[3][2]
            formu_s='y='+str(gg[3][0])+str('x^2+')+str(gg[3][1])+str('x')+str('+(')+str(gg[3][2])+str(')')
        elif gg[1] == '线性':
            x=fw
            y_sh=gg[3][0]*x+gg[3][1]
            formu_s='y_zh='+str(gg[3][0])+str('x')+str('+(')+str(gg[3][1])+str(')')
        elif gg[1] == '指数':
            x=fw
            y_sh=np.exp(gg[3][0]*x+gg[3][1])
            formu_s='y='+str(np.exp(gg[3][1]))+str('e')+'^'+str(gg[3][0]) +'x'
        elif gg[1] == '幂函数':
            x=fw
            y_sh=np.exp(gg[3][1]+(np.log(x)*gg[3][0]))   
            formu_s='y='+str(np.exp(gg[3][1]))+str('x')+'^'+str(gg[3][0])
        elif gg[1] == '对数':
            x=fw
            y_sh=gg[3][1]+(np.log(x)*gg[3][0])  
            formu_s='y='+str(gg[3][1])+'+'+str(gg[3][0])+'In(x)'      
        elif gg[1] == '生长':
            x=fw
            y_sh=np.exp(gg[3][0]*x+gg[3][1])   
            formu_s='y='+'e^('+str(gg[3][0])+str('x')+str('+(')+str(gg[3][1])+str('))')     
        elif gg[1] == '三次':
            x=fw
            y_sh=gg[3][0]*x**3+gg[3][1]*x**2+gg[3][2]*x+gg[3][3]
            formu_s='y='+str(gg[3][0])+str('x^3+')+str(gg[3][1])+str('x^2+')+str(gg[3][2])+str('x')+str('+(')+str(gg[3][3])+str(')')
        elif gg[1] == 'S函数':
            x=fw
            y_sh=np.exp(gg[3][0]*(x)**(-1)+gg[3][1])   
            formu_s='y='+'e^('+str(gg[3][0])+str('(1/x)')+str('+(')+str(gg[3][1])+str('))')          
        elif gg[1] == '逆函数':
            x=fw
            y_sh=gg[3][0]*(x)**(-1)+gg[3][1]   
            formu_s='y='+str(gg[3][0])+str('(1/x)')+str('+(')+str(gg[3][1])+str(')')
        elif gg[1] == '复合函数':
            x=fw
            y_sh=np.exp(gg[3][1]+(gg[3][0]*x))   
            formu_s='y='+str(np.exp(gg[3][1])) +'*'+str(np.exp(gg[3][0])) +'^x'       
        gg.append(formu_s)
        del gg[3]
        gg=[gg]
        
        df_a=df_a.append(gg,ignore_index=(True))
        
        
        
     
        # if gg[1] == '二次':
        #     x=np.arange(0.15,0.4,0.002)
        #     y_nh=gg[3][0]*x**2+gg[3][1]*x+gg[3][2]-x
        #     formu_n='y_cz='+str(gg[3][0])+str('x^2+')+str(gg[3][1])+str('x')+str('+(')+str(gg[3][2])+str(')')+'-x'
        # elif gg[1] == '线性':
        #     x=np.arange(0.15,0.4,0.002)
        #     y_nh=gg[3][0]*x+gg[3][1]-x
        #     formu_n='y_cz='+str(gg[3][0])+str('x')+str('+(')+str(gg[3][1])+str(')')+'-x'
        # elif gg[1] == '指数':
        #     x=np.arange(0.15,0.4,0.002)
        #     y_nh=np.exp(gg[3][0]*x+np.log(gg[3][1]))-x
        #     # formu=str(gg[3][0])+str('x')+str('+(')+str(gg[3][1])+str(')')    
        # else :
        #     x=np.arange(0.15,0.4,0.002)
        #     y_nh=np.exp(gg[3][0]*x+np.log(gg[3][1])) -x
        
        # if gg[5] == '二次':
        #     x=np.arange(0.15,0.4,0.002)
        #     y_sh=gg[7][0]*x**2+gg[7][1]*x+gg[7][2] -x
        #     formu_s='y_zh='+str(gg[7][0])+str('x^2+')+str(gg[7][1])+str('x')+str('+(')+str(gg[7][2])+str(')')+'-x'
        # elif gg[5] == '线性':
        #     x=np.arange(0.15,0.4,0.002)
        #     y_sh=gg[7][0]*x+gg[7][1] -x
        #     formu_s='y_zh='+str(gg[7][0])+str('x')+str('+(')+str(gg[7][1])+str(')')+'-x'
        # elif gg[5] == '指数':
        #     x=np.arange(0.15,0.4,0.002)
        #     y_sh=np.exp(gg[7][0]*x+np.log(gg[7][1])) -x 
        # else :
        #     x=np.arange(0.15,0.4,0.002)
        #     y_sh=np.exp(ff[7][0]*x+np.log(ff[7][1])) -x
        
        
        
        
        
        
        
        
        
        # fig11=plt.figure(num=11,figsize=(20,17))
        # ax11=fig11.add_subplot(111)
        #调整保存图片的大小
        plt.figure(figsize=(20, 15))
        
        plt.plot(x,y_sh,'r-.o',label=y_因变量+formu_s+'  r2='+str(gg[0][2]),linewidth=0.05)
        
        
        plt.tick_params(labelsize=23)
        
        plt.xlabel(x_自变量,fontsize=40)
        
        plt.ylabel(y_因变量,fontsize=40)
        
        
        
        
        plt.title(str(gg[0][0])+'--'+x_自变量+'&'+y_因变量,fontsize=40) #要用plt调动title
        
        plt.legend(fontsize=30)
    
    
    
    
        x2=data_df[(data_df['标签']==gg[0][0])][['自变量']]
        y2=data_df[(data_df['标签']==gg[0][0])][['因变量']]
        
       
        colors2 = '#DC143C'
        area = np.pi * 6**2.7  # 点面积 
        # 画散点图
        plt.scatter(x2, y2, s=area, c=colors2, alpha=0.5)
        plt.savefig('')
        
        
        plt.savefig(io_1+'/%s.jpg'%(gg[0][0]), bbox_inches='tight')
        plt.show()
        # plt.close()
        j=j+1
        if j > len(a)-1:    
            break
    df_a.columns= ['标签','类型', 'r2','公式'] 
    return df_a
————————————————
版权声明：本文为CSDN博主「viki viki」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/viki_2/article/details/121948864