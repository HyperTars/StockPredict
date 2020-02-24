import tushare as ts
import os
stock_code = input("Input Stock Need To Acquire:\n")
df = ts.get_hist_data(stock_code)

filename = 'stock_history/' + stock_code + '.csv'
#直接保存
df.to_csv(filename)

#选择保存
df.to_csv(filename ,columns=['open','high','low','close'])
