import pandas as pd

df = pd.read_csv('taxi_table.csv', sep = ';')

#print(df.info(all))
#print(df.head(25))

#Найти совокупную сумму чаевых топ-5 поездок
sum_tip = df.sort_values('tip', ascending = False).head(5)
print(sum_tip['tip'])

#Какова доля пошлин(tools) в общем объеме рынка(total). Ответ выразить в %
sum_tolls = df['tolls'].sum()
sum_total = df['total'].sum()
print(sum_tolls)
print(sum_total)
print(sum_tolls / sum_total * 100)

#Кто больше(в среднем) оставляет чаевых:
#    те кто рассплачивается банкавкими картами, или те, кто расплачивается наличными
count_cash = df['payment'].value_counts()
print(count_cash)


#Сколько секунд заняла самая длинная поездка
df['pickup'] = pd.to_datetime(df['pickup'])
df['dropoff'] = pd.to_datetime(df['dropoff'])
start = df['pickup']
end = df['dropoff']
sum_count = end - start
print(sum_count.max())

#Поездки из какого аэрапорта в среднем дороже?
fls = df.loc[df['pickup_zone'].fillna('').str.contains('Airport')]
print(fls.groupby('pickup_zone')['fare'].mean())