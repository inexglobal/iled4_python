from microbit import *
class iled4:
    ADDRESS             = 0x70
    BLINK_CMD           = 0x80
    CMD_BRIGHTNESS      = 0xE0
    # Digits 0 - F
    NUMS = [0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D,
        0x07, 0x7F, 0x6F, 0x77, 0x7C, 0x39, 0x5E, 0x79, 0x71]
       
    def __init__(self):
        self.buffer = bytearray([0]*16)
        i2c.write(self.ADDRESS,b'\x21')
        # 0 to 3
        self.blink_rate(0)
        # 0 to 15
        self.set_brightness(15)
        self.update_display()
    
    def set_brightness(self,b):
        i2c.write(self.ADDRESS,bytes([self.CMD_BRIGHTNESS | b]))       
    
    def blink_rate(self, b):
        i2c.write(self.ADDRESS,bytes([self.BLINK_CMD | 1 | (b << 1)]))
    
    def write_digit(self, position, digit, dot=False):
        # skip the colon
        offset = 0 #if position < 2 else 1
        pos = offset + position
        self.buffer[pos*2] = self.NUMS[digit] & 0xFF
        if dot:
            self.buffer[pos*2] |= 0x80                    
    
    def update_display(self):
        data = bytearray([0]) + self.buffer
        i2c.write(self.ADDRESS,data)
    
    def print(self,value):
        if value<0 or value>9999:
            return
        sdig =  '{:04d}'.format(value)
        dts = [int(x) for x in sdig]
        for i,d in enumerate(dts):
            self.write_digit(i,d)
    
    def set_decimal(self, position, dot=True): 
        # skip the colon
        offset = 0 #if position < 2 else 1
        pos = offset + position        
        if dot:
            self.buffer[pos*2] |= 0x80
        else:
            self.buffer[pos*2] &= 0x7F
        
    def clear(self):
        self.buffer = bytearray([0]*16)
        self.update_display()
    
    def set_colon(self, colon=True):
        if colon:
            self.buffer[8] |= 0xFF # 0x02
        else:
            self.buffer[8] &= 0x00 # 0xFD