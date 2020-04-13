#NOT USING FRAME

# import tkinter
#
# mainWindow = tkinter.Tk()
#
# mainWindow.title("Hello World")
# mainWindow.geometry('640x480+8+400')
#
# label = tkinter.Label(mainWindow, text="Hello Bhai")
# label.pack(side='top')
#
# canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=1)
# canvas.pack(side='left', fill=tkinter.Y)     # It fills the left side of window with canvas leaving labeled part.
#
# # canvas.pack(side='left', fill=tkinter.X)    # It doesnot return anything means return same thing as # canvas.pack(side='left').
#
# # canvas.pack(side='left', fill=tkinter.X, expand=True) #fills from center left to center right
#
# # canvas.pack(side='left', fill=tkinter.Y, expand=True) #fills from center top to center bottom
#
# # canvas.pack(side='left', fill=tkinter.BOTH, expand=True) #fills whole window screen leaving labeled part
#
# button1 = tkinter.Button(mainWindow, text="Button1")
# button2 = tkinter.Button(mainWindow, text="Button2")
# button3 = tkinter.Button(mainWindow, text="Button3")
# button4 = tkinter.Button(mainWindow, text="Button4")
#
# button1.pack(side='top', anchor='n')
# button2.pack(side='bottom', anchor='s')
# button3.pack(side='right', anchor='e')
# button4.pack(side='left', anchor='w')
#
# mainWindow.mainloop()

# USING FRAME:

import tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry('640x480+8+400')

label = tkinter.Label(mainWindow, text="Hello Bhai")
label.pack(side='top')

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.pack(side='left', anchor='n')     # It fills the left side of window with canvas leaving labeled part.

# canvas.pack(side='left', fill=tkinter.X)    # It doesnot return anything means return same thing as # canvas.pack(side='left').

# canvas.pack(side='left', fill=tkinter.X, expand=True) #fills from center left to center right

# canvas.pack(side='left', fill=tkinter.Y, expand=True) #fills from center top to center bottom

# canvas.pack(side='left', fill=tkinter.BOTH, expand=True) #fills whole window screen leaving labeled part

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right', anchor='n', expand=True)

button1 = tkinter.Button(rightFrame, text="Button1")
button2 = tkinter.Button(rightFrame, text="Button2")
button3 = tkinter.Button(rightFrame, text="Button3")
button4 = tkinter.Button(rightFrame, text="Button4")

button1.pack(side='top', anchor='n')
button2.pack(side='bottom', anchor='s')
button3.pack(side='right', anchor='e')
button4.pack(side='left', anchor='w')

mainWindow.mainloop()