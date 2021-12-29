# -*- coding:utf-8 -*-
import threading
import random
import subprocess
import time


class Controller:

    def __init__(self):
        self.path = None
        self.thread_start = False
        self.on_play = False
        self.ip = '192.168.31.88'
        # 教研室校园网： 192.168.137.247
        # 教研室公用wifi: 192.168.0.149
        # 寝室校园网： 192.168.31.88
        self.port = '8888'
        self.thread = None
        self.thread_num = 0
        self.connect()

    def connect(self):
        self.path = self.ip + ':' + self.port
        try:
            subprocess.run('adb disconnect', shell=True, timeout=1)
            resp = subprocess.run('adb connect ' + self.path, shell=True, timeout=1)
        except:
            return False
        return True

    def set_port(self):
        try:
            resp = subprocess.run('adb tcpip ' + self.port, shell=True, timeout=1)
        except:
            return False
        return True


    def _play_(self):
        self.thread_start = True
        self.thread_num += 1
        now_thread = self.thread_num
        while True:
            # print(now_thread)
            if self.thread_num != now_thread:
                # print('not now thread', end=' ')
                # print(self.thread_num, end=' ')
                # print(now_thread)
                break
            if self.on_play:
                # print('work')
                subprocess.run("adb shell input swipe 500 1000 250 250", shell=True)
                time.sleep(random.uniform(4, 5))
            else:
                # print('break')
                break

    def play(self):
        self.on_play = True
        try:
            self.thread = threading.Thread(target=self._play_)
            self.thread.setDaemon(True)
            self.thread.start()
        except:
            print("Error: 无法启动线程")

    def stop(self):
        self.on_play = False
