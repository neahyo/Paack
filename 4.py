#__________ Could you provide a code that executes the query you have created previously in question 6 of SQL and export the result to a CSV?

import pandas as pd
orders = pd.read_csv('orders_table.csv')
drivers = pd.read_csv('drivers_table.csv')

df = drivers.merge(orders, how = 'left', left_on = 'id', right_on= 'driver_id')
df.head()
df['time_hour'] = pd.to_datetime(df['Attempted time']).dt.hour
a = df.groupby(['driver_id','driver', 'time_hour']).agg({'Paack order number': 'nunique'})
a = a.rename(columns={'Paack order number':'Productivity(number of orders attempted per hour of the day)'})
a.to_csv('productivity.csv')
