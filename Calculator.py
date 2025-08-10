from tkinter import *

def setnumber(num):
    eq.set(eq.get()+num)

def calc():
    eq.set(eval(eq.get()))

def sign(s):
    if eq.get()[-1] == "*" or eq.get()[-1] == "/" or eq.get()[-1] == "+" or eq.get()[-1] == "-":
        eq.set(eq.get()[:-1]+s)
    else:
        eq.set(eq.get()+s)


root = Tk()
eq = StringVar()

lbl = Label(textvariable = eq, font=("tahoma", 20, "bold"), fg = "Orange", bg = "Black", padx = 10, pady = 10, width = 21,)
lbl.grid(columnspan = 4)

btn1 = Button(text = "1", width = 5, height = 2, fg = "white", bg = "black", font=("tahoma", 20, "bold"),command=lambda: setnumber("1"))
btn1.grid(row = 1, column = 0)

btn2 = Button(text = "2", width = 5, height = 2, fg = "white", bg = "black", font=("tahoma", 20, "bold"),command=lambda: setnumber("2"))
btn2.grid(row = 1, column = 1)

btn3 = Button(text="3", width = 5, height = 2, fg = "white", bg = "black", font=("tahoma", 20, "bold"),command=lambda: setnumber("3"))
btn3.grid(row = 1, column = 2)

btn4 = Button(text = "4", width=5, height=2, fg="white", bg="black", font=("tahoma", 20, "bold"),command=lambda: setnumber("4"))
btn4.grid(row = 2, column = 0)

btn5 = Button(text = "5", width=5, height=2, fg = "white", bg = "black", font=("tahoma", 20, "bold"),command=lambda: setnumber("5"))
btn5.grid(row = 2, column = 1)

btn6 = Button(text = "6", width = 5, height = 2, fg = "white", bg = "black", font=("tahoma", 20, "bold"),command=lambda: setnumber("6"))
btn6.grid(row = 2, column = 2)

btn7 = Button(text = "7", width = 5, height = 2, fg = "white", bg = "black", font=("tahoma", 20, "bold"),command=lambda: setnumber("7"))
btn7.grid(row = 3, column = 0)

btn8 = Button(text = "8", width = 5, height = 2, fg = "white", bg = "black", font=("tahoma", 20, "bold"),command=lambda: setnumber("8"))
btn8.grid(row = 3, column = 1)

btn9 = Button(text = "9", width = 5, height = 2, fg = "white", bg = "black", font=("tahoma", 20, "bold"),command=lambda: setnumber("9"))
btn9.grid(row = 3, column = 2)

btn10 = Button(text = "0", width = 5, height = 2, fg = "white", bg = "black", font=("tahoma", 20, "bold"),command=lambda: setnumber("0"))
btn10.grid(row = 4, column = 1)

btn11 = Button(text = "C", width = 5, height = 2, fg = "Orange", bg = "black", font=("tahoma", 20, "bold"),command=lambda:eq.set(""))
btn11.grid(row = 4, column = 0)

btn12 = Button(text = "=", width = 5, height = 2, fg = "Orange", bg = "black", font=("tahoma", 20, "bold"),command=calc)
btn12.grid(row = 4, column = 2)

btn13 = Button(text = "÷", width = 5, height = 2, fg = "white", bg = "black", font=("tahoma", 20, "bold"),command=lambda: sign("/"))
btn13.grid(row = 1, column = 3)

btn14 = Button(text = "*", width = 5, height = 2, fg = "white", bg = "black", font=("tahoma", 20, "bold"),command=lambda: sign("*"))
btn14.grid(row = 2, column = 3)

btn15 = Button(text = "+", width = 5, height = 2, fg = "white", bg = "black", font=("tahoma", 20, "bold"),command=lambda: sign("+"))
btn15.grid(row = 3, column = 3)

btn16 = Button(text = "-", width = 5, height = 2, fg = "white", bg = "black", font=("tahoma", 20, "bold"),command=lambda: sign("-"))
btn16.grid(row = 4, column = 3)

root.mainloop()