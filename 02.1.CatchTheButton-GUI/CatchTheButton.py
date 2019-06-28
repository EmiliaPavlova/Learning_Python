import tkinter as tkinter
import random


class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # create widgets
        # self.label = tkinter.Label(text='You win')

        # place widgets
        # self.label.pack()(side='left')

        # bind functions to events
        # mouse is over -> move button
        # leave button -> clear text
        self.button.bind('<Enter>', self.on_enter)
        self.button.bind('<Leave>', self.on_leave)

    def on_enter(self, event):
        x = random.randrange(0, 100)
        y = random.randrange(0, 100)
        self.button.pack(side='right', padx=x, pady=y)

    # def on_leave(self, event):

    # def on_click(self):

# https://softuni.bg/forum/18157/catch-the-button


# create the application
app = Application()
app.master.title('BGN to EUR Converter')
app.master.minimize(width=400, height=200)

# start the program
app.mainloop()