from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(2, "Enter your name: ")

def myClick():
	hello = "Hello, " + e.get() + "!"
	myLabel = Label(root, text=hello, bg='white', fg='blue')
	myLabel.pack()

myButton = Button(root, text='CLICK ME', command=myClick, width=20)
myButton.pack()

root.mainloop()
