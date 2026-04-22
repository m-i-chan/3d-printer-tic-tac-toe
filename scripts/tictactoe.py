from printrun.printcore import printcore

class Printer():

    # Pen offset from extruder in mm.
    pen_x = 0
    pen_y = 0
    pen_z = 12.5
    LIFT = pen_z + 10 # Height to lift pen while drawing

    def __init__(self,p:printcore,x:float=0,y:float=0,z:float=0):
        self.p = p
        self.pen_x = x
        self.pen_y = y
        self.pen_z = z

    def home(self):
        self.p.send('G28 ;') # Home printer
    
    def center(self):
        self.p.send(f'G0 X{110-self.pen_x} Y{110-self.pen_y} Z125 F3000') # Centers pen on Ender 3 with default bed size of 220x220mm.
    
    def load_pen(self):
        self.p.send(f'G0 X{110-self.pen_x} Y{200-self.pen_y} Z25.4') # Brings print head to front of printer to enable loading of pen.
        input("Press enter when pen is loaded.") # Awaits user confirmation that pen is loaded.
        self.p.send(f'G0 Z{self.pen_z}') # Lowers print head to meet desired pen_z offset and ensure pen is at correct height.
        self.center()
    
    def draw_line(self, start_x, start_y, end_x, end_y):
        self.p.send(f'G0 Z{self.LIFT}')
        self.p.send(f'G0 X{start_x} Y{start_y}')
        self.p.send(f'G0 Z{self.pen_z}')
        self.p.send(f'G0 X{end_x} Y{end_y}')
        self.p.send(f'G0 Z){self.LIFT}')
    
    def draw_circle(self, start_x, start_y, radius):
        self.p.send(f'G0 Z{self.LIFT}')
        self.p.send(f'G0 X{start_x} Y{start_y}')
        self.p.send(f'G0 Z{self.pen_z}')
        self.p.send(f'G2 R{radius}')
        self.p.send(f'G0 Z{self.LIFT}')