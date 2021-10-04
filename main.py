from microbit import *
DS1302_REG_SECOND = (0x80)
DS1302_REG_MINUTE = (0x82)
DS1302_REG_HOUR = (0x84)
DS1302_REG_DAY = (0x86)
DS1302_REG_MONTH = (0x88)
DS1302_REG_WEEKDAY = (0x8A)
DS1302_REG_YEAR = (0x8C)
DS1302_REG_WP = (0x8E)
DS1302_REG_CTRL = (0x90)
DS1302_REG_RAM = (0xC0)

class DS1302:
    def_init_(self, clk, dio, cs):
        self.clk = clk
        self.dio = dio 
        self.cs = cs 

    def DecToHex(self, dat):
        return (data//10) * 16 + (data%10)

    def HexToDec(self, dat):
            return (data//16) * 10 + (data%16)

    def write_byte(self, dat):
        for i in range(8):
            self.dio.write_digital((dat >> i) & 1)
            self.clk.write_digital(1)
            self.clk.write_digital(0)

    def read_byte(self):
        d = 0
        for i in range(8):
            d = d | (self.dio.read_digital() << i)
            self.clk.write_digital(1)
            self.clk.write_digital(0)
        return d

    def getReg(self, reg):
        self.cs.write_digital(1)
        self.write_byte(reg) 
        t = self.read_byte() 
        self.cs.write_digital(0)      
        return t

    def setReg(self, reg, dat) 
        self.cs.write_digital(1)
        self.write_byte(reg) 
        self.write_byte(dat) 
        self.cs.write_digital(0)

    def wr(self, reg, dat):
        self.setReg(DS1302_REG_WP, 0)
        self.setReg(reg, dat)
        self.setReg(DS1302_REG_WP, 0x80) 

    def start(self):
        t = self.getReg(DS1302_REG_SECOND + 1)
        self.wr(DS1302_REG_SECOND, t & 0x7f)

        