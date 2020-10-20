import tkinter as tk
import tkinter as Tkinter
from tkinter import *
import tkinter.messagebox
import random
import pandas as pd

test1 = pd.read_excel('C:\\Users\\lenovo\\Desktop\\数应191名单.xlsx')
data = test1.iloc[:, 2]
going = True  # 表示是否可以继续滚动(递归)显示下一个名额
is_run = False  # 表示当前抽奖器是否在运行


# def lottery_roll(var1, var2):
def lottery_roll(var1):
    global going
    show_member = random.choice(data)  # 随机选取姓名
    var1.set(show_member)  # var1 显示抽取出来的姓名
    if going:  # going=True
        window.after(50, lottery_roll, var1)  # 每50毫秒循环一次 after方法接受三个参数，时间（刷新主窗口的频率）+ 函数（tell主程序要做的动作）+ 更新的变量
    else:  # going=False
        result = tkinter.messagebox.showinfo(title='信息提示！', message='恭喜 {} ！！！'.format(show_member))  # 弹窗显示恭喜+抽取出来的姓名
        going = True
        return  # 跳出def


def lottery_start(var1):
    global is_run
    if is_run:  # is_run = True
        return  # 跳出def
    is_run = True
    lottery_roll(var1)  # 执行循环抽取姓名的执行语句


def lottery_end():
    global going, is_run
    if is_run:
        going = False
        is_run = False


if __name__ == '__main__':  # 如果模块是被直接运行的，则代码块被运行，如果模块是被导入的，则代码块不被运行。
    window = Tkinter.Tk()
    window.title('点名程序：')
    # window.geometry('500x300')
    window.geometry('405x320+250+15')
    # window.title('   滚 动 抽 奖 器')
    # bg_label = Label(window, width=70, height=24, bg='#ECf5FF')
    bg_label = Label(window, width=70, height=24)
    bg_label.place(anchor=NW, x=0, y=0)

    var1 = StringVar(value='即 将 开 始')
    #show_label1 = Label(window, textvariable=var1, justify='left', anchor=CENTER, width=17, height=3, bg='#BFEFFF',
    #                    font='楷体 -40 bold', foreground='black')
    show_label1 = Label(window, textvariable=var1, justify='left', anchor=CENTER, width=17, height=3,
                       font='楷体 -40 bold', foreground='black')
    show_label1.place(anchor=NW, x=21, y=20)

    button1 = Button(window, text='开始', command=lambda: lottery_start(var1), width=14, height=2, bg='#A8A8A8',
                     font='宋体 -18 bold')
    button1.place(anchor=NW, x=20, y=175)

    button2 = Button(window, text='结束', command=lambda: lottery_end(), width=14, height=2, bg='#A8A8A8',
                     font='宋体 -18 bold')
    button2.place(anchor=NW, x=232, y=175)

    window.mainloop()
