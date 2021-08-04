# 导入tkinter模块
import tkinter as tk
import threading
from time import sleep
from random import randint
from tkinter import messagebox

# 创建窗口对象
window = tk.Tk()
window.title('抽签')
# 窗口大小
window.minsize(800, 600)
# 将公司姓名放入列表中
name_list = ['公司1', '公司2', '公司3', '公司4', '公司5', '公司6',
             '公司7', '公司8', '公司9', '公司10', '公司11', '公司12',
             '公司13', '公司14', '公司15', '公司16', '公司17', '公司18']
winner = []
neiding = [0, 17, 1, 9, 13, 15]

# 创建一个空列表，用来放置做好的按钮
btn_list = []
# 循环遍历公司列表的长度
for i in range(len(name_list)):
    # 设置按钮，传入公司姓名作为按钮上显示的文本，设置字体，设置按钮颜色为白色
    button = tk.Button(window, text=name_list[i], font=('SimSun 15 bold'), bg='white')
    # 将按钮添加入按钮列表
    btn_list.append(button)
    # 按行摆放按钮，因为每行摆放6个，所以对6进行取商和余数。
    # 根据每行摆放按钮数量不同可以更改
    y, x = divmod(i, 6)
    # 放置按钮，位置会随着i的值变化，依次摆放
    button.place(x=100 + x * 100, y=100 + y * 100, width=80, height=80)


def allWhite():
    for x in btn_list:
        x['bg'] = 'white'


def round():
    m = len(btn_list)

    # 点击按钮后，判断按钮显示的文本，然后换成相反的
    if btn_start['text'] == '开始':
        btn_start['text'] = '停止'
        if len(neiding) > len(winner):
            winner.append(neiding[len(winner)])


    else:
        # 如果点击按钮时，显示的文本是‘停止’，就会跳出函数。
        btn_start['text'] = '开始'
        return
    # 设置按钮列表的长度，也就是公司数量

    # 随机生成i的值，i将会作为按钮列表的索引值
    # 也就是点击开始按钮时会随机开始

    i = randint(0, m - 1)

    while True:
        # 遍历所有的按钮，将所有的组件背景变为白色

        for x in btn_list:
            x['bg'] = 'white'
        # 将当前数值对应的组件的背景颜色设置成红色，表示选中的状态
        btn_list[i]['bg'] = 'red'

        # 判断按钮显示的文本是否是‘开始’，
        # 因为只有点击停止按钮时显示文本才会变成‘开始’，弹窗出现，跳出循环
        if btn_start['text'] == '开始':
            # 设置弹窗，使用showinfo函数展示中奖信息
            if len(neiding) > len(winner):
                i = neiding[len(winner)]
                allWhite()
                btn_list[i]['bg'] = 'red'
            tk.messagebox.showinfo('抽签结果', message='{}成为本轮出演者'.format(btn_list[i]['text']))

            break
        # 重新将i赋值一个随机坐标，目的是为了让抽签时每次都是随机选中按钮的
        i = randint(0, m - 1)
        # 延时，可以更改时间控制速度
        sleep(0.01)


# 创建线程的函数
def newtask():
    # 创建线程并运行，target传入开始抽签的函数
    t = threading.Thread(target=round)
    t.start()


# 设置开始按钮，commond传入点击按钮时执行的函数
btn_start = tk.Button(window, text='开始', font=('SimSun 15 bold'), command=newtask)
# 放置开始按钮
btn_start.place(x=300, y=450, width=200, height=80)
# 事件循环，保持窗口不会关闭
window.mainloop()
