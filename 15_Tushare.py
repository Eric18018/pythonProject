import datetime
import tushare as ts
import pandas as pd
import akshare as ak

if __name__ == '__main__':
    # df_sh1 = ts.get_hist_data('sh', start='2008-01-01', end=datetime.datetime.now().strftime('%Y-%m-%d'))
    # print(df_sh1.head())

    # get_k_data 返回2008年数据
    # df_sh2 = ts.get_k_data('sh', start='2008-01-01', end=datetime.datetime.now().strftime('%Y-%m-%d'))
    # df_sh2.index = pd.to_datetime(df_sh2.date)
    # df_sh2.drop(axis=1, columns='date', inplace=True)
    # print(df_sh2.head())

    # 设置token
    token = '988fc53106400636f5481f3369bbe936397a6e3791bd72acb604f49d'
    pro = ts.pro_api(token)  # 初始化pro接口
    # 获取平安银行日行情数据
    pa = pro.daily(ts_code='000001.SZ', start_date='20180101',end_date='20190101')
    print(pa.tail())

    pa.trade_date = pd.DatetimeIndex(pa.trade_date)
    pa.set_index("trade_date", drop=True, inplace=True)
    print(pa.tail())

    # 单次返回所有A股上市公司的实时行情数据
    # stock_df = ak.stock_zh_a_spot()
    # print(stock_df)

    # 单次返回具体某个A上市公司的所有历史行情数据
    stock_df = ak.stock_zh_a_daily(symbol="sh600000")
    print(stock_df)

