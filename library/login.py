from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import welcome 
import Student
import signin
import mysql.connector

class loginView:
	def __init__(self,window):
		global win 

		self.win=window
		self.win.title("Library")
		self.win.geometry('600x400+500+200')
		self.win.config(bg="white")
		self.backg = ImageTk.PhotoImage(file = "back.png")
		bg_lbl = Label(self.win,image = self.backg).pack()
		self.heading=Label(self.win,text="Login",fg="black",width=40,height=1,font=('algerian',20,'bold'),bg="wheat",activebackground="grey")
		self.heading.place(x=0,y=5,relwidth=1)

		self.user_name=Label(self.win,text="User Name",fg="black",width=20,height=2,font=('Monotype Corsiva',12,'bold'),bg="aliceblue",activebackground="grey")
		self.user_name.place(x=100,y=200)

	
		self.ent_user=Entry(self.win,width=12,font=('Arial',20))
		self.ent_user.place(x=320,y=200)
	

		self.password=Label(self.win,text="Password",fg="black",width=20,height=2,font=('Monotype Corsiva',12,'bold'),bg="aliceblue",activebackground="grey")
		self.password.place(x=100,y=250)

		
		self.ent_password=Entry(self.win,width=30,show="*")
		self.ent_password.place(x=320,y=270)

		self.but_login=Button (self.win,text="Login",fg="white",width=10,height=2,font=('algerian',10,'bold'),bg="black",activebackground="grey",command = self.login)
		self.but_login.place(x=250,y=300)
	def send(self):
		self.window=Toplevel(self.win)
		welcome.Admin(self.window)
	def login(self):

	    if self.ent_user.get()=="" or self.ent_password.get()=="":
	    	messagebox.showerror("ERROR","fill all the areas")
	    else:
	        self.my_connection = mysql.connector.connect(user="root", password="", host="localhost", port=3306, database='collagelibrary')
	       	self.my_cursor = self.my_connection.cursor()
	       	self.my_cursor.execute("select * from user_admin where username=%s and password=%s",(self.ent_user.get(),self.ent_password.get()))
	        row=self.my_cursor.fetchone()
	        if row==None:
	        	messagebox.showerror("ERROR","INVALID username or password")
	        else:
	        	messagebox.showinfo("SUCESS","WELCOME")
	        	self.send()     	

class Studentlogin(loginView):
	def __init__(self,window):
		super().__init__(window)

		self.but_login=Button (self.win,text="Login",fg="white",width=10,height=2,font=('algerian',10,'bold'),bg="black",activebackground="grey",command = self.login_student)
		self.but_login.place(x=250,y=300)

		def btn_sign():
			self.signin_window=Toplevel(self.win)
			signin.SignIn(self.signin_window)
		
		self.but_sign=Button (self.win,text="SignIn",fg="white",width=10,height=2,font=('algerian',10,'bold'),bg="black",activebackground="grey",command = btn_sign)
		self.but_sign.place(x=100,y=100)

	def send_student(self):
		self.window=Toplevel(self.win)
		Student.StudentWelcome(self.window)

	def login_student(self):

	    if self.ent_user.get()=="" or self.ent_password.get()=="":
	    	messagebox.showerror("ERROR","fill all the areas")
	    else:
	        self.my_connection = mysql.connector.connect(user="root", password="", host="localhost", port=3306, database='collagelibrary')
	       	self.my_cursor = self.my_connection.cursor()
	       	self.my_cursor.execute("select * from users where username=%s and password=%s",(self.ent_user.get(),self.ent_password.get()))
	        row=self.my_cursor.fetchone()
	        if row==None:
	        	Messagebox.showerror("ERROR","INVALID username or password")
	        else:
	        	messagebox.showinfo("SUCESS","WELCOME")
	        	self.send_student()  


"""win=Tk()
loginView(win)
win.mainloop()"""
