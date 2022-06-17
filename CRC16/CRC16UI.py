# -*- coding:utf-8 -*-

# -------------------------------------------------------------------------------
# @Name：CRC16UI
# @Time: 2022/3/3111:25
# @Author: Liufei
# -------------------------------------------------------------------------------

from tkinter import *
from tkinter import ttk
from CRC16 import GetCRC16


class CRC16_UI:
    #初始化窗口名
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

    def set_init_window(self):
        self.init_window_name.title("CRC-16校验计算")        # 设置窗口标题
        self.init_window_name.geometry('840x650+400+200')     # 设置窗口大小，定义窗口弹出时的默认展示位置
        #控件
        self.labeframe = LabelFrame(self.init_window_name, height=233, width=1000, relief=FLAT)
        self.labeframe.pack(ipadx=20)
        self.data_label = Label(self.labeframe, text="CRC（循环冗余校验）计算", font=('宋体', 18))
        self.data_label.grid(row=0, column=0, sticky=N, columnspan=10, pady=10, padx=150)
        self.data_label1 = Label(self.labeframe, text="需要校验的数据：", font=('宋体', 12))
        self.data_label1.grid(row=1, column=0, sticky=E, padx=10)
        self.data_Text = Text(self.labeframe, width=60, height=8, font=('宋体', 12))
        self.data_Text.grid(row=1, column=1, sticky=E, padx=10)
        self.data_label2 = Label(self.labeframe, text="输入的数据为16进制，例如：31 32 33 34", font=('宋体', 12))
        self.data_label2.grid(row=2, column=1, sticky=NW, padx=10)

        self.labeframe2 = LabelFrame(self.init_window_name, height=233, width=1000, relief=FLAT)
        self.labeframe2.pack(fill='x')

        def chooes(event):
            widget = event.widget
            value = widget.get()
            if value == '自定义':
                self.value2.set("1")
                self.width_Combobox.configure(values=[x for x in range(1, 33)], state=NORMAL)
                self.width_Combobox.current(0)
                self.value3.set("")
                self.poly_Entry.configure(textvariable=self.value3, state=NORMAL)
                self.value4.set("")
                self.init_Entry.configure(textvariable=self.value4, state=NORMAL)
                self.value5.set("")
                self.xorout_Entry.configure(textvariable=self.value5, state=NORMAL)
                self.refin_checkbutton.deselect()
                self.refin_checkbutton.configure(state=NORMAL)
                self.refout_checkbutton.deselect()
                self.refout_checkbutton.configure(state=NORMAL)
            elif value == 'CRC-16/MODBUS    x16+x15+x2+1':
                self.value2.set("16")
                self.width_Combobox.configure(values='16', state=DISABLED)
                self.width_Combobox.current(0)
                self.value3.set("8005")
                self.poly_Entry.configure(textvariable=self.value3, state=DISABLED)
                self.value4.set("FFFF")
                self.init_Entry.configure(textvariable=self.value4, state=DISABLED)
                self.value5.set("0000")
                self.xorout_Entry.configure(textvariable=self.value5, state=DISABLED)
                self.refin_checkbutton.select()
                self.refin_checkbutton.configure(state=DISABLED)
                self.refout_checkbutton.select()
                self.refout_checkbutton.configure(state=DISABLED)
            elif value == 'CRC-16/X25    x16+x12+x5+1':
                self.value2.set("16")
                self.width_Combobox.configure(values='16', state=DISABLED)
                self.width_Combobox.current(0)
                self.value3.set("1021")
                self.poly_Entry.configure(textvariable=self.value3, state=DISABLED)
                self.value4.set("FFFF")
                self.init_Entry.configure(textvariable=self.value4, state=DISABLED)
                self.value5.set("FFFF")
                self.xorout_Entry.configure(textvariable=self.value5, state=DISABLED)
                self.refin_checkbutton.select()
                self.refin_checkbutton.configure(state=DISABLED)
                self.refout_checkbutton.select()
                self.refout_checkbutton.configure(state=DISABLED)
            elif value == 'CRC-16/USB    x16+x15+x2+1':
                self.value2.set("16")
                self.width_Combobox.configure(values='16', state=DISABLED)
                self.width_Combobox.current(0)
                self.value3.set("8005")
                self.poly_Entry.configure(textvariable=self.value3, state=DISABLED)
                self.value4.set("FFFF")
                self.init_Entry.configure(textvariable=self.value4, state=DISABLED)
                self.value5.set("FFFF")
                self.xorout_Entry.configure(textvariable=self.value5, state=DISABLED)
                self.refin_checkbutton.select()
                self.refin_checkbutton.configure(state=DISABLED)
                self.refout_checkbutton.select()
                self.refout_checkbutton.configure(state=DISABLED)
            elif value == 'CRC-16/DNP    x16+x13+x12+x11+x10+x8+x6+x5+x2+1':
                self.value2.set("16")
                self.width_Combobox.configure(values='16', state=DISABLED)
                self.width_Combobox.current(0)
                self.value3.set("3D65")
                self.poly_Entry.configure(textvariable=self.value3, state=DISABLED)
                self.value4.set("0000")
                self.init_Entry.configure(textvariable=self.value4, state=DISABLED)
                self.value5.set("FFFF")
                self.xorout_Entry.configure(textvariable=self.value5, state=DISABLED)
                self.refin_checkbutton.select()
                self.refin_checkbutton.configure(state=DISABLED)
                self.refout_checkbutton.select()
                self.refout_checkbutton.configure(state=DISABLED)
            elif value == 'CRC-16/CCITT    x16+x12+x5+1':
                self.value2.set("16")
                self.width_Combobox.configure(values='16', state=DISABLED)
                self.width_Combobox.current(0)
                self.value3.set("1021")
                self.poly_Entry.configure(textvariable=self.value3, state=DISABLED)
                self.value4.set("0000")
                self.init_Entry.configure(textvariable=self.value4, state=DISABLED)
                self.value5.set("0000")
                self.xorout_Entry.configure(textvariable=self.value5, state=DISABLED)
                self.refin_checkbutton.select()
                self.refin_checkbutton.configure(state=DISABLED)
                self.refout_checkbutton.select()
                self.refout_checkbutton.configure(state=DISABLED)

        self.name_label = Label(self.labeframe2, text="参数模型 NAME：", font=('宋体', 12))
        self.name_label.grid(row=0, column=0, sticky=NE, padx=10, pady=10)
        self.value1 = StringVar(self.init_window_name)
        self.value1.set('自定义')
        self.values = ['自定义', 'CRC-16/MODBUS    x16+x15+x2+1', 'CRC-16/X25    x16+x12+x5+1', 'CRC-16/CCITT    x16+x12+x5+1',
                  'CRC-16/USB    x16+x15+x2+1', 'CRC-16/DNP    x16+x13+x12+x11+x10+x8+x6+x5+x2+1']
        self.name_Combobox = ttk.Combobox(self.labeframe2, state='readonly', font=('宋体', 12), cursor='arrow', width=50, values=self.values)
        self.name_Combobox.grid(row=0, column=1, sticky=NW, pady=10)
        self.name_Combobox.bind('<<ComboboxSelected>>', chooes)
        self.name_Combobox.current(0)

        self.width_label = Label(self.labeframe2, text="宽度 WIDTH：", font=('宋体', 12))
        self.width_label.grid(row=1, column=0, sticky=NE, padx=10, pady=10)
        self.value2 = StringVar(self.init_window_name)
        self.value2.set('1')
        self.values1 = [x for x in range(1, 33)]
        self.width_Combobox = ttk.Combobox(self.labeframe2, state='readonly', font=('宋体', 12), cursor='arrow', width=10, values=self.values1)
        self.width_Combobox.grid(row=1, column=1, sticky=NW, pady=10)
        self.width_Combobox.current(0)

        self.poly_label = Label(self.labeframe2, text="多项式 POLY（Hex）：", font=('宋体', 12))
        self.poly_label.grid(row=2, column=0, sticky=NE, padx=10, pady=10)
        self.value3 = StringVar(self.init_window_name)
        self.value3.set('')
        self.poly_Entry = Entry(self.labeframe2, width=25, font=('宋体', 12), textvariable=self.value3)
        self.poly_Entry.grid(row=2, column=1, sticky=W)
        self.poly_label2 = Label(self.labeframe2, text="例如：3D65", font=('宋体', 12))
        self.poly_label2.grid(row=2, column=1, sticky=NW, padx=250, pady=10)

        self.init_label = Label(self.labeframe2, text="初始值 INIT（Hex）：", font=('宋体', 12))
        self.init_label.grid(row=3, column=0, sticky=NE, padx=10, pady=10)
        self.value4 = StringVar(self.init_window_name)
        self.value4.set('')
        self.init_Entry = Entry(self.labeframe2, width=25, font=('宋体', 12), textvariable=self.value4)
        self.init_Entry.grid(row=3, column=1, sticky=W)
        self.init_label2 = Label(self.labeframe2, text="例如：FFFF", font=('宋体', 12))
        self.init_label2.grid(row=3, column=1, sticky=NW, padx=250, pady=10)

        self.xorout_label = Label(self.labeframe2, text="结果异或值 XOROUT（Hex）：", font=('宋体', 12))
        self.xorout_label.grid(row=4, column=0, sticky=NE, padx=10, pady=10)
        self.value5 = StringVar(self.init_window_name)
        self.value5.set('')
        self.xorout_Entry = Entry(self.labeframe2, width=25, font=('宋体', 12), textvariable=self.value5)
        self.xorout_Entry.grid(row=4, column=1, sticky=W)
        self.xorout_label2 = Label(self.labeframe2, text="例如：0000", font=('宋体', 12))
        self.xorout_label2.grid(row=4, column=1, sticky=NW, padx=250, pady=10)

        self.status1 = IntVar()
        self.refin_checkbutton = Checkbutton(self.labeframe2, text="输入数据反转（REFIN）", font=('宋体', 12), variable=self.status1)
        self.refin_checkbutton.grid(row=5, column=1, sticky=NW, pady=10)

        self.status2 = IntVar()
        self.refout_checkbutton = Checkbutton(self.labeframe2, text="输出数据反转（REFOUT）", font=('宋体', 12), variable=self.status2)
        self.refout_checkbutton.grid(row=5, column=1, sticky=NW, padx=230, pady=10)

        def getdata():
            data = self.data_Text.get('0.0', 'end')
            width = self.width_Combobox.get()
            poly = self.poly_Entry.get()
            init = self.init_Entry.get()
            xorout = self.xorout_Entry.get()
            refin = self.status1.get()
            refout = self.status2.get()
            crc16 = GetCRC16('0x'+init, '0x'+poly, int(width), '0x'+xorout, refin, refout)
            CRC = crc16.getCRC16(data)
            outdata_bin = bin(CRC)[2:].zfill(16)
            outdata_hex = hex(CRC)[2:]
            self.value6.set(outdata_hex.upper())
            self.hex_Entry.configure(textvariable=self.value6, state='readonly')

            self.value7.set(outdata_bin)
            self.bin_Entry.configure(textvariable=self.value7, state='readonly')

        self.success_btn = Button(self.labeframe2, text="计算", font=('宋体', 12), bg='green', fg='white', command=getdata)
        self.success_btn.grid(row=6, column=1, sticky=NW, pady=10, ipadx=20)

        def cleardata():
            self.data_Text.delete('0.0', 'end')

            self.value1.set("自定义")
            self.name_Combobox.configure(values=['自定义', 'CRC-16/MODBUS    x16+x15+x2+1', 'CRC-16/X25    x16+x12+x5+1',
                  'CRC-16/XMODEM    x16+x12+x5+1', 'CRC-16/DNP    x16+x13+x12+x11+x10+x8+x6+x5+x2+1'], state=NORMAL)
            self.name_Combobox.current(0)

            self.value2.set("1")
            self.width_Combobox.configure(values=[x for x in range(1, 33)], state=NORMAL)
            self.width_Combobox.current(0)

            self.poly_Entry.configure(state=NORMAL)
            self.poly_Entry.delete(0, 'end')
            self.init_Entry.configure(state=NORMAL)
            self.init_Entry.delete(0, 'end')
            self.xorout_Entry.configure(state=NORMAL)
            self.xorout_Entry.delete(0, 'end')

            self.refin_checkbutton.deselect()
            self.refin_checkbutton.configure(state=NORMAL)
            self.refout_checkbutton.deselect()
            self.refout_checkbutton.configure(state=NORMAL)

            self.hex_Entry.configure(state=NORMAL)
            self.hex_Entry.delete(0, 'end')
            self.hex_Entry.configure(state='readonly')
            self.bin_Entry.configure(state=NORMAL)
            self.bin_Entry.delete(0, 'end')
            self.bin_Entry.configure(state='readonly')

        self.claer_btn = Button(self.labeframe2, text="清空", font=('宋体', 12), bg='green', fg='white', command=cleardata)
        self.claer_btn.grid(row=6, column=1, sticky=NW, pady=10, padx=100, ipadx=20)

        self.labeframe3 = LabelFrame(self.init_window_name, height=233, width=1000, relief=FLAT)
        self.labeframe3.pack(ipadx=150)
        self.hex_label = Label(self.labeframe3, text="校验计算结果（Hex）：", font=('宋体', 12))
        self.hex_label.grid(row=0, column=0, sticky=NE, padx=10)
        self.value6 = StringVar(self.init_window_name)
        self.value6.set('')
        self.hex_Entry = Entry(self.labeframe3, width=35, font=('宋体', 12), state='readonly')
        self.hex_Entry.grid(row=0, column=1, sticky=W)
        self.hex_label2 = Label(self.labeframe3, text="高位在左低位在右，使用时请注意高低位顺序！！！", font=('宋体', 10), fg="red")
        self.hex_label2.grid(row=1, column=1, sticky=NW)

        self.bin_label = Label(self.labeframe3, text="校验计算结果（Bin）：", font=('宋体', 12))
        self.bin_label.grid(row=2, column=0, sticky=NE, padx=10, pady=10)
        self.value7 = StringVar(self.init_window_name)
        self.value7.set('')
        self.bin_Entry = Entry(self.labeframe3, width=35, font=('宋体', 12), state='readonly')
        self.bin_Entry.grid(row=2, column=1, sticky=W)

