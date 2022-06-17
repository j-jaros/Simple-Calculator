from tkinter import *

window = Tk()
input_box = Text(window, bd=0,bg="black", width=8, height=1, font=("Arial", 60), fg="white", highlightthickness=2, highlightcolor="white")
input_box.place(x=20, y=10)
input_box.tag_configure("right-left", justify="right")
input_box.config(state='disabled')

class Calculator:

    def calculate(self):
        self.operation = input_box.get(1.0, END).replace(" ", "")
        self.operation = eval(self.operation)
        result = round(self.operation, 2)
        input_box.config(state='normal')
        input_box.delete(1.0, END)
        input_box.insert(1.0, result, 'right-left')
        input_box.config(state='disabled')

calculator = Calculator()

class Gui:

    def setup(self):
        window.geometry("400x500")
        window.resizable(False, False)
        window.config(background="black")
        window.title("Simple calculator by Julian Jaros")

    def insert_num(self, number):
        length = len(input_box.get(1.0, END).replace(" ", ""))
        print(length)
        if length > 8:
            pass
        else:
            input_box.config(state='normal')
            input_box.insert(END, number, 'right-left')
            input_box.config(state='disabled')

    def clear_window(self):
        input_box.config(state='normal')
        input_box.delete(1.0, END)
        input_box.config(state='disabled')

    def buttons(self):
        button0 = Button(window, width=9, height=1, text="0", font=("Arial", 25, "bold"), bd=0, foreground="white" ,activebackground="grey", background="#333333", command=lambda: self.insert_num(0))
        buttoncomma = Button(window, width=4, height=1, text=",", font=("Arial", 25, "bold"), bd=0, foreground="white" ,activebackground="grey", background="#333333", command=lambda: self.insert_num("."))
        buttonequals = Button(window, width=4, height=1, text="=", font=("Arial", 25, "bold"), bd=0, foreground="white" ,activebackground="grey", background="#333333", command=lambda: calculator.calculate())
        buttonadd = Button(window, width=4, height=1, text="+", font=("Arial", 25, "bold"), bd=0, foreground="white" ,activebackground="grey", background="#333333", command=lambda: self.insert_num("+"))
        buttonsubtract = Button(window, width=4, height=1, text="-", font=("Arial", 25, "bold"), bd=0, foreground="white" ,activebackground="grey", background="#333333", command=lambda: self.insert_num("-"))
        buttonmultiply = Button(window, width=4, height=1, text="*", font=("Arial", 25, "bold"), bd=0, foreground="white" ,activebackground="grey", background="#333333", command=lambda: self.insert_num("*"))
        buttondivision = Button(window, width=4, height=1, text="/", font=("Arial", 25, "bold"), bd=0, foreground="white" ,activebackground="grey", background="#333333", command=lambda: self.insert_num("/"))

        button1 = Button(window, width=4, height=1, text="1", font=("Arial", 25, "bold"), bd=0, foreground="white" ,activebackground="grey", background="#333333", command=lambda:self.insert_num(1))
        button2 = Button(window, width=4, height=1, text="2", font=("Arial", 25, "bold"), bd=0, foreground="white" ,activebackground="grey", background="#333333", command=lambda:self.insert_num(2))
        button3 = Button(window, width=4, height=1, text="3", font=("Arial", 25, "bold"), bd=0, foreground="white" ,activebackground="grey", background="#333333", command=lambda:self.insert_num(3))
        button4 = Button(window, width=4, height=1, text="4", font=("Arial", 25, "bold"), bd=0, foreground="white" ,activebackground="grey", background="#333333", command=lambda:self.insert_num(4))
        button5 = Button(window, width=4, height=1, text="5", font=("Arial", 25, "bold"), bd=0, foreground="white" ,activebackground="grey", background="#333333", command=lambda:self.insert_num(5))
        button6 = Button(window, width=4, height=1, text="6", font=("Arial", 25, "bold"), bd=0, foreground="white" ,activebackground="grey", background="#333333", command=lambda:self.insert_num(6))
        button7 = Button(window, width=4, height=1, text="7", font=("Arial", 25, "bold"), bd=0, foreground="white" ,activebackground="grey", background="#333333", command=lambda:self.insert_num(7))
        button8 = Button(window, width=4, height=1, text="8", font=("Arial", 25, "bold"), bd=0, foreground="white" ,activebackground="grey", background="#333333", command=lambda:self.insert_num(8))
        button9 = Button(window, width=4, height=1, text="9", font=("Arial", 25, "bold"), bd=0, foreground="white" ,activebackground="grey", background="#333333", command=lambda:self.insert_num(9))
        buttonclear = Button(window, width=6, height=1, text="C", font=("Arial", 25, "bold"), bd=0, foreground="white" ,activebackground="grey", background="#333333", command=lambda:self.clear_window()) # Button clear and button clear all working the same way for now!
        buttonclearall = Button(window, width=7, height=1, text="CE", font=("Arial", 25, "bold"), bd=0, foreground="white" ,activebackground="grey", background="#333333", command=lambda:self.clear_window())

        button0.place(x=12, y=420)
        buttoncomma.place(x=210, y=420)
        buttonequals.place(x=302, y=420)
        buttonadd.place(x=302, y=350)
        buttonsubtract.place(x=302, y=280)
        buttonmultiply.place(x=302, y=210)
        buttondivision.place(x=302, y=140)

        button1.place(x=12, y=350)
        button2.place(x=112, y=350)
        button3.place(x=210, y=350)

        button4.place(x=12, y=280)
        button5.place(x=112, y=280)
        button6.place(x=210, y=280)

        button7.place(x=12, y=210)
        button8.place(x=112, y=210)
        button9.place(x=210, y=210)
        buttonclearall.place(x=12, y=140)
        buttonclear.place(x=170, y=140)

gui = Gui()
gui.setup()

gui.buttons()

window.mainloop()

