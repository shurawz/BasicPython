try:
    import tkinter
except ImportError: #Python2
    import Tkinter as tkinter

keys = [[('C', '1'), ('CE', '1')],
        [('7', '1'), ('8', '1'), ('9', '1'), ('+', '1')],
        [('4', '1'), ('5', '1'), ('6', '1'), ('-', '1')],
        [('1', '1'), ('2', '1'), ('3', '1'), ('*', '1')],
        [('0', '1'), ('=', '1'), ('/', '1')],
        ]

mainWindow = tkinter.Tk()

mainWindow.title("Calculator")
mainWindow.geometry('640x480-8-200')
mainWindow['padx'] = 8

result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, sticky='nsew')

keyPad = tkinter.Frame(mainWindow)
keyPad.grid(row=1, column=0, sticky='nsew')

row = 0
for keyRow in keys:
    col = 0
    for key in keyRow:
        tkinter.Button(keyPad, text=key[0]).grid(row=row, column=col, columnspan=1, sticky=tkinter.E + tkinter.W)
        col += 1
    row += 1

mainWindow.update()
mainWindow.minsize(result.winfo_width() + mainWindow['padx'], result.winfo_height() + keyPad.winfo_height())
mainWindow.maxsize(result.winfo_width() + 50 + mainWindow['padx'], result.winfo_height() + 50 + keyPad.winfo_height())

mainWindow.mainloop()