from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import messagebox
import tkinter
from turtle import circle, width
import BT
import sys
import gtts
from playsound import playsound
from PIL import Image, ImageTk
import os


def getImage(name, width, height):
    im = Image.open(name).resize((width, height))
    return ImageTk.PhotoImage(im)


def action():
    #获取输入框内容
    data = entry.get().strip()
    
    if data == '':
        message = messagebox.showinfo(title='Error', message='【发生错误】\n\n你啥都没输入啊喂！= = ')
        print(message)

    else:
        output = BT.work(data)

        #创建第二个窗口
        root2 = Tk()
        root2.geometry('550x260+400+250')
        root2.title('翻译结果')

        Label(root2, text = '【' + data + '】:\n\n' + output, font = ('黑体',12)).place(x=70,y=40)

        #message = messagebox.showinfo(title='翻译结果', message='【' + data + '】:\n\n' + output)
        #print(message)

        #语音播报(施工中...)
        '''
        tts = gtts.gTTS(output)
        tts.save("output.mp3")
        playsound("output.mp3")
        '''




def readme():
    #打开readme.txt
    path = str(path2) + '\\readme.txt'
    os.system(path)


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

    #os寻找目录路径
    path1 = os.path.abspath(__file__)
    path2 = os.path.dirname(path1)
    
    #设置位置和大小 500x300
    root.geometry('500x300+700+150')

    #设置窗口颜色
    #root.configure(bg='#F7DFDF')

    #创建画布
    canvas = Canvas(width=500, height=353, highlightthickness=0, borderwidth=0)
    canvas.place(x=0, y=0)
    Imagepath = str(path2) + '\\Images\\2.png'

    bg = PhotoImage(file=Imagepath)
    bgid = canvas.create_image(0, 0, image=bg, anchor='nw')

    #是否可拉伸窗口
    root.resizable(False,False)

    #设置标题
    root.title('百度翻译')

    #设置标签，grid --> 设置网格

    #Label(root, text = '请输入词汇: ', font = ('Microsoft Yahei UI',14, 'bold'),
    #       foreground='#9C5858',
    #        bg='#F7DFDF').grid(padx=30, pady=70)

    #设置canvas文字
    canvas.create_text((90,99), text='请输入词汇: ', font=('Microsoft Yahei UI',14, 'bold'), fill="White")
    
    #Label(root, text = '                     Created by BinL', font = ('黑体',10),
    #        foreground='#9C5858', 
    #        bg='#F7DFDF').grid(row=4, column=1,pady=30)

    canvas.create_text((400,260), text='Created by BinL', font=('黑体',10, 'bold'), fill="White")
    
    #Label(root, text = 'Ver 0.0.1', font = ('黑体',10), 
    #        foreground='#9C5858',
    #        bg='#F7DFDF').grid(row=2, column=0)
    canvas.create_text((80,260), text='Ver 0.1.2', font=('黑体',10, 'bold'), fill="White")

    #输入框
    entry = Entry(root,width=38)
    entry.place(x=170, y=88.3)



    #按钮1
    #im_button = getImage('2.png', 300, 212)
    button1 = Button(root, text = '运行', bg='#F7DFDF',command=action)
    button1.place(x=135, y=175, width=230, height=30)

    #按钮2
    button2 = Button(root, text = 'Readme', bg='#F8F2F2',command=readme)
    button2.place(x=0, y=0, width=60, height=20)
    



    #循环弹窗
    root.mainloop()

