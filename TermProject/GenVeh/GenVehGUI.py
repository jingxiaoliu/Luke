from Tkinter import *
from tkFileDialog import askdirectory
from GenVeh import GenVeh
from ResultPlots import plotData

class GenVehGUI():

    def __init__(self):
        self.window = Tk()
        self.window.resizable(0, 0)
        self.window.title("GenVeh v1.0")
        self.window.wm_iconbitmap('GenVeh.ico')
        self.frame = Frame(self.window)
        self.group = None
        self.resultList = None
        self.entryNumber = None
        self.runButton = None
        self.directory = None
        self.label1 = None
        self.c1 = None
        self.c2 = None
        self.number = IntVar()
        self.pattern = []
        self.agwp = []
        self.gvm = []
        self.parameter = []
        self.CheckVar1 = IntVar()
        self.CheckVar2 = IntVar()
        self.CheckVar3 = IntVar()
        self.CheckVar4 = IntVar()

    def checkSelected(self,c):
        self.pattern.append(c.cget("text"))
        self.resultList.insert(END, c.cget("text"))

    def listSelected(self, event):
        selectedIndex = self.resultList.curselection()
        self.resultIndex = selectedIndex[0]
        plotData(self.gvm[self.resultIndex], self.agwp[self.resultIndex], self.parameter[self.resultIndex])

    def run(self,*args):
        self.agwp, self.gvm, self.parameter = GenVeh(self.number.get(), self.pattern, self.directory)
        self.resultList.bind("<<ListboxSelect>>", self.listSelected)

    def askdirectory(self):
        self.directory = askdirectory()

    def aboutPressed(self):
        aboutWindow = Tk()
        aboutWindow.resizable(0, 0)
        aboutWindow.title("About")
        aboutWindow.wm_iconbitmap('GenVeh.ico')
        Label(aboutWindow, text = "2016 Jingxiao Liu    (jingxial@andrew.cum.edu)").grid(row=0, column=0, pady=5, padx=5)
        aboutWindow.mainloop()

    def createComponents(self):

        menubar = Menu(self.window)
        self.window.config(menu = menubar)

        helpMenu = Menu(menubar)
        menubar.add_cascade(label="Help", menu=helpMenu)
        helpMenu.add_command(label="About", command = self.aboutPressed)

        choice = Frame(self.frame)

        label1 = Label(choice, text = "Number of Vehicles:", anchor = 'w')
        label1.grid(row = 0, column = 1, padx = 5, pady = 5, sticky=W)

        self.entryNumber = Entry(choice, textvariable=self.number, width = 15)
        self.entryNumber.grid(row=1, column=1, columnspan=5, padx = 5, pady = 5)

        self.directoryButton = Button(choice, text="Choose Directory", command = lambda: self.askdirectory())
        self.directoryButton.grid(row=2, column=1, columnspan=5, padx=5, pady=5)

        label2 = Label(choice, text = "Patterns:", anchor = 'w')
        label2.grid(row=3, column=1, padx = 5, columnspan=5, pady = 5, sticky=W)
        self.c1 = Checkbutton(choice, text="123", command=lambda: self.checkSelected(self.c1), variable=self.CheckVar1,
                              onvalue=1, offvalue=0, height=1, width=3, anchor='w')
        self.c1.grid(row=4, column=1, pady=(0, 5))
        self.c2 = Checkbutton(choice, text="122", command=lambda: self.checkSelected(self.c2), variable=self.CheckVar2,
                              onvalue = 1, offvalue = 0, height=1, width = 3, anchor = 'w')
        self.c2.grid(row=4, column=2, pady = (0,5))
        self.c3 = Checkbutton(choice, text="1211", command=lambda: self.checkSelected(self.c3), variable=self.CheckVar3,
                              onvalue=1, offvalue=0, height=1, width=3, anchor='w')
        self.c3.grid(row=5, column=1, pady=(0, 5))
        self.c4 = Checkbutton(choice, text="1133", command=lambda: self.checkSelected(self.c4), variable=self.CheckVar4,
                              onvalue=1, offvalue=0, height=1, width=3, anchor='w')
        self.c4.grid(row=5, column=2, pady=(0, 5))


        self.runButton = Button(choice, text="Run", command = lambda: self.run())
        self.runButton.grid(row=6, column=1, padx=5, columnspan=5, pady=(5,10))

        choice.pack(side = LEFT)

        list = Frame(self.frame)

        label3 = Label(list, text="Select to See Result:")
        label3.grid(row=1, column=1, padx=5, pady=(5,0), sticky=W)
        self.resultList = Listbox(list)
        self.resultList.grid(row=2, column=1, rowspan=3, columnspan=5, padx=5, pady=(0,5), sticky=W)

        list.pack(side = LEFT)

        self.frame.pack(fill=BOTH, expand=1)
