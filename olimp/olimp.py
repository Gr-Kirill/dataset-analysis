import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv('olim.csv', sep = ';')

df.columns = [x.lower() for x in df.columns.tolist()]

# print(df.info())
# print(df.describe(include = 'all'))
# print(df)

#Вид спорта, где было самое большое число уникальных победителей
df_gold = df[df['medal'] == 'Gold']
df_ans = df_gold.groupby('sport').agg({'team' : 'nunique'}).sort_values('team', ascending = False)
print(df_ans)


#Самые сильные виды спорта, для сборных Китая и США
df_gold = df[df['medal'] == 'Gold']
df_CHN = df_gold[df_gold['noc'] == 'CHN'].reset_index() 
df_USA = df_gold[df_gold['noc'] == 'USA'].reset_index()

df_ans_CHN = df_CHN.groupby('sport').agg({'name':'count'}).sort_values('name', ascending = False)
df_ans_USA = df_USA.groupby('sport').agg({'name':'count'}).sort_values('name', ascending = False)
print(df_ans_CHN)
print(df_ans_USA)

#Странa, у которой доля отправленных спортсменов, завоевавших золотые медали является максимальной?
df_gold = df[df['medal'] == 'Gold'] 
df_gold_country = df_gold.groupby('team').agg({'medal' : 'count'})

df_gold_ans = df_gold.groupby('team').agg({'name' : 'nunique'}).sort_values('name', ascending = False)
df_all_ans = df.groupby('team').agg({'name' : 'nunique'}).sort_values('name', ascending = False)
# print(df_all_ans)
# print(df_gold_ans)

df = pd.merge(df, df_all_ans, how = 'left', on = 'team')
df = pd.merge(df, df_gold_ans, how = 'left', on = 'team')
df = pd.merge(df, df_gold_country, how = 'left', on = 'team')

res = df[df['medal_y'] > 50]
res['ans'] = (res['name'] / res['name_y'])*100
res.sort_values('ans', ascending = False, inplace = True)

print(res['team'])

#Фамилия самого титулованного спортсмена
df_cool = df.groupby('name').agg({'medal' : 'count'}).sort_values('medal', ascending = False)
print(df_cool)

#Максимальная разница в возрасте
df = df[df['medal'] == 'Gold'] 
df = df.dropna(subset = ['age'])

df_age_min = df.groupby(['team', 'games']).agg({'age' : 'min'})
df_age_max = df.groupby(['team', 'games']).agg({'age' : 'max'})
# print(df_age_min)
# print(df_age_max)

df = pd.merge(df, df_age_max, how = 'left', on = ['team', 'games'])
df = pd.merge(df, df_age_min, how = 'left', on = ['team', 'games'])

df['res']= (df['age_y'] - df['age']).max()
print(df)