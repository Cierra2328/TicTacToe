from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("Tic Tac Toe")
count = 0
def click(b):
    global count
    if count %2 == 0 and b["text"] == " ":
        b["text"] = "X"
        count+=1
        win()
    elif b["text"] == " ":
        b["text"] = "O"
        count +=1
        win()
    else:
        messagebox.showerror("Tic Tac Toe", "Box has already been checked")

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

def disableButtons():
    b1.config(state = DISABLED)
    b2.config(state = DISABLED)
    b3.config(state = DISABLED)
    b4.config(state = DISABLED)
    b5.config(state = DISABLED)
    b6.config(state = DISABLED)
    b7.config(state = DISABLED)
    b8.config(state = DISABLED)
    b9.config(state = DISABLED)
    
def win():
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="red") 
        b2.config(bg="red")
        b3.config(bg="red")
        disableButtons()
        messagebox.info("Tic Tac Toe", "X Wins")
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        disableButtons()
        messagebox.info("Tic Tac Toe", "X Wins")    
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg = "red") 
        b8.config(bg = "red")
        b9.config(bg = "red")
        disableButtons()
        messagebox.info("Tic Tac Toe", "X Wins")    
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b4.config(bg = "red") 
        b1.config(bg = "red")
        b7.config(bg = "red")
        disableButtons()
        messagebox.info("Tic Tac Toe", "X Wins")
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg = "red") 
        b5.config(bg = "red")
        b8.config(bg = "red")
        disableButtons()
        messagebox.showinfo("Tic Tac Toe", "X Wins")
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg = "red") 
        b6.config(bg = "red")
        b9.config(bg = "red")
        disableButtons()
        messagebox.showinfo("Tic Tac Toe", "X Wins")
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg = "red") 
        b5.config(bg = "red")
        b9.config(bg = "red")
        disableButtons()
        messagebox.showinfo("Tic Tac Toe", "X Wins")
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg = "red") 
        b5.config(bg = "red")
        b7.config(bg = "red")
        disableButtons()
        messagebox.showinfo("Tic Tac Toe", "X Wins")
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg = "red") 
        b2.config(bg = "red")
        b3.config(bg = "red")
        disableButtons()
        messagebox.showinfo("Tic Tac Toe", "O Wins")
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg = "red") 
        b5.config(bg = "red")
        b6.config(bg = "red")
        disableButtons()
        messagebox.showinfo("Tic Tac Toe", "O Wins")
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg = "red") 
        b8.config(bg = "red")
        b9.config(bg = "red")
        disableButtons()
        messagebox.showinfo("Tic Tac Toe", "O Wins")
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b4.config(bg = "red") 
        b1.config(bg = "red")
        b7.config(bg = "red")
        disableButtons()
        messagebox.showinfo("Tic Tac Toe", "O Wins")
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg = "red") 
        b5.config(bg = "red")
        b8.config(bg = "red")
        disableButtons()
        messagebox.showinfo("Tic Tac Toe", "O Wins")
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg = "red") 
        b6.config(bg = "red")
        b9.config(bg = "red")
        disableButtons()
        messagebox.showinfo("Tic Tac Toe", "O Wins")
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg = "red") 
        b5.config(bg = "red")
        b9.config(bg = "red")
        disableButtons()
        messagebox.showinfo("Tic Tac Toe", "O Wins")
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg = "red") 
        b5.config(bg = "red")
        b7.config(bg = "red")
        disableButtons()
        messagebox.showinfo("Tic Tac Toe", "O Wins")






    
