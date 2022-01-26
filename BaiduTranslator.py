from cgitb import text
from tkinter import *
from tkinter import messagebox
from turtle import width
import BT
import sys

def action():
    #获取输入框内容
    data = entry.get().strip()
    output = BT.work(data)
    message = messagebox.showinfo(title='翻译结果', message='翻译结果:\n' + output)
    print(message)

def exit():
    #退出
    sys.exit(0)

#施工中...
def actWin():
    root = Tk()
    root.geometry('150x100+800+400')
    root.resizable(False,False)
    root.title('状态')
    Label(root, text = '正在执行中', font = ('黑体',13)).grid(padx=30, pady=70)
    root.mainloop()

if __name__ == '__main__':
    
    #实例化Tk
    root = Tk()
    

    #设置位置和大小
    root.geometry('500x300+800+400')

    #是否可拉伸窗口
    root.resizable(False,False)

    #设置标题
    root.title('百度翻译')

    #设置标签，grid --> 设置网格
    Label(root, text = '请输入词汇: ', font = ('黑体',13)).grid(padx=30, pady=70)
    Label(root, text = '                     Created by BinL', font = ('黑体',10)).grid(row=4, column=1,pady=30)
    Label(root, text = 'Ver 0.0.1', font = ('黑体',10)).grid(row=2, column=0)

    #输入框
    entry = Entry(root, width=40)
    entry.grid(row=0,column=1)


    #按钮1
    button1 = Button(root, text = '运行', width=20, command=action)
    button1.grid(row=2,column=1)



    #循环弹窗
    root.mainloop()