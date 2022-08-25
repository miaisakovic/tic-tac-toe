from tkinter import *

root = Tk()
root.title("Tic-tac-toe")

blank_img = PhotoImage(width=100, height=100)


def button_click(pos):
    click(pos)


# Create widgets
status = Label(root, text="X plays", font=("Monaco 15"))

button_1 = Button(root, image=blank_img, highlightbackground="#24C0D6", compound="center", width=100, height=100, command=lambda: button_click(0))
button_2 = Button(root, image=blank_img, highlightbackground="#24C0D6", compound="center", width=100, height=100, command=lambda: button_click(1))
button_3 = Button(root, image=blank_img, highlightbackground="#24C0D6", compound="center", width=100, height=100, command=lambda: button_click(2))

button_4 = Button(root, image=blank_img, highlightbackground="#24C0D6", compound="center", width=100, height=100, command=lambda: button_click(3))
button_5 = Button(root, image=blank_img, highlightbackground="#24C0D6", compound="center", width=100, height=100, command=lambda: button_click(4))
button_6 = Button(root, image=blank_img, highlightbackground="#24C0D6", compound="center", width=100, height=100, command=lambda: button_click(5))

button_7 = Button(root, image=blank_img, highlightbackground="#24C0D6", compound="center", width=100, height=100, command=lambda: button_click(6))
button_8 = Button(root, image=blank_img, highlightbackground="#24C0D6", compound="center", width=100, height=100, command=lambda: button_click(7))
button_9 = Button(root, image=blank_img, highlightbackground="#24C0D6", compound="center", width=100, height=100, command=lambda: button_click(8))

buttons = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9]


def click(pos):
    global turn
    global num_turns

    button = buttons[pos]

    # Check if button has been previously clicked
    if button["state"] == DISABLED:
        pass
    else:
        try:
            num_turns = num_turns + 1
        except NameError:
            num_turns = 1

        try:
            if turn == "X":
                turn = "O"
                button["disabledforeground"] = "white"
                status["text"] = "X plays"
            else:
                turn = "X"
                button["disabledforeground"] = "red"
                status["text"] = "O plays"
        except NameError:
            turn = "X"
            button["disabledforeground"] = "red"
            status["text"] = "O plays"

        button["text"] = turn
        button["font"] = ("Helvetica 50 bold")

        button["state"] = DISABLED

        # Check if there is a winner
        if (
            (button_1["text"] == button_2["text"] == button_3["text"] == turn) or
            (button_4["text"] == button_5["text"] == button_6["text"] == turn) or
            (button_7["text"] == button_8["text"] == button_9["text"] == turn) or
            (button_1["text"] == button_4["text"] == button_7["text"] == turn) or
            (button_2["text"] == button_5["text"] == button_8["text"] == turn) or
            (button_3["text"] == button_6["text"] == button_9["text"] == turn) or
            (button_1["text"] == button_5["text"] == button_9["text"] == turn) or
            (button_3["text"] == button_5["text"] == button_7["text"] == turn)
           ):
            status["text"] = "Player " + turn + " wins!"
            i = 0
            while i < len(buttons):
                buttons[i]["state"] = DISABLED
                i = i + 1

        # Check if there is a tie
        if num_turns == 9:
            status["text"] = "It's a tie!"


# Display widgets
status.grid(row=3, column=0, columnspan=3)

button_1.grid(row=0, column=0)
button_2.grid(row=0, column=1)
button_3.grid(row=0, column=2)

button_4.grid(row=1, column=0)
button_5.grid(row=1, column=1)
button_6.grid(row=1, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

root.mainloop()
