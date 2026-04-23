"""
app.py

GUI and controller for tic-tac-toe game. Inputs to GUI are translated to tic tac toe and associated printer function is called.
"""
class TicTacToe_App:

    import tkinter as tk
    from printrun.printcore import printcore

    import tictactoe as ttt
    import print_func as pf

    def __init__(self, root):
        self.root = root
        self.game = self.ttt.Game()
        self.com_port_frame()

    def com_port_frame(self):
        self.root.title("Ender 3 Tic-Tac_Toe")
        self.root.geometry("400x200")
        self.frame = self.tk.Frame(self.root)
        self.frame.pack()
        self.tk.Label(self.frame, text="COM Port").pack()
        self.com_port_val = self.tk.StringVar()
        self.com_port_entry = self.tk.Entry(self.frame,textvariable=self.com_port_val)
        self.com_port_button = self.tk.Button(self.frame, text="Connect",command=self.submit)
        self.com_port_entry.pack()
        self.com_port_button.pack()

    def submit(self):
        com_port = self.com_port_val.get()
        p = self.printcore(com_port,115200)
        if p.online:
            printer = self.pf.Printer(p)
            self.main.destroy()
            self.main = self.tk.Frame(self.root)
            self.main.pack()
        else:
            self.tk.Label(self.frame, text="Error connecting", fg="red").pack()
