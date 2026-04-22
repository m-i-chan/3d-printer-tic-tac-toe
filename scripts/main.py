"""
main.py

Entry point for tic-tac-toe.
"""

import sys
import time
from printrun.printcore import printcore

import tictactoe as ttt

if __name__ == "__main__":
    if sys.version_info.major != 3 and sys.version_info.minor != 12:
        raise Exception("Python 3.12 is required.")
    port = input("Enter device port: ")
    baud = input("Enter baud rate (default 115200): ")
    if baud == "":
        baud = 115200
    offset = {"x": 0,"y": 0, "z": 12.5}
    response = input("Pen offset? [y/n]")
    if response.lower() == "y":
        for key in offset.keys():
            offset[key] = input(f"{key} offset in mm: ")
    p = printcore(port,baud)
    setup = ttt.Printer(p,offset["x"],offset["y"],offset["z"])
    setup.home()
    setup.load_pen()
    p.disconnect()
