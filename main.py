# -*- coding:utf-8 -*-

# -------------------------------------------------------------------------------
# @Name：main
# @Time: 2022/3/3113:45
# @Author: Liufei
# -------------------------------------------------------------------------------

from CRC16UI import CRC16_UI
from tkinter import *


if __name__ == '__main__':
    init_window = Tk()  # 实例化出一个父窗口
    CRC16 = CRC16_UI(init_window)
    CRC16.set_init_window()
    init_window.mainloop()  # 父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示