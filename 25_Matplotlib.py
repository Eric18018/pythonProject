import matplotlib.pyplot as plt
import pandas_datareader.data as web
import datetime
import mplfinance as mpf

if __name__ == '__main__':

    df_stockload = web.DataReader("600797.SS", "yahoo", datetime.datetime(2018, 1, 1), datetime.datetime(2018, 3, 1))
    print(df_stockload.info())

    mpf.plot(df_stockload, type='candle', mav=(2, 5, 10), volume=True)

    # fig = plt.figure(figsize=(8, 6), dpi=100, facecolor="white")  # 创建fig对象
    # fig.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    # graph_KAV = fig.add_subplot(1, 1, 1)  # 创建子图
    # mpf.candlestick2_ochl(graph_KAV, df_stockload.Open, df_stockload.Close, df_stockload.High, df_stockload.Low,
    #                       width=0.5, colorup='r', colordown='g')  # 绘制K线走势
