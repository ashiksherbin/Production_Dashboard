#does the processing on the data given
import pandas as pd
df=pd.read_csv("/content/data.csv")
df.head()

df['date'] = pd.to_datetime(df['work_date'], format='%m/%d/%Y')
df['work_date'] = df['date'].dt.strftime('%d/%m/%Y')

df=df.loc[:, df.columns != 'date']
year,month,date=[],[],[]
month_dict={'01':'Jan','02':'Feb','03':'Mar','04':'Apr','05':'May','06':'Jun','07':'Jul','08':'Aug','09':'Sep','10':'Oct','11':'Nov','12':'Dec'}
for i in df["work_date"]:
    idx=i.split("/")
    date.append(idx[0])
    month.append(month_dict[idx[1]])
    year.append(idx[2])
df['date']=date  
df['month']=month
df['year']=year

for i in df['Site Name'].unique():
  df['Site Name']=df['Site Name'].replace(i,i[-1])

for i in df['metric']:
  if i== 'Product A Produced':
    df['metric']=df['metric'].replace('Product A Produced','Production A')
  if i == 'Product B Produced':
    df['metric']=df['metric'].replace('Product B Produced','Production B')

df_new=df[['Site Name','city','metric','quantity','work_date','date','month'	,'year']]
df_new.to_csv('vizualization.csv')
