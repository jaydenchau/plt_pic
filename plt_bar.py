import random
import string

VERIFY_CODE_EXPIRE_TIME = 10 * 60


# 生成n位随机数（纯数字）
def _gen_num(length):
    # 选中length个数字
    slc_num = [random.choice(string.digits) for _ in range(length)]
    # 打乱组合
    random.shuffle(slc_num)
    # 生成密码
    gen_pwd = ''.join([i for i in slc_num])
    return gen_pwd


def send_sms(mobile):
    code = _gen_num(6)
    # TODO: 待添加
    return True, code




if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import warnings

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    warnings.filterwarnings("ignore")
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    y1 = [102, 134, 154, 122, 143, 243, 355, 342, 276, 299, 241, 287]
    y2 = [102, 134, 154, 122, 143, 243, 355, 342, 276, 299, 241, 287]
    y3 = [100, 200, 300, 400, 500, 243, 355, 342, 276, 299, 241, 287]
    y2.sort()
    y3.sort()
    plt.figure(figsize=(15, 6))
    bar1 = plt.bar([i - 0.4 for i in x], y1, color='#9999ff', width=0.4, label='部门1')
    bar2 = plt.bar([i for i in x], y2, color='g', width=0.4, label='部门2')
    bar3 = plt.bar([i + 0.4 for i in x], y3, color='r', width=0.4, label='部门3')
    plt.xticks(x)
    # plt.xlim(-0.5, 11)
    # plt.ylim(0,10500)
    plt.title('Weight change in 15 months')
    plt.xlabel('Month')
    plt.ylabel('Number')
    plt.legend()    #增加图例(需要在bar里指定label)
    #  参数一是x轴坐标
    #  参数二是y轴坐标
    #  参数三是显示哪个轴的数据（字符串格式）
    #  verticalalignment：垂直对齐方式 ，参数：[ ‘center’ | ‘top’ | ‘bottom’ | ‘baseline’ ]
    #  horizontalalignment：水平对齐方式 ，参数：[ ‘center’ | ‘right’ | ‘left’ ]
    # for a, b in zip(x, y):  # 柱状图添加数据显示
    #     plt.text(a, b + 1.3, str(b), ha='center', va='bottom', fontsize=10.5)
    for rect in bar1:
        height = rect.get_height()  # 获得bar1的高度
        plt.text(rect.get_x() + rect.get_width() / 2, height + 3, str(height), ha="center", va="bottom")
    for rect in bar2:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height + 3, str(height), ha="center", va="bottom")
    for rect in bar3:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height + 3, str(height), ha="center", va="bottom")
    # plt.savefig('t_bar.png', dpi=300)
    plt.show()