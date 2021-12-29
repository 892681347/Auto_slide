import base64
import tkinter as tk
from tkinter import ttk
from tkinter import *
import subprocess
from tkinter import messagebox
from controller import Controller
from config_png import img as config_img

controller = Controller()
config_window = None


# 打包 pyinstaller -F -w -i Awake.ico main.py

# 按钮的函数
def play():
    if not controller.on_play:
        controller.play()
        var.set('停止')
    else:
        controller.stop()
        var.set('播放')


def config():
    global config_window

    def connect():
        controller.port = port_entry.get()
        controller.ip = ip_entry.get()
        global config_window
        status = controller.connect()
        if status:
            try:
                config_window.destroy()
            except:
                pass
            messagebox.showinfo('提示', '连接成功')
        else:
            messagebox.showerror('提示', '连接失败')

    def set_port():
        controller.port = port_entry.get()
        status = controller.set_port()
        if status:
            messagebox.showinfo('提示', '设置端口成功')
        else:
            messagebox.showerror('提示', '设置端口失败')

    if config_window is not None:
        try:
            config_window.destroy()
        except:
            pass
    config_window = tk.Tk()
    config_window.title('')
    config_window.resizable(False, False)
    config_window.wm_attributes('-topmost', 1)
    ip_frame = ttk.Frame(config_window)
    port_frame = ttk.Frame(config_window)
    btn_frame = ttk.Frame(config_window)
    ip_label = ttk.Label(ip_frame, text="  ip  ")
    ip_label.pack(side=LEFT)
    ip_entry = ttk.Entry(ip_frame, show=None, takefocus=False)  # 如果是输入密码，可以写show='*'
    ip_entry.pack(side=RIGHT)
    ip_entry.insert(0, controller.ip)
    ip_frame.pack(padx=10, pady=10)

    port_label = ttk.Label(port_frame, text="port")
    port_label.pack(side=LEFT)
    port_entry = ttk.Entry(port_frame, show=None, takefocus=False)  # 如果是输入密码，可以写show='*'
    port_entry.pack()
    port_entry.insert(0, controller.port)
    port_frame.pack(padx=10)

    port_btn = ttk.Button(btn_frame, text='设置端口', takefocus=False, command=set_port)
    port_btn.pack(side=LEFT, padx=10)
    connect_btn = ttk.Button(btn_frame, text='测试连接', takefocus=False, command=connect)
    connect_btn.pack(side=RIGHT, padx=10)
    btn_frame.pack(padx=10, pady=10)

    # test_btn = tk.Button(config_window, text='测试连接', command=test)
    # test_btn.pack(pady=2)

    config_window.mainloop()


if __name__ == '__main__':
    # 创建窗口
    window = tk.Tk()
    window.title('')  # 窗口的标题
    window.geometry('180x80')  # 窗口的大小
    window.resizable(False, False)
    # 定义一个lable
    var = tk.StringVar()  # 定义一个字符串变量
    var.set('播放')

    tmp = open('config.png', 'wb')  # 创建临时的文件
    tmp.write(base64.b64decode(config_img))  ##把这个one图片解码出来，写入文件中去。
    tmp.close()
    config_img = tk.PhotoImage(file=r'config.png')
    config_btn = ttk.Button(window, image=config_img, command=config, takefocus=False)
    # config_btn = ttk.Button(window, text='配置', command=config, takefocus=False)
    config_btn.pack(side=TOP, pady=5)

    play_btn = ttk.Button(window, textvariable=var, width=10, command=play, takefocus=False)  # 点击按钮执行一个名为“hit_me”的函数
    play_btn.pack()

    window.mainloop()
