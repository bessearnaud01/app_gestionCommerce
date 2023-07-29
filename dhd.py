from tkinter import *
from tkinter import ttk
         
root = Tk()
w = ttk.Treeview(root, show="headings", columns=('Column1', 'Column2'))
w.heading('#1', text='Column1', anchor=W)
w.heading('#2', text='Column2', anchor=W)

w.column('#1', minwidth = 70, width = 70, stretch = False)
w.column('#2', minwidth = 70, width = 70, stretch = True)  

w.pack(expand=1, fill='x')

mainloop()

