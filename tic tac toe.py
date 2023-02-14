from tkinter import *

root = Tk()

root.title("Tic Tac Toe")
clicked = True
count = 0
def click(b):
    global clicked, count
    if clicked == True and b["text"] == " ":
        b["text"] = "X"
        clicked = False
        count+=1
    elif clicked == False and b["text"] == " ":
        b["text"] = "O"
        clicked = True
        count +=1
    else:
        messagebox.showerror("Tic Tac Toe", "Box has already been checked")

def win():
    for 

b1 = Button(root, font = (20), height = 3, width = 7, text = " ", command = lambda: click(b1))
b2 = Button(root,font = (20), height = 3, width = 7, text = " ", command = lambda: click(b2))
b3 = Button(root,font = (20), height = 3, width = 7, text = " ", command = lambda: click(b3))

b4 = Button(root,font = (20), height = 3, width = 7, text = " ", command = lambda: click(b4))
b5 = Button(root,font = (20), height = 3, width = 7, text = " ", command = lambda: click(b5))
b6 = Button(root,font = (20), height = 3, width = 7, text = " ", command = lambda: click(b6))

b7 = Button(root,font = (20), height = 3, width = 7, text = " ", command = lambda: click(b7))
b8 = Button(root,font = (20), height = 3, width = 7, text = " ", command = lambda: click(b8))
b9 = Button(root,font = (20), height = 3, width = 7, text = " ", command = lambda: click(b9))

b1.grid(row=0, column = 0)
b2.grid(row=0, column = 1)
b3.grid(row=0, column = 2)

b4.grid(row=1, column = 0)
b5.grid(row=1, column = 1)
b6.grid(row=1, column = 2)

b7.grid(row=2, column = 0)
b8.grid(row=2, column = 1)
b9.grid(row=2, column = 2)
