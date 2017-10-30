from tkinter import *


class MayksButtons:
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()

		self.printButton = Button(frame, text="Print Message", command=self.printButton)
		self.printButton.pack(side=LEFT)
		self.quitButton = Button(frame, text="Quit", command=frame.quit)
		self.quitButton.pack(side=LEFT)


	def printButton(self):
		print("Hello World")



root = Tk()
app = MayksButtons(root)
root.mainloop()