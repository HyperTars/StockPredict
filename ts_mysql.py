import tushare as ts
import MySQLdb
insert_sql = "INSERT INTO stock_5min_tick (code, tick, volume, open, close, high, low) VALUES ('%s', '%s', %s, %s, %s, %s, %s);"
def get_5min_tick(code):
    return ts.get_k_data(code,ktype = '5')

def write_5min_data(conn,data):
    cur = conn.cursor()
    for index, row in data.iterrows():
        row_tulpe = (row['code'],row['date'],row['volume'],row['open'],row['close'],row['high'],row['low'])
        wsql = insert_sql % row_tulpe
        try:
            cur.execute(wsql)
        except:
            pass;
    conn.commit()

def main():
    conn = MySQLdb.connect("addr","account","password","database" )
    stock_list = ts.get_stock_basics();
    for code,info in stock_list.iterrows():
        print "Trying:"+code
        print info
        for i in range(5):
            try:
                write_5min_data(conn,get_5min_tick(code));
                print "Written:"+code
                break;
            except:
                print "Retrying..."+code
    conn.close();    

if __name__=="__main__":
    main();
