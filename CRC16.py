# -*- coding:utf-8 -*-

# -------------------------------------------------------------------------------
# @Name：CRC16
# @Time: 2022/2/2816:58
# @Author: Liufei
# -------------------------------------------------------------------------------

''''
    1．设置CRC寄存器，并给其赋值0000(hex)。
　　2．将数据的第一个8-bit字符与16位CRC寄存器的低8位进行异或，并把结果存入CRC寄存器。
　　3．CRC寄存器向右移一位，最高位(MSB)补零，移出并检查最低位(LSB)。
　　4．如果LSB为0，重复第三步；若LSB为1，CRC寄存器与多项式码相异或。
　　5．重复第3与第4步直到8次移位全部完成。此时一个8-bit数据处理完毕。
　　6．重复第2至第5步直到所有数据全部处理完成。
　　7．最终CRC寄存器的内容即为CRC值。
'''
class GetCRC16:
    def __init__(self, init, poly, width, xorout, refin, refout):
        # 参数模型名称：NAME
        # 例如：CRC-16/DNP x16+x13+x12+x11+x10+x8+x6+x5x+x2+1
        # 初始值：这是算法开始时寄存器（crc）的初始化预置值，十六进制表示。
        self.init = init
        # 多项式：生成项的简写，以16进制表示。
        self.poly = poly
        # 宽度：即CRC比特数。
        self.width = width
        # 结果异或值：计算结果与此参数异或后得到最终的CRC值。
        self.xorout = xorout
        # 输入数据反转：待测数据的每个字节是否按位反转，True或False。
        self.refin = refin
        # 输出数据反转：在计算后之后，异或输出之前，整个数据是否按位反转，True或False。
        self.refout = refout

    def refpoly(self):
        # 如果输入数据反转与输出数据反转都为True，则将多项式按位颠倒。
        if self.refin == 1 and self.refout == 1:
            refpoly = bin(int(self.poly, 16))[2:].zfill(self.width)[::-1]
            poly = hex(int(refpoly, 2))
            return poly
        else:
            return self.poly

    def getCRC16(self, data):
        data_list = data.split(" ")
        # 将数据的第一个8-bit字符与16位CRC寄存器的低8位进行异或，并把结果存入CRC寄存器。
        poly = self.refpoly()
        for data_subset in data_list:
            if self.refin == 1 and self.refout == 1:
                init = int(data_subset, 16) ^ int(self.init, 16)
                # CRC寄存器向右移一位，最高位(MSB)补零，移出并检查最低位(LSB)。
                for i in range(8):
                    LSB = bin(init)[2:].zfill(self.width)[-1:]
                    if int(LSB) == 1:
                        init = (init >> 1) ^ int(poly, 16)
                    else:
                        init = init >> 1
                self.init = hex(init)
            else:
                init = int(data_subset, 16) << 8 ^ int(self.init, 16)
                for i in range(8):
                    LSB = bin(init)[2:].zfill(self.width)[-1:]
                    if int(LSB) == 1:
                        init = (init >> 1) ^ int(poly, 16)
                    else:
                        init = init >> 1
                self.init = hex(init)
                #     LSB = bin(init)[2:].zfill(self.width)[:1]
                #     if int(LSB) == 1:
                #         init = (init << 1) ^ int(poly, 16)
                #     else:
                #         init = init << 1
                # init1 = bin(init).zfill(self.width)[3:]
                # self.init = hex(int(init1, 2))

        CRC = int(self.init, 16) ^ int(self.xorout, 16)
        return CRC


if __name__ == '__main__':
    crc16_xmodem = GetCRC16('0x0000', '0x1021', 16, '0x0000', 0, 0)
#     crc16_CCITTFALSE = CRC16('0xFFFF', '0x1021', 16, '0x0000', False, False)
#     # crc16_dnp = CRC16('0x0000', '0x3D65', 16, '0xFFFF', True, True)
    # crc16_X25 = CRC16('0xFFFF', '0x1021', 16, '0xFFFF', True, True)
    data = input('请输入数据：')
    CRC = crc16_xmodem.getCRC16(data)
    print(bin(CRC)[2:].zfill(16))
    print(hex(CRC))