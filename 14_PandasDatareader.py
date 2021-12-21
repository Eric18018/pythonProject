import matplotlib.pyplot as plt
import pandas_datareader.data as web
import datetime

if __name__ == '__main__':

    # 获取上证指数的2017.1.1日至今的交易数据
    df_stockload = web.DataReader("000001.SS", "yahoo", datetime.datetime(2017, 1, 1), datetime.date.today())
    print(df_stockload.head())  # 查看前几行
    print(df_stockload.tail())  # 查看后几行
    print(df_stockload.columns)  # 查看列索引信息
    print(df_stockload.index)  #查看行索引信息
    print(df_stockload.shape)  # 查看形状
    print(df_stockload.describe())  # 查看各列数据描述性统计
    print(df_stockload.info())  # 查看缺失及每列数据类型
    # 绘制收盘价
    df_stockload.High.plot(c='b')
    plt.legend(['Close', '30ave', '60ave'], loc='best')
    plt.show()
