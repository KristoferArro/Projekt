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
        Button(self, text="Järgmine küsimus", command=lambda: [kontrolli(), parent.switch_frame(PageFour)]).pack(side="bottom", pady=20)

class PageFour(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        Frame.configure(self, bg="black")
        Label(self, text="3. küsimus", font=("Arial", 20, "bold"), bg="black", fg="pink").pack(side="top")
        Label(self, text="Mitu väravat on Renee Püvi Team Helmi eest löönud?", font=("Arial", 15), bg="black", fg="pink").pack(side="top", pady=40)
        def kontrolli():
            if var.get() == "True":
                global score
                score += 1
                messagebox.showinfo("Tubli!", "Õige vastus!")
            else:
                messagebox.showinfo("Pole hullu..", "Vale vastus!")
        var = StringVar()
        Radiobutton(self, text="(A) 42", variable=var, value="False1", tristatevalue=0).pack(side=TOP, ipady=5)
        Radiobutton(self, text="(B) 38", variable=var, value="False2", tristatevalue=0).pack(side=TOP, ipady=5)
        Radiobutton(self, text="(C) 36", variable=var, value="False3", tristatevalue=0).pack(side=TOP, ipady=5)
        Radiobutton(self, text="(D) 34", variable=var, value="True", tristatevalue=0).pack(side=TOP, ipady=5)
        Button(self, text="Kontrolli vastust!", command=lambda: [kontrolli(), parent.switch_frame(PageFive)]).pack(side="bottom", pady=20)

class PageFive(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        Frame.configure(self, bg="black")
        Label(self, text="4. küsimus", font=("Arial", 20, "bold"), bg="black", fg="pink").pack(side="top")
        Label(self, text="Mitu erinevat mängijat on Team Helmi eest mänginud?", font=("Arial", 15), bg="black", fg="pink").pack(side="top", pady=40)
        def kontrolli():
            if var.get() == "True":
                global score
                score += 1
                messagebox.showinfo("Tubli!", "Õige vastus!")
            else:
                messagebox.showinfo("Pole hullu..", "Vale vastus!")
        var = StringVar()
        Radiobutton(self, text="(A) 25", variable=var, value="False1", tristatevalue=0).pack(side=TOP, ipady=5)
        Radiobutton(self, text="(B) 32", variable=var, value="False2", tristatevalue=0).pack(side=TOP, ipady=5)
        Radiobutton(self, text="(C) 42", variable=var, value="True", tristatevalue=0).pack(side=TOP, ipady=5)
        Radiobutton(self, text="(D) 48", variable=var, value="False3", tristatevalue=0).pack(side=TOP, ipady=5)
        Button(self, text="Kontrolli vastust!", command=lambda: [kontrolli(), parent.switch_frame(PageSix)]).pack(side="bottom", pady=20)

class PageSix(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        Frame.configure(self, bg="black")
        Label(self, text="5. küsimus", font=("Arial", 20, "bold"), bg="black", fg="pink").pack(side="top")
        Label(self, text="Kui palju mänge on mänginud Team Helmi eest \n klubi ikoon Frederik Mathias Helm?", font=("Arial", 15), bg="black", fg="pink").pack(side="top", pady=40)
        def kontrolli():
            if var.get() == "True":
                global score
                score += 1
                messagebox.showinfo("Tubli!", "Õige vastus!")
            else:
                messagebox.showinfo("Pole hullu..", "Vale vastus!")
        var = StringVar()
        Radiobutton(self, text="(A) 52", variable=var, value="True", tristatevalue=0).pack(side=TOP, ipady=5)
        Radiobutton(self, text="(B) 50", variable=var, value="False1", tristatevalue=0).pack(side=TOP, ipady=5)
        Radiobutton(self, text="(C) 47", variable=var, value="False2", tristatevalue=0).pack(side=TOP, ipady=5)
        Radiobutton(self, text="(D) 59", variable=var, value="False3", tristatevalue=0).pack(side=TOP, ipady=5)
        Button(self, text="Kontrolli vastust!", command=lambda: [kontrolli(), parent.switch_frame(PageSeven)]).pack(side="bottom", pady=20)

class PageSeven(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        Frame.configure(self, bg="black")
        Label(self, text="6. küsimus", font=("Arial", 20, "bold"), bg="black", fg="pink").pack(side="top")
        Label(self, text="Kes on viimati Team Helmiga liitunud mängija?", font=("Arial", 15), bg="black", fg="pink").pack(side="top", pady=40)
        def kontrolli():
            if var.get() == "True":
                global score
                score += 1
                messagebox.showinfo("Tubli!", "Õige vastus!")
            else:
                messagebox.showinfo("Pole hullu..", "Vale vastus!")
        var = StringVar()
        Radiobutton(self, text="(A) Rico Reinoja", variable=var, value="True", tristatevalue=0).pack(side=TOP, ipady=5)
        Radiobutton(self, text="(B) Kristjan Põldmaa", variable=var, value="False1", tristatevalue=0).pack(side=TOP, ipady=5)
        Radiobutton(self, text="(C) Mikk Toom", variable=var, value="False2", tristatevalue=0).pack(side=TOP, ipady=5)
        Radiobutton(self, text="(D) Joonas Salu", variable=var, value="False3", tristatevalue=0).pack(side=TOP, ipady=5)
        Button(self, text="Kontrolli vastust!", command=lambda: [kontrolli(), parent.switch_frame(PageEight)]).pack(side="bottom", pady=20)

class PageEight(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        Frame.configure(self, bg="black")
        Label(self, text="7. küsimus", font=("Arial", 20, "bold"), bg="black", fg="pink").pack(side="top")
        Label(self, text="Mitu mängijat on löönud 10 või rohkem väravat?", font=("Arial", 15), bg="black", fg="pink").pack(side="top", pady=40)
        def kontrolli():
            if var.get() == "True":
                global score
                score += 1
                messagebox.showinfo("Tubli!", "Õige vastus!")
            else:
                messagebox.showinfo("Pole hullu..", "Vale vastus!")
        var = StringVar()
        Radiobutton(self, text="(A) 5", variable=var, value="False1", tristatevalue=0).pack(side=TOP, ipady=5)
        Radiobutton(self, text="(B) 6", variable=var, value="False2", tristatevalue=0).pack(side=TOP, ipady=5)
        Radiobutton(self, text="(C) 7", variable=var, value="False3", tristatevalue=0).pack(side=TOP, ipady=5)
        Radiobutton(self, text="(D) 8", variable=var, value="True", tristatevalue=0).pack(side=TOP, ipady=5)
        Button(self, text="Kontrolli vastust!", command=lambda: [kontrolli(), parent.switch_frame(PageNine)]).pack(side="bottom", pady=20)

class PageNine(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        Frame.configure(self, bg="black")
        Label(self, text="8. küsimus", font=("Arial", 20, "bold"), bg="black", fg="pink").pack(side="top")
        Label(self, text="Mitmel mängijal on üle 50 mängu Team Helmi eest?", font=("Arial", 15), bg="black", fg="pink").pack(side="top", pady=40)
        def kontrolli():
            if var.get() == "True":
                global score
                score += 1
                messagebox.showinfo("Tubli!", "Õige vastus!")
            else:
                messagebox.showinfo("Pole hullu..", "Vale vastus!")
        var = StringVar()
        Radiobutton(self, text="(A) 4", variable=var, value="False1", tristatevalue=0).pack(side=TOP, ipady=5)
        Radiobutton(self, text="(B) 5", variable=var, value="False2", tristatevalue=0).pack(side=TOP, ipady=5)
        Radiobutton(self, text="(C) 6", variable=var, value="True", tristatevalue=0).pack(side=TOP, ipady=5)
        Radiobutton(self, text="(D) 7", variable=var, value="False3", tristatevalue=0).pack(side=TOP, ipady=5)
        Button(self, text="Kontrolli vastust!", command=lambda: [kontrolli(), parent.switch_frame(PageTen)]).pack(side="bottom", pady=20)

class PageTen(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        Frame.configure(self, bg="black")
        Label(self, text="9. küsimus", font=("Arial", 20, "bold"), bg="black", fg="pink").pack(side="top")
        Label(self, text="Märgi kõik mängijad, kes on Team Helmi eest värava löönud!", font=("Arial", 15), bg="black", fg="pink").pack(side="top", pady=40)
        def kontrolli():
            if var1.get() == 1 and var2.get() == 1 and var3.get() == 1:
                global score
                score += 1
                messagebox.showinfo("Tubli!", "Õige vastus!")
            else:
                messagebox.showinfo("Pole hullu..", "Vale või osaliselt vale vastus!")
        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        Checkbutton(self, text="Robin Sova", variable=var1, onvalue=1, offvalue=0).pack(side=TOP, ipady=5)
        Checkbutton(self, text="Aksel Arna", variable=var2, onvalue=1, offvalue=0).pack(side=TOP, ipady=5)
        Checkbutton(self, text="Joonas Raidvee", variable=var3, onvalue=1, offvalue=0).pack(side=TOP, ipady=5)
        Checkbutton(self, text="Sander Künnapuu", variable=var4, onvalue=1, offvalue=0).pack(side=TOP, ipady=5)
        Button(self, text="Kontrolli vastust!", command=lambda: [kontrolli(), parent.switch_frame(PageEleven)]).pack(side="bottom", pady=20)

class PageEleven(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        Frame.configure(self, bg="black")
        Label(self, text="10. küsimus", font=("Arial", 20, "bold"), bg="black", fg="pink").pack(side="top")
        Label(self, text="Kes järgnevatest mängijatest \n on löönud üle 5 värava Team Helmi eest?", font=("Arial", 15), bg="black", fg="pink").pack(side="top", pady=40)
        def kontrolli():
            if var2.get() == 1 and var4.get() == 1:
                global score
                score += 1
                messagebox.showinfo("Tubli!", "Õige vastus!")
            else:
                messagebox.showinfo("Pole hullu..", "Vale või osaliselt vale vastus!")
        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        Checkbutton(self, text="Karl Sten Kõks", variable=var1, onvalue=1, offvalue=0).pack(side=TOP, ipady=5)
        Checkbutton(self, text="Sass Vedler", variable=var2, onvalue=1, offvalue=0).pack(side=TOP, ipady=5)
        Checkbutton(self, text="Kristjan Põldmaa", variable=var3, onvalue=1, offvalue=0).pack(side=TOP, ipady=5)
        Checkbutton(self, text="Jakob Mägi", variable=var4, onvalue=1, offvalue=0).pack(side=TOP, ipady=5)
        Button(self, text="Kontrolli vastust!", command=lambda: [kontrolli(), parent.switch_frame(LastPage)]).pack(side="bottom", pady=20)


class LastPage(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        Frame.configure(self, bg="black")
        Label(self, text="Mäng läbi!", font=("Arial", 25, "bold"), bg="black", fg="pink").pack(side=TOP, pady=20)
        global score
        Label(self, text=("Suutsid koguda"), font=("Arial", 18), bg="black", fg="pink").pack(side=TOP, pady=30)
        Label(self, text=score, font=("Arial", 25), bg="black", fg="pink").pack(side=TOP, pady=20)
        Label(self, text="punkti.", font=("Arial", 18), bg="black", fg="pink").pack(side=TOP, pady=20)

app = App()
app.geometry("600x400")
app.mainloop()
