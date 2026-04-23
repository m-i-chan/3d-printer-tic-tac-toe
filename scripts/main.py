"""
main.py

Entry point for tic-tac-toe.
"""

import sys
import time
import tkinter as tk

import app

if __name__ == "__main__":
    if sys.version_info.major != 3 and sys.version_info.minor != 12:
        raise Exception("Python 3.12 is required.")
    root = tk.Tk()
    game = app.TicTacToe_App(root)
    root.mainloop()
