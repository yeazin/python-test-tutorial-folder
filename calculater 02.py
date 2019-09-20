class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*font','times 20 bold')
        self.pack(expand=yes,fill=BOTH)
        self.master.title('calculater')


        display = StringVar()
        Entry(self, relief=RIDGE,
              textvariable=display,justify='right' ,bd=30,bg='pink').pack(side=TOP,expand=YES,fill=BOTH)
