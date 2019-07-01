# Not finished!

import tkinter as tkinter


class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # create widgets
        self.label = tkinter.Label(text='Value Converter')
        self.numberEntry = tkinter.Entry()
        self.convertButton = tkinter.Button(text='Convert', command=self.convert)
        self.output = tkinter.Label()

        # place widgets
        self.label.pack()(side='left')
        self.numberEntry.pack(side='left')
        self.convertButton.pack(side='left')
        self.output.pack(side='left')

    def convert(self):
        entry = self.numberEntry.get()

        try:
            value = float(entry)
            result = round(value * 1.95583, 2)
            self.output.config(
                text=str(value) + ' BGN = ' + str(result) + ' EUR',
                bg='green', fg='white')
        except ValueError:
            self.output.config(text='Not a number', bg='red', fg='black')


# create the application
app = Application()
app.master.title('BGN to EUR Converter')

# start the program
app.mainloop()
