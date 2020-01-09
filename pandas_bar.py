

if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    index = ['%d月'%x for x in range(1,13)]
    pd = pd.DataFrame(np.random.randint(1000, size=36).reshape(12,3),
                      index=index, columns=['部门1', '部门2', '部门3'])
    pd.plot(kind='bar', ylim=[0,1100], title='部门统计',  rot=0)
    plt.show()