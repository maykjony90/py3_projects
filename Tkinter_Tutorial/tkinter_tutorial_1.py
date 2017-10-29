
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

class Window(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        
        self.master = master
        
        self.init_window()
        

    # 
    def init_window(self):
        # name of the app that appears on the bar
        self.master.title("GUI TUTORIAL")
        # MISSING
        self.pack(fill=BOTH, expand=1)


        # create a button object with text "quit"
        quitButton = Button(self, text="Quit", width=20, command=self.clientExit)
        # place the button on the top left corner
        # quitButton.place(x=0, y=0)
        # or you can place it at the center
        quitButton.place(relx=.5, rely=.5, anchor="c")

        # create a Menu object, menu
        # this is the main menu of the main window
        menu = Menu(self.master)
        # configure master menu as menu
        # say that menu will be menu instance
        self.master.config(menu=menu)

        # create a Menu object with menu, file
        file = Menu(menu)
		# with demonstration purpose:
        file.add_command(label='Save', command=self.clientSave)
        # add a command to file menu
        file.add_command(label='Exit', command=self.clientExit)
        
        # add file to the menu by cascading
        menu.add_cascade(label='File', menu=file)

        # create a Menu object, edit
        edit = Menu(menu)
        #
        edit.add_command(label='Undo')
        #
        menu.add_cascade(label='Edit', menu=edit)

        # Edit menu
        help_menu = Menu(menu)
        help_menu.add_command(label='FAQ', command=self.openReadme)
        menu.add_cascade(label='Help', menu=help_menu)


        # SHOW IMAGE AND TEXT
        show = Menu(menu)
        show.add_command(label="Show Image", command=self.showImage)
        show.add_command(label="Show Text", command=self.showText)
        menu.add_cascade(label="Showing", menu=show)


    # show Image method
    def showImage(self):
    	load = Image.open("dermoplast-logo.jpg")
    	render = ImageTk.PhotoImage(load)

    	img = Label(self, image=render)
    	img.image = render
    	img.place(x=0, y=0)


    # show Text method
    def showText(self):
    	text = Label(self, text="Hey there motherfucka!")
    	text.pack(fill=X)

        
    # exit function
    def clientExit(self):
        exit()

    # save function
    def clientSave(save):
    	pass

    # open README.txt file
    def openReadme(self):
    	file = open("/home/jony/Documents/python_projects/py3projects/Tkinter_Tutorial/README.txt")
    	content = file.read()
    	messagebox.showinfo("FAQ", content)


# create a Tk object, root
root = Tk()
# decide the initial size of the app window
root.geometry("400x300")

# MISSING
app = Window(root)

# MISSING
root.mainloop()