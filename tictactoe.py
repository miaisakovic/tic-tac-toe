import tkinter as tk

root = tk.Tk()
root.title("Tic-tac-toe")

blank_img = tk.PhotoImage(width=100, height=100)


def button_click(pos):
    click(pos)


# Create widgets
status = tk.Label(root, text="X plays", font=("Monaco 15"))

button1 = tk.Button(root, image=blank_img, highlightbackground="#24C0D6",
                    compound="center", width=100, height=100,
                    command=lambda: button_click(0))
button2 = tk.Button(root, image=blank_img, highlightbackground="#24C0D6",
                    compound="center", width=100, height=100,
                    command=lambda: button_click(1))
button3 = tk.Button(root, image=blank_img, highlightbackground="#24C0D6",
                    compound="center", width=100, height=100,
                    command=lambda: button_click(2))

button4 = tk.Button(root, image=blank_img, highlightbackground="#24C0D6",
                    compound="center", width=100, height=100,
                    command=lambda: button_click(3))
button5 = tk.Button(root, image=blank_img, highlightbackground="#24C0D6",
                    compound="center", width=100, height=100,
                    command=lambda: button_click(4))
button6 = tk.Button(root, image=blank_img, highlightbackground="#24C0D6",
                    compound="center", width=100, height=100,
                    command=lambda: button_click(5))

button7 = tk.Button(root, image=blank_img, highlightbackground="#24C0D6",
                    compound="center", width=100, height=100,
                    command=lambda: button_click(6))
button8 = tk.Button(root, image=blank_img, highlightbackground="#24C0D6",
                    compound="center", width=100, height=100,
                    command=lambda: button_click(7))
button9 = tk.Button(root, image=blank_img, highlightbackground="#24C0D6",
                    compound="center", width=100, height=100,
                    command=lambda: button_click(8))

buttons = [button1, button2, button3, button4, button5, button6,
           button7, button8, button9]


def click(pos):
    global turn
    global num_turns

    button = buttons[pos]

    # Check if button has been previously clicked
    if button["state"] == "disabled":
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

        button["state"] = "disabled"

        # Check if there is a winner
        if (
            (button1["text"] == button2["text"] == button3["text"] == turn) or
            (button4["text"] == button5["text"] == button6["text"] == turn) or
            (button7["text"] == button8["text"] == button9["text"] == turn) or
            (button1["text"] == button4["text"] == button7["text"] == turn) or
            (button2["text"] == button5["text"] == button8["text"] == turn) or
            (button3["text"] == button6["text"] == button9["text"] == turn) or
            (button1["text"] == button5["text"] == button9["text"] == turn) or
            (button3["text"] == button5["text"] == button7["text"] == turn)
           ):
            status["text"] = "Player " + turn + " wins!"
            i = 0
            while i < len(buttons):
                buttons[i]["state"] = "disabled"
                i = i + 1

        # Check if there is a tie
        if num_turns == 9:
            status["text"] = "It's a tie!"


# Display widgets
status.grid(row=3, column=0, columnspan=3)

button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)

button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)

button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)

root.mainloop()
