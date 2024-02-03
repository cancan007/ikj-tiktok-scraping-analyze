import numpy as np
import pandas as pd
import seaborn as sns
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import datetime
import os
import time

plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams["legend.framealpha"] = 1
plt.rcParams["font.family"] = 'Times New Roman'
plt.rcParams["mathtext.fontset"] = 'cm'
plt.rcParams["font.size"] = 13

dt_now = datetime.datetime.now()
dt_today=f"{dt_now.year}-{dt_now.month}-{dt_now.day}"
os.makedirs(f'{dt_today}/', exist_ok=True)


def calc_time(x):
    time=0
    arr=x.split('h')
    if(len(arr)>1 ):
        time+=float(arr[0])*60
        arr.pop(0)
        x=''.join(arr)
    
    arr=x.split('m')
    if(len(arr)>1 ):
        time+=float(arr[0])
        arr.pop(0)
        x=''.join(arr)
    
    arr=x.split('s')
    if(len(arr)>1):
        time+=float(arr[0])/60
    
    return time

def divide_time_area(t):
    h=t.hour
    if(0<=h<3):
        return 0
    if(3<=h<6):
        return 1
    if(6<=h<9):
        return 2
    if(9<=h<12):
        return 3
    if(12<=h<15):
        return 4
    if(15<=h<18):
        return 5
    if(18<=h<21):
        return 6
    if(21<=h):
        return 7

def get_plus_by_viewers(df):
    if(df['total_viewers']==0):
        return 0
    return df['plus_followers']/df['total_viewers']

def get_plus_by_time(df):
    if(df['time']==0):
        return 0
    return df['plus_followers']/df['time']

# 標準化したデータを読み込みます
data = pd.read_csv('../tiktok-scraping/data/tiktok-live-data.csv')
print(data['plus_followers'])
data['start_date_time']=pd.to_datetime(data['start_date_time'])
data['month'] = list(map(lambda x:x.month, data['start_date_time']))
data['week_day']=list(map(lambda x:x.weekday(), data['start_date_time']))
data['time_area']=list(map(divide_time_area, data['start_date_time']))
data['total_viewers']=list(map(lambda x:int(x.replace(',','')),data['total_viewers']))
#data['plus_followers']=list(map(lambda x:int(x.replace(',','')),data['plus_followers']))
data['reward']=list(map(lambda x:int(x.replace(',','')),data['reward']))
data['time']=list(map(calc_time, data['time']))
data['plus_by_viewers'] = data.apply(get_plus_by_viewers, axis=1)
data['plus_by_time'] = data.apply(get_plus_by_time, axis=1)
data=data.drop(['title','Unnamed: 0','start_date_time'],axis=1)
corr=data.corr() #各項目の相関度
print(corr)
print(np.mean(data['plus_followers'])) 

fig,ax=plt.subplots(figsize=(10,8))
sns.heatmap(corr,vmax=1,vmin=-1,center=0) #各項目の相関をヒートマップで視覚的にわかりやすく
plt.savefig(f'{dt_today}/corr-heatmap.png')


for w in ['plus_followers', 'plus_by_viewers', 'plus_by_time']:
    #四分位数でカラーわけ
    percentile=np.percentile(data[w], q=[0, 25, 50, 75])
    data.loc[data[w] > percentile[3] ,'color'] = 'blue'
    data.loc[(data[w] <= percentile[3]) & (data[w] > percentile[2]) ,'color'] = 'green'
    data.loc[(data[w] <= percentile[2]) & (data[w] > percentile[1]) ,'color'] = 'darkorange'
    data.loc[(data[w] <= percentile[1]) ,'color'] = 'red'
    #data.loc[data['plus_by_time'] <= percentile[0] ,'color'] = 'black'
    color=data['color']
    del data['color']
    plt.figure()
    plot=scatter_matrix(data,diagonal='density',color=color,figsize=(11,11))
    plt.suptitle(f'{dt_today}_{w}')
    plt.savefig(f'{dt_today}/scatter_matrix_color_{w}.png')
    
    for h in ['time_area', 'week_day']:
        #ヒストグラム作成(曜日)
        x1 = data[data[w] > percentile[3]][h]
        x2 = data[(data[w] <= percentile[3]) & (data[w] > percentile[2])][h]
        x3 = data[(data[w] <= percentile[2]) & (data[w] > percentile[1])][h]
        x4 = data[(data[w] <= percentile[1])][h]
        #x5 = data[data[w] <= percentile[0]][h]
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        ax.hist([x1, x2, x3 , x4 ], bins=8 if h == 'time_area' else data[h].nunique(), color=['blue', 'green', 'darkorange', 'red'], label=['Top 0~25%', 'Top 25~50%', 'Top 50~75%', 'Top 75~100%'], histtype='bar', stacked=True)
        ax.set_title(f'{dt_today} histogram {w} {h}')
        ax.set_xlabel(h)
        ax.set_ylabel('count')
        ax.legend(loc='upper left')
        plt.savefig(f'{dt_today}/hist_{w}_{h}.png')
    time.sleep(2)

print(data['time_area'].value_counts())