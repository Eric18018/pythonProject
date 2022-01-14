import pandas_datareader.data as web
import datetime
import numpy as np
from timeit import timeit


# 循环遍历
def for_in_loop(df):
    df['signal1'] = 0  # df = df.assign(signal = 0)  #可采用assign新增一列
    for i in np.arange(0, df.shape[0]):
        df.iloc[i, df.columns.get_loc('signal1')] = np.sign(df.iloc[i]['Close'] - df.iloc[i]['Ma20'])
    return df


# 迭代器遍历方式
def iterrows_loop(df):
    df['signal2'] = 0  # df = df.assign(signal = 0)  #可采用assign新增一列
    for index, row in df.iterrows():
        df.loc[index, 'signal2'] = np.sign(row['Close'] - row['Ma20'])
    return df


# apply方法循环
def apply_loop(df):
    # apply()方法可将函数应用于dataframe特定行或列，lambda 为匿名函数，末尾包含axis参数，
    # 用来告知Pandas将函数运用于行（axis = 1）或者列（axis = 0）
    df['signal3'] = df.apply(lambda row: (np.sign(row['Close'] - row['Ma20'])), axis=1)
    print(df.head())


# Pandas series 的矢量化方式循环
def serious_loop(df):
    df['signal4'] = np.sign(df['Close'] - df['Ma20'])


# Numpy arrays的矢量化方式
def numpy_serious_loop(df):
    df['signal5'] = np.sign(df['Close'].values - df['Ma20'].values)


if __name__ == '__main__':
    # 获取上证指数交易数据 pandas-datareade模块data.DataReader()方法
    df_stock = web.DataReader("000001.SS", "yahoo", datetime.datetime(2018, 1, 1), datetime.datetime(2019, 1, 1))
    df_stock['Ma20'] = df_stock.Close.rolling(window=20).mean()  # 增加M20移动平均线
    df_stock.dropna(axis=0, how='any', inplace=True)  # NAN值删除,在第20个交易日时才能得到第一个Ma20移动平均线数值

    # 我们遍历全部交易日的收盘价数值和Ma20数值，将收盘价数值减去Ma20数值，并使用np.sign()取差值符号，
    # 当收盘价在Ma20上方时差值为正，收盘价在Ma20上下方时差值为负，由负转正对应为买点，由正转负对应为卖点
    def test1():
        for_in_loop(df_stock)


    def test2():
        iterrows_loop(df_stock)


    def test3():
        apply_loop(df_stock)


    def test4():
        serious_loop(df_stock)


    def test5():
        numpy_serious_loop(df_stock)


    # for..in循环迭代方式
    t1 = timeit('test1()', 'from __main__ import test1', number=100)
    # iterrows()遍历方式
    t2 = timeit('test2()', 'from __main__ import test2', number=100)
    # apply()方法循环方式
    t3 = timeit('test3()', 'from __main__ import test3', number=100)
    # Pandas series 的矢量化方式
    t4 = timeit('test4()', 'from __main__ import test4', number=100)
    # Numpy arrays的矢量化方式：
    t5 = timeit('test5()', 'from __main__ import test5', number=100)

    print(t1, t2, t3, t4, t5)
