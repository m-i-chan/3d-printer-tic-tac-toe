from printrun.printcore import printcore
import time

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
        self.p.send('G0 F6000;') # Increase move rate.
        self.p.send('G28 ;') # Home printer
    
    def center(self):
        self.p.send(f'G0 X{110-self.pen_x} Y{110-self.pen_y} Z50 F6000;') # Centers pen on Ender 3 with default bed size of 220x220mm.
    
    def load_pen(self):
        self.p.send(f'G0 X{110-self.pen_x} Y{self.pen_y} Z25.4;') # Brings print head to front of printer to enable loading of pen.
        input("Press enter when pen is loaded.") # Awaits user confirmation that pen is loaded.
        self.p.send(f'G0 Z{self.pen_z} F500;') # Lowers print head to meet desired pen_z offset and ensure pen is at correct height.
        self.center()

    def go_to(self,x,y):
        self.p.send(f'G0 X{x-self.pen_x} Y{y-self.pen_y};')
    
    def draw_line(self, start_x, start_y, end_x, end_y):
        self.p.send(f'G0 Z{self.LIFT};')
        self.p.send(f'G0 X{start_x-self.pen_x} Y{start_y-self.pen_y};')
        self.p.send(f'G0 Z{self.pen_z};')
        self.p.send(f'G0 X{end_x-self.pen_x} Y{end_y-self.pen_y};')
        self.p.send(f'G0 Z{self.LIFT};')
        time.sleep(1)
    
    def draw_circle(self, start_x, start_y, i_offset, j_offset):
        self.p.send(f'G0 Z{self.LIFT};')
        self.p.send(f'G0 X{start_x-self.pen_x} Y{start_y-self.pen_y};')
        self.p.send(f'G0 Z{self.pen_z};')
        self.p.send(f'G2 I{i_offset} J{j_offset};')
        self.p.send(f'G0 Z{self.LIFT};')
        time.sleep(1)
    
    def draw_grid(self):
        self.draw_line(50,130,170,130)
        self.draw_line(50,90,170,90)
        self.draw_line(90,170,90,50)
        self.draw_line(130,170,130,50)
    
    def draw_o(self,grid_x=0,grid_y=0):
        offset_x = 70 + 40 * grid_x
        offset_y = 168 - 40 * grid_y
        self.draw_circle(offset_x,offset_y,0,-18)
    
    def draw_x(self,grid_x=0,grid_y=0):
        offset_x = 52 + 40 * grid_x
        offset_y = 168 - 40* grid_y
        self.draw_line(offset_x,offset_y,offset_x + 36, offset_y - 36)
        self.draw_line(offset_x,offset_y-36,offset_x + 36, offset_y)

        