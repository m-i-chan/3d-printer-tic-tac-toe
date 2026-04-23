"""
main.py

Entry point for tic-tac-toe.
"""

import sys
import time
import tkinter as tk

from printrun.printcore import printcore
import print_func as pf
import app

def test():
    ender = pf.Printer(p)
    ender.draw_x(2,2)

if __name__ == "__main__":
    if sys.version_info.major != 3 and sys.version_info.minor != 12:
        raise Exception("Python 3.12 is required.")
    
#    Troubleshooting space, please ignore
#    p = printcore("COM3",115200)
#    time.sleep(1)
#    test()
#    ender.draw_grid()
#    ender.draw_x(1,1)
#    ender.draw_o(1,2)
#    p.disconnect()

    root = tk.Tk()
    game = app.TicTacToe_App(root)
    root.mainloop()
