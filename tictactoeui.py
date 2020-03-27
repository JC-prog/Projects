from tkinter import *

# Global Variable

#Functions 
def reset():
    pass

def sel():
    pass

#Front End
window = Tk()
window.title("Tic Tac Toe")

# Left Frame
left_frame = Frame(window)
left_frame.pack(side=LEFT)

# Player Names 
player1_label = Label(left_frame, text="Player 1")
player1_label.grid(row=0, column=0)
player1_entry = Entry(left_frame, width=10)
player1_entry.grid(row=0, column=1)

player2_label = Label(left_frame, text="Player 2")
player2_label.grid(row=1, column=0)
player2_entry = Entry(left_frame, width=10)
player2_entry.grid(row=1, column=1)

# Option Menu
p1_marker = StringVar()
player1_option = OptionMenu(left_frame, p1_marker, "X", "O" )
player1_option.grid(row=0, column=2)

p2_marker = StringVar()
player2_option = OptionMenu(left_frame, p2_marker, "X", "O")
player2_option.grid(row=1, column=2)

# Player Order
p1 = IntVar
p2 = IntVar
player_order_label = Label(left_frame, text="Who goes first?")
player_order_label.grid(row=2, column=0)

player_order_radio_1 = Radiobutton(left_frame, variable=p1, text="Player 1", value=1)
player_order_radio_1.grid(row=2, column=1)
player_order_radio_2 = Radiobutton(left_frame, variable=p2, text="Player 2", value=2 )
player_order_radio_2.grid(row=3, column=1)

# Reset Button
reset_button = Button(left_frame,text ="Reset", width=5)
reset_button.grid(row=4, column=1)

# Right Frame 
right_frame = Frame(window)
right_frame.pack(side=RIGHT)

# Game Board Buttons
# Row 1
button_1 = Button(right_frame,text=" " ,width=5, height=2)
button_1.grid(row=0, column=0)
button_2 = Button(right_frame,text=" " , width=5, height=2)
button_2.grid(row=0, column=1)
button_3 = Button(right_frame,text=" " , width=5, height=2)
button_3.grid(row=0, column=2)

# Row 2
button_4 = Button(right_frame,text=" " , width=5, height=2)
button_4.grid(row=1, column=0)
button_5 = Button(right_frame,text=" " , width=5, height=2)
button_5.grid(row=1, column=1)
button_6 = Button(right_frame,text=" " , width=5, height=2)
button_6.grid(row=1, column=2)

# Row 3
button_7 = Button(right_frame,text=" " , width=5, height=2)
button_7.grid(row=2, column=0)
button_8 = Button(right_frame,text=" " , width=5, height=2)
button_8.grid(row=2, column=1)
button_9 = Button(right_frame,text=" " , width=5, height=2)
button_9.grid(row=2, column=2)

mainloop()