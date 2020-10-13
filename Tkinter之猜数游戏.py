#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk  # 使用Tkinter前需要先导入(方法一)
from tkinter import *  # 导入 Tkinter 库（方法二）
import tkinter.messagebox

# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title('猜数字小游戏：')

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x

# 第4步，建立一个文本，设置字的颜色，内容，字的字体、大小
label1 = tk.Label(window, fg='black', text="游戏规则：\n在1到100中猜数字！！！", font=('宋体', 15, 'bold'))
# 设置文本框的位置
label1.grid(padx=10, pady=10)  # Label(父对象, padx=水平边距, pady=垂直边距)
label2 = tk.Label(window, fg='black', text="请输入你所猜测的数字：", font=('宋体', 15, 'bold'))
label2.grid(padx=10, pady=10)

text = tk.Entry(window, width=30)
text.grid(padx=100)
# 在使用Tkinter模块编写图像界面时，经常用到pack()和grid()进行布局管理，
# pack()参数较少，使用方便，是最简单的布局，
# 但是当控件数量较多时，可能需要使用grid()进行布局
# （不要在同一个窗口中同时使用grid()和pack()！！)

import random
number = random.randint(1, 100)

def compare():
    use = int(text.get())
    nmaxn = 100
    nminn = 0
    if use == '':
        tk.messagebox.showerror('警告', '输入不能为空！！！')

    elif use < number:
        if use > nminn:
            nmaxn = use  # 修改提示范围的最大值
            tk.messagebox.showinfo('不正确', "大了，大了！请输入" + str(nminn) + "到" + str(nmaxn) + "之间任意整数：")
        elif use < 0:
            tk.messagebox.showerror('警告', '输入不正确！！！')

    elif use > number:
        if use < nmaxn:
            nminn = use  # 修改提示范围的最小值
            tk.messagebox.showinfo('不正确',"小了，小了！请输入" + str(nminn) + "到" + str(nmaxn) + "之间任意整数：")
        elif use > 100:
            tk.messagebox.showerror('警告', '输入不正确！！！')

    elif use == number:
        tk.messagebox.showinfo('正确', 'bingo！对啦！！')

    else:
        tk.messagebox.showerror('警告', '输入不正确！！！')

def close(event):
    window.destroy()

# 第5步，建立一个按钮,通过按钮触发比较函数
button1 = tk.Button(window, text='确定', command=compare, width=10, font=('微软雅黑', 10,))
# 设置按钮的位置
button1.grid(padx=10, pady=10)
text.bind('Return',compare)
button1.bind('Return',compare)
# 第6步，建立一个按钮,通过按钮触发界面退出
button2 = tk.Button(window, text='退出游戏', command=close, width=10, bg='yellow', font=('微软雅黑', 10,))  # bg是背景颜色
button2.grid(padx=10, pady=10)
button2.bind('<Button-1>',close)
# 第7步，主窗口循环显示
window.mainloop()
# 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环
# 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键。
