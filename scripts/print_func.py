"""
print_func.py

Contains printer manipulation functions
"""

from printrun.printcore import printcore
import time

class Printer():
    # Pen offset from extruder in mm.
    pen_x = 0
    pen_y = 0
    pen_z = 0

    wait_time = 1 # Time in seconds after draw_line and draw_circle commands to wait for printer to draw.


    lift_z = pen_z + 5 # Height to lift pen after drawing.

    def __init__(self,p:printcore,x:float=0,y:float=0,z:float=12.5):
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
    
    def pen_loaded(self):
        self.p.send(f'G0 Z{self.pen_z} F500;') # Lowers print head to meet desired pen_z offset and ensure pen is at correct height.

    def go_to(self,x,y):
        self.p.send(f'G0 X{x-self.pen_x} Y{y-self.pen_y};')
    
    def go_to(self,x,y,z):
        self.p.send(f'G0 X{x-self.penx} Y{y-self.pen_y} Z{z-self.pen_z}')

    def draw_line(self, start_x, start_y, end_x, end_y):
        self.p.send(f'G0 Z{self.lift_z};')
        self.p.send(f'G0 X{start_x-self.pen_x} Y{start_y-self.pen_y};')
        self.p.send(f'G0 Z{self.pen_z};')
        self.p.send(f'G0 X{end_x-self.pen_x} Y{end_y-self.pen_y};')
        self.p.send(f'G0 Z{self.lift_z};')
        time.sleep(self.wait_time)
    
    def draw_circle(self, start_x, start_y, i_offset, j_offset):
        self.p.send(f'G0 Z{self.lift_z};')
        self.p.send(f'G0 X{start_x-self.pen_x} Y{start_y-self.pen_y};')
        self.p.send(f'G0 Z{self.pen_z};')
        self.p.send(f'G2 I{i_offset} J{j_offset};')
        self.p.send(f'G0 Z{self.lift_z};')
        time.sleep(self.wait_time)
    
    def draw_grid(self):
        # Draws tic tac toe grid
        # Currently hard-coded for Ender 3 center.
        self.draw_line(50,130,170,130)
        self.draw_line(50,90,170,90)
        self.draw_line(90,170,90,50)
        self.draw_line(130,170,130,50)
    
    def draw_o(self,grid_x=0,grid_y=0):
        # Draws an o in specified square of above grid. Grid coordinates are (0,0) for top left square and (2,2) for bottom right.
        # Hard coded for above grid
        offset_x = 70 + 40 * grid_x
        offset_y = 168 - 40 * grid_y
        self.draw_circle(offset_x,offset_y,0,-18)
        print(f'Drawing O at ({grid_x},{grid_y})')
    
    def draw_x(self,grid_x=0,grid_y=0):
        #  Draws an x in specified square of above grid. Grid coordinates are (0,0) for top left square and (2,2) for bottom right.
        # Hard coded for above grid
        offset_x = 52 + 40 * grid_x
        offset_y = 168 - 40* grid_y
        self.draw_line(offset_x,offset_y,offset_x + 36, offset_y - 36)
        self.draw_line(offset_x,offset_y-36,offset_x + 36, offset_y)
        print(f'Drawing X at ({grid_x},{grid_y})')

        