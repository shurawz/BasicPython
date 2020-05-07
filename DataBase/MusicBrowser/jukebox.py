import sqlite3
try:
    import tkinter
except ImportError: # Python 2
    import Tkinter as tkinter

db = sqlite3.connect('music.sqlite')


def tkinter_scrollbar(attribute, row, column, rowspan):
    listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=attribute.yview)
    listScroll.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
    attribute['yscrollcommand'] = listScroll.set



mainWindow = tkinter.Tk()
mainWindow.title('Music DB Browser')
mainWindow.geometry('960x640')

mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=1)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=5)
mainWindow.rowconfigure(3, weight=1)


# Creating Label for each modules
tkinter.Label(mainWindow, text="Artists").grid(row=0, column=0)
tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)

# Creating Listbox

artistList = tkinter.Listbox(mainWindow)
artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
artistList.config(border=2, relief='sunken')
tkinter_scrollbar(artistList, 1, 0, 2)

# Creating album listbox

albumLV = tkinter.Variable(mainWindow)
albumLV.set(("Choose an artist",))
albumList = tkinter.Listbox(mainWindow, listvariable=albumLV)
albumList.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
albumList.config(border=2, relief='sunken')
tkinter_scrollbar(albumList, 1, 1, 1)

# Creating song listbox

songLV = tkinter.Variable(mainWindow)
songLV.set(("Choose an album",))
songList = tkinter.Listbox(mainWindow, listvariable=songLV)
songList.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
songList.config(border=2, relief='sunken')
tkinter_scrollbar(songList, 1, 2, 1)

mainWindow.mainloop()
print("Closing the database connection")

db.close()
