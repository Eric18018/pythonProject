import matplotlib.pyplot as plt
import numpy as np


# 创建简易的市场模型
def simpmarket(win_rate, play_cnt=1000, stock_num=9, position=0.01, commission=0.01, lever=False):
    my_money = np.zeros(play_cnt)
    my_money[0] = 1000  # 初始资金
    once_chip = my_money[0] * position  # 初始仓位
    lose_count = 1
    binomial = np.random.binomial(stock_num, win_rate, play_cnt)  # 伯努利分布
    for i in range(1, play_cnt):
        if binomial[i] > stock_num // 2:
            my_money[i] = my_money[i - 1] + once_chip if lever == False else my_money[i - 1] + once_chip * lose_count
            lose_count = 1
        else:
            my_money[i] = my_money[i - 1] - once_chip if lever == False else my_money[i - 1] - once_chip * lose_count
            lose_count += 1
        my_money[i] -= commission
        if my_money[i] <= 0:
            break
    return my_money

#创建简易的市场模型应用仓位管理
def positmanage(play_cnt=1000, stock_num=9, commission=0.01):
    my_money = np.zeros(play_cnt)
    my_money[0] = 1000

    for i in range(1, play_cnt):
        win_rate = np.random.random(size=1)#生成[0,1)之间的浮点数
        binomial = np.random.binomial(stock_num, win_rate, 1)
        once_chip = my_money[0] * win_rate * 0.1

        if binomial > stock_num//2:
            my_money[i] = my_money[i-1] + once_chip
        else:
            my_money[i] = my_money[i-1] - once_chip
        my_money[i] -= commission
        if my_money[i] <= 0:
            break
    return my_money


if __name__ == '__main__':
    trader = 50
    # _ = [plt.plot(np.arange(1000), simpmarket(0.5, play_cnt=1000, stock_num=9, commission=0), alpha=0.6)
    #      for _ in np.arange(0, trader)]
    # _ = plt.hist([simpmarket(0.5, play_cnt=1000, stock_num=9, commission=0)[-1]
    #               for _ in np.arange(0, trader)], bins=30)

    # 概率50% 手续费0.01 参加500000次
    # _ = [plt.plot(np.arange(500000), simpmarket(0.5, play_cnt=500000, stock_num=9, commission=0.01), alpha=0.6) \
    #      for _ in np.arange(0, trader)]
    # _ = plt.hist([simpmarket(0.5, play_cnt=500000, stock_num=9, commission=0.01)[-1]
    #               for _ in np.arange(0, trader)], bins=30)

    # 仓位管理 手续费0.01 参加1000次
    _ = [plt.plot(np.arange(1000), positmanage(play_cnt=1000, stock_num=9, commission=0.01), alpha=0.6)
         for _ in np.arange(0, trader)]
    _ = plt.hist([positmanage(play_cnt=1000, stock_num=9, commission=0)[-1]
                  for _ in np.arange(0, trader)], bins=30)

    plt.show()
