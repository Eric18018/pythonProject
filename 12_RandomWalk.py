import matplotlib.pyplot as plt
import numpy as np


def random_walk(nsteps=1000):
    draws = np.random.randint(0, 2, size=nsteps)
    print(f'random walk direction is {draws}')  # random walk direction is [1 0 1 ... 0 1 0]
    steps = np.where(draws > 0, 1, -1)  # 将0转换为-1
    walk = steps.cumsum()  # 累加方式记录轨迹
    return walk


# 多样本随机漫步轨迹-plot
def simple_random_walk():
    # 正常显示画图时出现的中文和负号
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    _ = [plt.plot(np.arange(2000), random_walk(nsteps=2000), c='b', alpha=0.05) for _ in np.arange(0, 1000)]
    plt.xlabel('游走步数')
    plt.ylabel('分布轨迹')
    plt.title(u"模拟随机漫步")
    plt.show()


if __name__ == '__main__':
    simple_random_walk()
