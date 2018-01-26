from tkinter import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Lolerwaffles IOTA Seed Generator")
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)
        genSeedButton = Button(self, text="Genterate IOTA Seed",command=self.client_exit)
        genSeedButton.place(relx=0.5, rely=0.5, anchor=CENTER)

    def showText(self):
        text = Label(self, "IOTASEED")
        text.pack()

    def client_exit(self):
        exit()
    def generateSeed(self):
        exit()






root = Tk()
root.geometry("600x400")
app = Window(root)
root.mainloop()
