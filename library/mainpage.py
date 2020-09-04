from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import login
from PIL import Image, ImageTk
class main:
	def __init__(self,window):
		
		self.win=window
		self.win.title("Library")
		self.win.geometry('600x400+500+200')
		self.win.config(bg="white")
		self.backg = ImageTk.PhotoImage(file = "back.png")
		bg_lbl = Label(self.win,image = self.backg).pack()
		self.student = ImageTk.PhotoImage(file = "student.png")
		self.teacher = ImageTk.PhotoImage(file = "admin.png")
		self.bg_student = Label(self.win, image = self.student)
		self.bg_student.place(x=120,y=120)
		self.bg_teacher = Label(self.win, image = self.teacher)
		self.bg_teacher.place(x=320,y=120)
		self.heading=Label(self.win,text="Library Management System",fg="black",width=40,height=1,font=('algerian',20,'bold'),bg="wheat",activebackground="grey")
		self.heading.place(x=0,y=5,relwidth=1)

		
		self.user_name=Button(self.win,text="Librarian",fg="black",width=20,height=2,font=('Monotype Corsiva',12,'bold'),bg="wheat",activebackground="grey",command=self.btn_login)
		self.user_name.place(x=300,y=250)

		self.password=Button(self.win,text="Student",fg="black",width=20,height=2,font=('Monotype Corsiva',12,'bold'),bg="wheat",activebackground="grey",command=self.btn_login_student)
		self.password.place(x=100,y=250)

	def btn_login(self):
		self.login_window=Toplevel(self.win)
		login.loginView(self.login_window) 

	def btn_login_student(self):
		self.login_window=Toplevel(self.win)
		login.Studentlogin(self.login_window)
		
win=Tk()
main(win)
win.mainloop()