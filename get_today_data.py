import tushare as ts
import os
import time

df = ts.get_today_all()

filename = 'stock_daily/' + time.strftime("%Y-%m-%d") + '.csv'
#直接保存
df.to_csv(filename)
#选择保存
df.to_csv(filename,columns=['open','high','low','close'])
