import pandas as pd
import tushare as ts

if __name__ == '__main__':
    # 分时数据接口暂不能用
    df_tick = ts.get_tick_data('002372', date='2020-01-23', src='tt')
    df_tick.index = pd.to_datetime(df_tick.time)
    df_tick.drop(axis=1, columns='time', inplace=True)
    print(df_tick[2000:2010])
