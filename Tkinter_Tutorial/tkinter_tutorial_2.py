from tkinter import *
from tkinter import messagebox

root = Tk()

# ADD FRAME
# topFrame = Frame(root)
# topFrame.pack()


# ADD BUTTON

# bottomFrame = Frame(root)
# bottomFrame.pack(side=BOTTOM)

# button1 = Button(topFrame, text='Button 1', fg='red')
# button2 = Button(topFrame, text='Button 2', fg='green')
# button3 = Button(bottomFrame, text='Button 3', fg='purple')

# button1.pack(side=LEFT)
# button2.pack(side=LEFT)
# button3.pack()

# ADD LABEL

# one = Label(root, text='One', bg='red', fg='white')
# one.pack()
# two = Label(root, text='Two', bg='blue', fg='orange')
# two.pack(fill=X)
# three = Label(root, text='Three', bg='green', fg='yellow')
# three.pack(side=LEFT, fill=Y)

# quitButton = Button(root, text="Quit", bg='yellow', fg='red')
# quitButton.place(relx=.5, rely=.5, anchor="c")

# # GET USER INPUT

# label_1 = Label(root, text='Name')
# label_2 = Label(root, text='Password')
# entry_1 = Entry(root)
# entry_2 = Entry(root)

# label_1.grid(row=0)
# label_2.grid(row=1)

# label_1.grid(row=0, sticky=S)
# label_2.grid(row=1, sticky=S)

# entry_1.grid(row=0, column=1)
# entry_2.grid(row=1, column=1)


# ADD CHECKBUTTON

# c = Checkbutton(root, text="Keep me logged in")
# c.grid(columnspan=2)


# BIND FUNCTION TO BUTTON

# def printName(event):
# 	print("Hello my name is Mayk")

# button_1 = Button(root, text="Print my name")
# button_1.bind("<Button-1>", printName)
# button_1.pack(side=BOTTOM) 


# BIND FUNCTION TO SCREEN(FRAME)

def leftClick(event):
	# print("Left")
	messagebox.showinfo("Button Clicked", "Left")

def middleClick(event):
	messagebox.showinfo("Button Clicked", "Middle")
	# print("Middle")


def rightClick(event):
	# print("Right")
	messagebox.showinfo("Button Clicked", "Right")


frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", middleClick)
frame.bind("<Button-3>", rightClick)
frame.pack()


# decide the initial size of the app window
root.geometry("400x300")

root.mainloop()