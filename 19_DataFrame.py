import pandas_datareader.data as web
import datetime


def record():
    df_stock = web.DataReader("000001.SS", "yahoo", datetime.datetime(2018, 1, 1), datetime.datetime(2018, 2, 1))
    # 查看前几行
    print(df_stock.head(10))
    # 行索引
    print(df_stock.index)
    # 列索引
    print(df_stock.columns)
    # 行+列索引
    print(df_stock.axes)
    # 访问全部元素数值
    print(df_stock.values)
    # 访问某列内容
    print(df_stock.Open)
    # 访问某行内容
    print(df_stock[0:2])
    # loc的选取规则：通过行和列标签组合的方式来选择数据，以逗号来区分行和列的指定，前半部分参数为指定行标签，后半部分参数指定为列标签，冒号指定了行或者列选取的范围
    print(df_stock.loc['2018-01-02', ['High', 'Low']])
    print(df_stock.loc[['2018-01-02', '2018-01-04'], ['High', 'Low']])
    print(df_stock.loc[df_stock.index[[0, 2]], ['High', 'Low']])
    # iloc的选取规则：通过行和列位置组合的方式来选择数据
    print(df_stock.iloc[[0, 2], [0, 1]])
    print(df_stock.iloc[[0, 2], df_stock.columns.get_loc('High')])
    print(df_stock.iloc[[0, 2], df_stock.columns.get_indexer(['High', 'Open'])])


if __name__ == '__main__':
    # record()
    df_stockload = web.DataReader("000001.SS", "yahoo", datetime.datetime(2018, 1, 1), datetime.datetime(2018, 2, 1))
    print(df_stockload[0:])
    print(df_stockload.describe().loc['mean']['High'])
    # 选取条件是'High'列中数值大于平均值所对应的行，列的选取为全部列的元素。
    print(df_stockload.iloc[[i for i in range(len(df_stockload.values)) if
                             df_stockload.High[i] > df_stockload.describe().loc['mean']['High']], 0:])
