
if __name__ == '__main__':
    import numpy as np
    import pandas as pd

    a = np.random.randint(1000, size=36).reshape(12,3)
    index = ['%d月'%x for x in range(1,13)]
    print(index)
    print(a)
    df = pd.DataFrame(a, index=index, columns=['部门1', '部门2'])
    print(df)