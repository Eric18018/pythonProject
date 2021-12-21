import random
import matplotlib.pyplot as plt
import numpy as np
from timeit import timeit
import pandas as pd

if __name__ == '__main__':
    # 生成日时间序列
    dd = pd.date_range('2010-01-01', freq='D', periods=1000)
    stock_data = np.random.normal(loc=10.0, scale=1.0, size=1000)
    pct_change = np.around((stock_data - np.roll(stock_data, 1)) / np.roll(stock_data, 1), 2)
    pct_change[0] = np.nan
    df_stock = pd.DataFrame({'close': stock_data, 'price range': pct_change}, index=dd)
    print(f'股价交易数据：\n {df_stock.head()}')  # 打印前5行数据
    # 绘制收盘价
    df_stock.close[100:150].plot(c='m')
    plt.legend(['Close'], loc='best')
    plt.show()

