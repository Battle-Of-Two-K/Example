from tkinter import *

root = Tk()
root.geometry('400x400')

n = 0

def click():
	global n
	button.place_info()
	move = 5
	n += move
	button.place(x = n, y = n)
	button.after(100, click)



button = Button(root, text="CLick", command=click, width=5, height=4)
button.place(x = 0, y = 0)

root.mainloop()