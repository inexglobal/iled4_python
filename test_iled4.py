from iled4 import *
import gc
gc.collect()
# declare an instance
f = iled4()
# decimals on
for i in range(4):
    f.set_decimal(i)
    f.update_display()
    sleep(1000)
# decimals off
for i in range(4):
    f.set_decimal(i, False)
    f.update_display()
    sleep(1000)

# print something
f.print(1234)
f.update_display()
sleep(1000)
# clear the display
f.clear()
sleep(1000)
# blink the colon
for i in range(4):
    f.set_colon()
    f.update_display()
    sleep(500)
    f.set_colon(False)
    f.update_display()
    sleep(500)       
# do some counting    
for i in range(10000):
    f.print(i)
    f.update_display()
    sleep(50)