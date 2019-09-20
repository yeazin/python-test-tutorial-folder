
from tkinter import *
window=Tk()
window.title('2nd tutorial')
window.minsize(500,300)
window.configure(background='gray')
meframe=Frame(window,width=200,height=200,bg='black')
meframe.pack(side=RIGHT)
intt=Entry(window,width=10,font=('Times 20 italic'))
intt.place(x=100,y=200)
window.mainloop()
