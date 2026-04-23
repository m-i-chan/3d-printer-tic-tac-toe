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
        self.root.title("Ender 3 Tic-Tac-Toe")
        self.root.geometry("400x200")
        self.display_com_port()

    def display_com_port(self):
        self.com_port_frame = self.tk.Frame(self.root)
        self.com_port_frame.pack()
        self.tk.Label(self.com_port_frame, text="COM Port").pack()
        self.com_port_val = self.tk.StringVar()
        self.com_port_entry = self.tk.Entry(self.com_port_frame,textvariable=self.com_port_val)
        self.tk.Label(self.com_port_frame,text="(Ensure baud rate is 115200 in device manager.)").pack()
        com_port_button = self.tk.Button(self.com_port_frame, text="Connect",command=self.submit)
        self.com_port_entry.pack()
        com_port_button.pack()

    def submit(self):
        com_port = self.com_port_val.get()
        self.p = self.printcore(com_port,115200)
        if not self.p.online:
            self.printer = self.pf.Printer(self.p)
            self.com_port_frame.destroy()
            self.display_menu_frame()
            self.printer.home()
        else:
            self.tk.Label(self.com_port_frame, text="Error connecting", fg="red").pack()

    def display_menu_frame(self):
        self.menu_frame = self.tk.Frame(self.root)
        self.menu_frame.pack()

        start_button = self.tk.Button(self.menu_frame,text="Start",command=self.start)
        start_button.pack()

        setup_button = self.tk.Button(self.menu_frame, text="Setup",command=self.setup)
        setup_button.pack()

    def start(self):
        self.menu_frame.destroy()
        self.display_game_frame()
        self.printer.draw_grid()

    def setup(self):
        self.menu_frame.destroy()
        self.display_setup_frame()
        self.printer.load_pen()

    def display_setup_frame(self):
        self.setup_frame = self.tk.Frame(self.root)
        self.setup_frame.pack()
        self.tk.Label(self.setup_frame,text="Click confirm when pen is loaded.").pack()
        confirm_button = self.tk.Button(self.setup_frame,text="Confirm",command=self.setup_confirm)
        confirm_button.pack()
    
    def setup_confirm(self):
        self.printer.pen_loaded()
        self.setup_frame.destroy()
        self.display_menu_frame()

    def display_game_frame(self):
        self.game_frame = self.tk.Frame(self.root)
        self.game_frame.pack()
        self.game_frame.columnconfigure(1,minsize=105)

        # GUI grid and printer grid are reflected over y=x for...reasons? TODO: Investigate

        top_left_button = self.tk.Button(self.game_frame,text="\u2518",command=lambda: self.move(0,0))
        top_left_button.grid(row=0,column=0)

        top_middle_button = self.tk.Button(self.game_frame,text="  ",command=lambda: self.move(1,0))
        top_middle_button.grid(row=0,column=1)

        top_right_button = self.tk.Button(self.game_frame,text="\u2514",command=lambda: self.move(2,0))
        top_right_button.grid(row=0,column=2)

        middle_left_button = self.tk.Button(self.game_frame,text="  ",command=lambda: self.move(0,1))
        middle_left_button.grid(row=1,column=0)

        middle_middle_button = self.tk.Button(self.game_frame,text="\u25A1",command=lambda: self.move(1,1))
        middle_middle_button.grid(row=1,column=1)

        middle_right_button = self.tk.Button(self.game_frame,text="  ",command=lambda: self.move(2,1))
        middle_right_button.grid(row=1,column=2)

        bottom_left_button = self.tk.Button(self.game_frame,text="\u2510",command=lambda: self.move(0,2))
        bottom_left_button.grid(row=2,column=0)

        bottom_middle_button = self.tk.Button(self.game_frame,text="  ",command=lambda: self.move(1,2))
        bottom_middle_button.grid(row=2,column=1)

        bottom_right_button = self.tk.Button(self.game_frame,text="\u250C",command=lambda: self.move(2,2))
        bottom_right_button.grid(row=2,column=2)

        self.player_label = self.tk.Label(self.game_frame, text="X is up.")
        self.player_label.grid(row=3,column=0,columnspan=3)
        self.error_label = self.tk.Label(self.game_frame, text="Space was taken.", fg="red")

        new_game_button = self.tk.Button(self.game_frame,text="New Game",command=self.new_game)
        new_game_button.grid(row=5, column=0, columnspan=3)

        quit_button = self.tk.Button(self.game_frame,text="Quit",command=self.quit)
        quit_button.grid(row=6,column=1)

    def display_new_game_frame(self):
        self.new_game_frame = self.tk.Frame(self.root)
        self.new_game_frame.pack()
        
        self.tk.Label(self.new_game_frame,text="Clear the board.").pack()

        new_game_next_button = self.tk.Button(self.new_game_frame,text="Next",command=self.new_game_confirm)
        new_game_next_button.pack()

    def new_game_confirm(self):
        self.new_game_frame.destroy()
        
        self.printer.draw_grid()

        self.display_game_frame()

    def new_game(self):
        self.game_frame.destroy()
        self.display_new_game_frame()
        self.printer.center()
        self.game.new_game() # Clear computer's game state
    
    def quit(self):
        self.printer.center()
        self.p.disconnect()
        self.root.destroy()

    def move(self,x,y):
        try:
            self.game.turn(x,y)
            print(self.game.player)
            if self.game.player*-1 == -1:
                self.printer.draw_x(x,y)
            else:
                self.printer.draw_o(x,y)
            if self.game.winner != 0:
                self.player_label.config(text=f"Game over, {"X" if self.game.winner == -1 else "O"} won!")
                self.printer.center()
            else:
                self.player_label_toggle()
            self.error_label.grid_forget()
        except ValueError:
            self.error_label.grid(row = 4, column=0, columnspan=3)
        except Exception:
            self.player_label.config(text=f"Game over, {"X" if self.game.winner == -1 else "O"} won!")
            self.printer.center()

    def player_label_toggle(self):
        self.player_label.config(text=f"{"X" if self.game.player == -1 else "O"} is up.")