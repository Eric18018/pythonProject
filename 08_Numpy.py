import random
import matplotlib.pyplot as plt
import numpy as np
from timeit import timeit

if __name__ == '__main__':

    def list_test():
        walk = []
        for _ in range(1000000):
            walk.append(random.normalvariate(0, 1))


    def ndarray_test():
        np.random.normal(loc=0.0, scale=1.0, size=1000000)


    # t1 = timeit('list_test()', 'from __main__ import list_test', number=1)
    # t2 = timeit('ndarray_test()', 'from __main__ import ndarray_test', number=1)
    #
    # print("list：{}".format(t1))
    # print("ndarray：{}".format(t2))

    # ======================================================================================

    stock_data = np.random.normal(loc=10.0, scale=1.0, size=1000)
    stock_data = np.around(stock_data, 2)
    # print("stock_data：\n {}".format(stock_data))

    # pct_change = np.around((stock_data - np.roll(stock_data, 1)) / np.roll(stock_data, 1), 2)
    # pct_change = (stock_data - np.roll(stock_data, 1)) / np.roll(stock_data, 1)
    # pct_change[0] = np.nan
    # print("pct_change：\n {}".format(pct_change))

    stock_data = np.random.normal(loc=10.0, scale=5.0, size=10)
    yes_data = np.random.normal(loc=10.0, scale=5.0, size=10)
    print(stock_data)
    print(yes_data)
    print(stock_data - yes_data)

