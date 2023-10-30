from tkinter import *

main = Tk()
ourMessage = "Agus dan Hizkiel Jomok"
messageVar = Message(main, text=ourMessage)
messageVar.config(bg='lightgreen')
messageVar.pack()
mainloop()