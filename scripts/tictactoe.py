from printrun import gcoder
from printrun.printcore import printcore

class Printer():

    # Pen offset from extruder in mm.
    pen_x = 0
    pen_y = 0
    pen_z = 12.5

    def __init__(self,p:printcore,x:float=0,y:float=0,z:float=0):
        self.p = p
        self.pen_x = x
        self.pen_y = y
        self.pen_z = z

    def setup(self):
        self.p.send_now('G28 ;') # Home printer
        self.load_pen()
        self.center()
    
    def center(self):
        self.p.send_now(f'G0 X{110-self.pen_x} Y{110-self.pen_y} Z125 F3000') # Centers pen on Ender 3 with default bed size of 220x220mm.
    
    def load_pen(self):
        self.p.send_now(f'G0 X{110-self.pen_x} Y{200-self.pen_y} Z25.4') # Brings print head to front of printer to enable loading of pen.
        input("Press enter when pen is loaded.") # Awaits user confirmation that pen is loaded.
        self.p.send_now(f'G0 Z{self.pen_z}') # Lowers print head to meet desired pen_z offset and ensure pen is at correct height.

