import tkinter as tk
master=tk.Tk()
master.title("Registery Form")
master.geometry("500x500")

lbl=tk.Label(text="Evalutaion Form", font=("mi sans",30,"normal"), fg="Black")
lbl.pack(pady=(10,10))

lbl_firstname=tk.Label(text="Firstname:", font=("mi sans",30,"normal"),fg="Black", bg="#EDECEB")
lbl_firstname.place(x=100,y=150)

en_firstname=tk.Entry(font=("mi sans",10,"normal"), width=40)
en_firstname.place(x=355,y=170)

lbl_lastname=tk.Label(text="Lastname:", font=("mi sans",30,"normal"), fg="Black", bg="#EDECEB")
lbl_lastname.place(x=100,y=250)

en_lastname=tk.Entry(font=("mi sans",10,"normal"), width=40)
en_lastname.place(x=355,y=270)

lbl_education=tk.Label(text="Education:", font=("mi sans",30,"normal"), fg="Black", bg="#EDECEB")
lbl_education.place(x=100,y=350)

education=tk.StringVar()
r1=tk.Radiobutton(text="Diploma", variable=education, value="Diploma", font=("mi sans",15,"normal"), fg="Black", bg="#EDECEB")
r1.place(x=350,y=360)

r2=tk.Radiobutton(text="Pd Diploma", variable=education, value="Pd Diploma", font=("mi sans",15,"normal"), fg="Black", bg="#EDECEB")
r2.place(x=455,y=360)

r3=tk.Radiobutton(text="Bachelor", variable=education, value="Bachelor", font=("mi sans",15,"normal"), fg="Black", bg="#EDECEB")
r3.place(x=590,y=360)

r4=tk.Radiobutton(text="Master", variable=education, value="Master", font=("mi sans",15,"normal"), fg="Black", bg="#EDECEB")
r4.place(x=700,y=360)

r5=tk.Radiobutton(text="PhD", variable=education, value="PhD", font=("mi sans",15,"normal"), fg="Black", bg="#EDECEB")
r5.place(x=795,y=360)


lbl_gender=tk.Label(text="Gender:", font=("mi sans",30,"normal"),fg="Black",bg="#EDECEB")
lbl_gender.place(x=100,y=450)

gender=tk.StringVar()
rg1=tk.Radiobutton(text="Female", variable=gender, value="Female", font=("mi sans",15,"normal"), fg="Black", bg="#EDECEB")
rg1.place(x=350,y=460)

rg2=tk.Radiobutton(text="Male", variable=gender, value="Male", font=("mi sans",15,"normal"), fg="Black", bg="#EDECEB")
rg2.place(x=455,y=460)


lbl_major=tk.Label(text="Favorite majors:", font=("mi sans",30,"normal"),fg="Black", bg="#EDECEB")
lbl_major.place(x=100,y=550)

field=tk.StringVar()
rf1=tk.Checkbutton(text="Network", variable=education, onvalue="Network", font=("mi sans",15,"normal"),fg="Black",bg="#EDECEB")
rf1.place(x=450,y=560)

rf2=tk.Checkbutton(text="Web", variable=education, onvalue="Web", font=("mi sans",15,"normal"),fg="Black",bg="#EDECEB")
rf2.place(x=560,y=560)

rf3=tk.Checkbutton(text="Basic Algorithm", variable=education, onvalue="Basic Algorithm", font=("mi sans",15,"normal"),fg="Black",bg="#EDECEB")
rf3.place(x=638,y=560)

rf4=tk.Checkbutton(text="Programming", variable=education, onvalue="Programming", font=("mi sans",15,"normal"),fg="Black",bg="#EDECEB")
rf4.place(x=810,y=560)




master.mainloop()