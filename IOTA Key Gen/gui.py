from tkinter import *
import secrets

class Window(Frame):
    finalSeed = []
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
        genSeedButton = Button(self, text="Genterate IOTA Seed",command=self.generateSeed)
        genSeedButton.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.showResults = StringVar()
        frame=Frame(window)
        frame.pack()
        oneTicket=Label(frame, textvariable=self.showResults).pack()


    def showText(self):
        text = Label(self, "IOTASEED")
        text.pack()


    def client_exit(self):
        exit()
    def generateSeed(self):
        charLib= ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","9"]
        seed = []
        finalSeed = ""

        for i in range(0,secrets.randbelow(10240)):
            for i in range(0,secrets.randbelow(1024)):
                seed.append(secrets.choice(charLib))
            charLib = seed

        while len(finalSeed) < 81:
            finalSeed = finalSeed + seed[secrets.randbelow(1024)]

            self.showResults.set(finalSeed)







root = Tk()
root.geometry("600x400")
app = Window(root)
root.mainloop()
