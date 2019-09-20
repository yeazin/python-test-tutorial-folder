from tkinter import*
window=Tk()
#all window infomation will be in this
#need to define four labels like title author year and ISBN 
window.title("Yeasin ")
window.minsize(450,200)
window.configure(background='#416383')
but2=Button(window,text='click',width=10,height=3)
but2.pack() #place(x=,y=) #grid=(rows=,column=)
but2.place(x=100,y=50)
print('hey are you')


window.mainloop()
