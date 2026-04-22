"""
main.py

Eventual entry point for tic-tac-toe app.
"""

import sys
import time
from printrun.printcore import printcore

import scripts.tictactoe as tictactoe

if __name__ == "__main__":
    if sys.version_info.major != 3 and sys.version_info.minor != 12:
        raise Exception("Python 3.12 is required.")
    port = input("Enter device port: ")
    baud = input("Enter baud rate (default 115200): ")
    if baud == "":
        baud = 115200
    offset = {"x": 0,"y": 0, "z": 0}
    response = input("Pen offset? [y/n]")
    if response.lower() == "y":
        for key in offset.keys():
            offset[key] = input(f"{key} offset in mm: ")
    p = printcore(port,baud)
    game = tictactoe.Printer(p,offset["x"],offset["y"],offset["z"])
    game.setup()
    p.disconnect()
