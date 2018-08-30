#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import configparser
import os
import sys

from tkinter import *
import tkinter.filedialog


class Run(object):
    def __init__(self):
        self.data_name = ''
        self.local_name = ''
        self.xshell_name = ''
        self.config = configparser.ConfigParser()
        self.filename = '%s\\config.ini' % os.path.split(os.path.realpath(__file__))[0]
        self.config_text = '[global]\ndata_dir=\nlocal_dir=\nxshell_path=\n'
        self.root = Tk()
        self.root.title("连接工具")
        self.root.geometry("800x400")
        self.title = Label(self.root, text='连接工具', font=('Arial', 20))  # 标题
        self.title.pack()

        self.frm = Frame(self.root)
        self.frm_l = Frame(self.frm)
        self.frm_r = Frame(self.frm)
        # self.frm_data = Frame(self.frm)
        # self.frm_xshell = Frame(self.frm)

        self.data_var = Label(self.frm_r, text=self.get_config()['data_dir'], font=("宋体",11), height=2)
        self.data_btn = Button(self.frm_l, text='选择数据目录', font=("宋体",11), height=2, width=15, command=self.data)
        self.local_var = Label(self.frm_r, text=self.get_config()['local_dir'], font=("宋体", 11), height=2)
        self.local_btn = Button(self.frm_l, text='选择本地目录', font=("宋体", 11), height=2, width=15, command=self.local)
        self.xshell_var = Label(self.frm_r, text=self.get_config()['xshell_path'], font=("宋体",11), height=2)
        self.xshell_btn = Button(self.frm_l, text='选择xshell程序', font=("宋体",11), height=2, width=15, command=self.xshell)

        self.start = Button(self.root, text='启动', font=("黑体",15), height=2, width=15, command=self.start)
        self.info = Label(self.root, text='', font=("宋体",12), height=4)
        self.blank = Label(self.root, text='', font=("宋体",11), height=4)

        self.frm.pack()
        # self.frm_data.pack()
        self.frm_l.pack(side=LEFT)
        self.frm_r.pack(side=RIGHT)

        self.data_var.pack(side=TOP)
        self.data_btn.pack(side=TOP)
        self.local_var.pack(side=TOP)
        self.local_btn.pack(side=TOP)
        # self.frm_xshell.pack()
        self.xshell_var.pack(side=TOP)
        self.xshell_btn.pack(side=TOP)

        self.info.pack(side=BOTTOM)
        self.blank.pack(side=BOTTOM)
        self.start.pack(side=BOTTOM)

    def get_config(self):
        if not os.path.isfile(self.filename):
            f = open(self.filename, 'a+')
            try:
                f.writelines(self.config_text)
                f.close()
            except Exception as e:
                print(e)
        try:
            self.config.read(self.filename)
            data_dir = self.config.get('global', 'data_dir')
            local_dir = self.config.get('global', 'local_dir')
            xshell_path = self.config.get('global', 'xshell_path')
            # print('data_dir, xshell', self.data_dir, self.xshell)
            return {'data_dir': data_dir, 'local_dir': local_dir, 'xshell_path': xshell_path}
        except Exception as e:
            print('配置文件读取失败！')
            print(e)

    def set_config(self, section, key, value):
        if not os.path.isfile(self.filename):
            f = open(self.filename, 'a+')
            try:
                f.writelines(self.config_text)
                f.close()
            except Exception as e:
                print(e)
        try:
            # self.config = configparser.ConfigParser()
            self.config.read(self.filename)
            self.config.set(section, key, value)
            # self.config.set('global', 'data_dir', self.data_name)
            # self.config.set('global', 'local_dir', self.local_name)
            # self.config.set('global', 'xshell_path', self.xshell_name)
            with open(self.filename, 'w') as f:
                self.config.write(f)
        except Exception as e:
            self.info.config(text=e, fg='red')

    def data(self):
        self.data_name = tkinter.filedialog.askdirectory()
        if self.data_name != '':
            self.data_var.config(text=self.data_name)
            self.set_config('global', 'data_dir', self.data_name)
        else:
            pass

    def local(self):
        self.local_name = tkinter.filedialog.askdirectory()
        if self.local_name != '':
            self.local_var.config(text=self.local_name)
            self.set_config('global', 'local_dir', self.local_name)
        else:
            pass

    def xshell(self):
        self.xshell_name = tkinter.filedialog.askopenfilename()
        if self.xshell_name != '':
            self.xshell_var.config(text=self.xshell_name)
            self.set_config('global', 'xshell_path', self.xshell_name)
        else:
            pass

    def start(self):
        self.info.config(text='拉取数据目录中', fg='green')
        # config = configparser.ConfigParser()
        self.config.read(self.filename)
        if self.get_config()['data_dir'] == '':
            if self.data_name == '':
                self.info.config(text='数据目录不能为空！', fg='red')
            else:
                self.config.set('global', 'data_dir', self.data_name)
            # if self.data_name == '':
            #     self.info.config(text='数据目录不能为空！', fg='red')
            # elif self.local_name == '':
            #     self.info.config(text='本地目录不能为空！', fg='red')
            # elif self.xshell_name == '':
            #     self.info.config(text='xshell路径不能为空！', fg='red')
            # else:
            #     config.set('global', 'data_dir', self.data_name)
        elif self.get_config()['local_dir'] == '':
            if self.local_name == '':
                self.info.config(text='本地目录不能为空！', fg='red')
            else:
                self.config.set('global', 'local_dir', self.local_name)
            # if self.data_name == '':
            #     self.info.config(text='数据目录不能为空！', fg='red')
            # elif self.local_name == '':
            #     self.info.config(text='本地目录不能为空！', fg='red')
            # elif self.xshell_name == '':
            #     self.info.config(text='xshell路径不能为空！', fg='red')
            # else:
            #     config.set('global', 'local_dir', self.local_name)
        elif self.get_config()['xshell_path'] == '':
            if self.xshell_name == '':
                self.info.config(text='xshell路径不能为空！', fg='red')
            else:
                self.config.set('global', 'xshell_path', self.xshell_name)
            # if self.data_name == '':
            #     self.info.config(text='数据目录不能为空！', fg='red')
            # elif self.local_name == '':
            #     self.info.config(text='本地目录不能为空！', fg='red')
            # elif self.xshell_name == '':
            #     self.info.config(text='xshell路径不能为空！', fg='red')
            # else:
            #     config.set('global', 'xshell_path', self.xshell_name)
        else:
            self.info.config(text='拉取数据目录中', fg='green')
            self.get_data()

        with open(self.filename, 'w') as f:
            self.config.write(f)

    def get_data(self):
        command = 'xcopy "' + self.get_config()['data_dir'].replace('/', '\\') + '" "' + self.get_config()['local_dir'].replace('/', '\\') + '" /d/i/y/e'
        # for i in os.listdir(self.data_name):
        #     print(i)
        print(command)
        run = os.system(command)
        if run == 0:
            self.info.config(text='拉取成功，启动xshell', fg='green')
            self.start_xshell()
        elif run == 1:
            self.info.config(text='没有找到要复制的文件', fg='red')
        elif run == 4:
            self.info.config(text='内存或磁盘空间不足，或无效的驱动器名称或语法', fg='red')
        elif run == 5:
            self.info.config(text='磁盘写入错误', fg='red')
        else:
            self.info.config(text='拉取失败，%s' % run, fg='red')

    def start_xshell(self):
        try:
            os.startfile(self.get_config()['xshell_path'])
            sys.exit(0)
        except Exception as e:
            self.info.config(text='启动xshell失败, %s' % e, fg='red')

def main():
    Run()
    mainloop()

if __name__== "__main__":
    main()