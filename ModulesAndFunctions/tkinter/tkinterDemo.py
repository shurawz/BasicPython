try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)


mainWindow = tkinter.Tk()

mainWindow.title("Tkinter tutorial")
mainWindow.geometry('640x480')

#If line 20 isnot in the program, the program won't run at the moment.
#The reason behind this scenario is:
#We need to pass control over to Tk by calling main method on our top window because main method handles the -->
# --> event processing that the GUI needs in order to function so we actually need add this code

mainWindow.mainloop()