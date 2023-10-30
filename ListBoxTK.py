from tkinter import *

top = Tk()
Lb = Listbox(top)
Lb.insert(1, 'python')
Lb.insert(2, 'C++')
Lb.insert(3, 'JavaScript')
Lb.insert(4, 'Ruby')
Lb.insert(5, 'PHP')
Lb.pack()
top.mainloop()
