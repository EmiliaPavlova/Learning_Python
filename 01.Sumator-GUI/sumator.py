# Not finished!

import tkinter as tkinter


class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # create widgets
        self.firstNumberEntry = tkinter.Entry()
        self.plusSign = tkinter.Label(text='+')
        self.secondNumberEntry = tkinter.Entry()
        self.equalSign = tkinter.Label(text='=')
        self.resultLabel = tkinter.Label(text='Result...', bg='green', fg='white')
        self.calculateButton = tkinter.Button(text='Calculate')

        # place widgets
        self.firstNumberEntry.pack(side='left')
        self.plusSign.pack(side='left')
        self.secondNumberEntry.pack(side='left')
        self.equalSign.pack(side='left')
        self.resultLabel.pack(side='left')
        self.calculateButton.pack(side='left')
        tkinter.Button(text='Calculate', command=self.calculate)

    def calculate(self):
        result = 'Not number/s'
        bg = 'red'
        fg = 'black'
        try:
            first_value = float(self.firstNumberEntry.get())
            second_value = float(self.secondNumberEntry.get())
            result = str(first_value + second_value)
            bg = 'green'
            fg = 'white'
        finally:
            self.resultLabel.config(text=result, bg=bg, fg=fg)
            print(result)


# create the application
app = Application()
app.master.title('Sumator')
app.master.minsize(width=300, height=100)

# start the program
app.mainloop()




