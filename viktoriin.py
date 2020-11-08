from tkinter import *
from tkinter import messagebox

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.width = 600
        self.height = 400
        self.frame = None
        self.resizable(False, False)
        self.switch_frame(MainPage)

    def switch_frame(self, frame_to_switch):
        if self.frame != None:
            self.frame.destroy()
        self.frame = frame_to_switch(self)
        self.frame.pack(fill="both", expand=True)

# Esimene leht
class MainPage(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        Frame.configure(self, bg="black")
        Label(self, text="Team Helmi viktoriin", font=("Arial", 20, "bold"), bg="black", fg="pink").pack(side="top", pady=30)
        Label(self, text="Viktoriin koosneb 10st küsimusest. \n Peale vastamist saad teada, \n mitu punkti suutsid koguda.", font=("Arial", 15), bg="black", fg="pink").pack(pady=40)
        Button(self, text="Alusta", command=lambda: parent.switch_frame(PageTwo)).place(anchor="center", x=parent.width/2, y=(parent.height/2)+100)

score = 0

# Küsimused..
class PageTwo(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        Frame.configure(self, bg="black")
        Label(self, text="1. küsimus", font=("Arial", 20, "bold"), bg="black", fg="pink").pack(side="top")
        Label(self, text="Kes on Team Helmi suurim väravakütt?", font=("Arial", 15), bg="black", fg="pink").pack(side="top", pady=40)
        def kontrolli():
            if var.get() == "True":
                global score
                score += 1
                messagebox.showinfo("Tubli!", "Õige vastus!")
            else:
                messagebox.showinfo("Pole hullu..", "Vale vastus!")
        var = StringVar()
        Radiobutton(self, text="(A) Karl Erik Ott", variable=var, value="False1", tristatevalue=0).pack(side=TOP, ipady=5)
        Radiobutton(self, text="(B) Marcus Saksing", variable=var, value="False2", tristatevalue=0).pack(side=TOP, ipady=5)
        Radiobutton(self, text="(C) Renee Püvi", variable=var, value="True", tristatevalue=0).pack(side=TOP, ipady=5)
        Radiobutton(self, text="(D) Karl Sten Kõks", variable=var, value="False3", tristatevalue=0).pack(side=TOP, ipady=5)
        Button(self, text="Kontrolli vastust!", command=lambda: [kontrolli(), parent.switch_frame(PageThree)]).pack(side="bottom", pady=20)

class PageThree(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        Frame.configure(self, bg="black")
        Label(self, text="2. küsimus", font=("Arial", 20, "bold"), bg="black", fg="pink").pack(side="top")
        Label(self, text="Kellel on Team Helmi eest kõige rohkem mänge?", font=("Arial", 15), bg="black", fg="pink").pack(side="top", pady=40)
        def kontrolli():
            if var.get() == "True":
                global score
                score += 1
                messagebox.showinfo("Tubli!", "Õige vastus!")
            else:
                messagebox.showinfo("Pole hullu..", "Vale vastus!")
        var = StringVar()
        Radiobutton(self, text="(A) Kristofer Johan Arro", variable=var, value="True", tristatevalue=0).pack(side=TOP, ipady=5)
        Radiobutton(self, text="(B) Aaron Kants", variable=var, value="False2", tristatevalue=0).pack(side=TOP, ipady=5)
        Radiobutton(self, text="(C) Renee Püvi", variable=var, value="False1", tristatevalue=0).pack(side=TOP, ipady=5)
        Radiobutton(self, text="(D) Frederik Mathias Helm", variable=var, value="False3", tristatevalue=0).pack(side=TOP, ipady=5)
        Button(self, text="Järgmine küsimus", command=lambda: [kontrolli(), parent.switch_frame(LastPage)]).pack(side="bottom", pady=20)


class LastPage(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        Frame.configure(self, bg="black")
        Label(self, text="Mäng läbi!", font=("Arial", 25, "bold"), bg="black", fg="pink").pack(side=TOP, pady=20)
        global score
        Label(self, text=("Suutsid koguda", score, "punkti."), font=("Arial", 15), bg="black", fg="pink").pack(side=TOP, pady=30)

app = App()
app.geometry("600x400")
app.mainloop()
