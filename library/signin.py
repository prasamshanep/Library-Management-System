from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector

class SignIn:

	def __init__(self,window):
		global win 

		self.win=window
		self.win.title("Library")
		self.win.geometry('600x400+500+200')
		self.win.config(bg="white")
		self.backg = ImageTk.PhotoImage(file = "back.png")
		self.bg_lbl = Label(self.win,image = self.backg).pack()
		self.update_index = ""

		self.heading=Label(self.win,text="Signin",fg="black",width=40,height=1,font=('algerian',20,'bold'),bg="wheat",activebackground="grey")
		self.heading.place(x=0,y=5,relwidth=1)

		self.name=Label(self.win,text="Full Name",fg="black",width=20,height=2,font=('Monotype Corsiva',12,'bold'),bg="aliceblue",activebackground="grey")
		self.name.place(x=100,y=50)
	
		self.ent_name=Entry(self.win,width=22,font=('Arial',15))
		self.ent_name.place(x=320,y=60)
	
		self.username=Label(self.win,text="Username",fg="black",width=20,height=2,font=('Monotype Corsiva',12,'bold'),bg="aliceblue",activebackground="grey")
		self.username.place(x=100,y=100)

		self.ent_username=Entry(self.win,width=20,font=('Arial',15))
		self.ent_username.place(x=320,y=110)

		self.email=Label(self.win,text="Email",fg="black",width=20,height=2,font=('Monotype Corsiva',12,'bold'),bg="aliceblue",activebackground="grey")
		self.email.place(x=100,y=150)

		self.ent_email=Entry(self.win,width=22,font=('Arial',15))
		self.ent_email.place(x=320,y=160)

		self.number=Label(self.win,text="Contact Number",fg="black",width=20,height=2,font=('Monotype Corsiva',12,'bold'),bg="aliceblue",activebackground="grey")
		self.number.place(x=100,y=200)

		self.ent_number=Entry(self.win,width=20,font=('Arial',15))
		self.ent_number.place(x=320,y=210)
		
		self.password=Label(self.win,text="Password",fg="black",width=20,height=2,font=('Monotype Corsiva',12,'bold'),bg="aliceblue",activebackground="grey")
		self.password.place(x=100,y=250)

		self.ent_password=Entry(self.win,width=30,show="*")
		self.ent_password.place(x=320,y=260)

		self.but_signin=Button (self.win,text="Sign Up",fg="white",width=10,height=2,font=('algerian',10,'bold'),bg="black",activebackground="grey", command = self.get_user)
		self.but_signin.place(x=250,y=300)

	def get_user(self):
		if self.update_index != "":
			messagebox.showerror("Error", "Please enter all value")
		else:
			fullname = self.ent_name.get()
			username = self.ent_username.get()
			gmail = self.ent_email.get()
			number = self.ent_number.get()
			password = self.ent_password.get()

			if self.add_user(username, fullname, password, gmail, number):
				messagebox.showinfo('User', "User Added")
				self.ent_name.delete(0,END)
				self.ent_username.delete(0,END)
				self.ent_email.delete(0,END)
				self.ent_number.delete(0,END)
				self.ent_password.delete(0,END)
			else:
				messagebox.showerror("Error", 'Can not be added')

	def add_user(self,username, fullname, password, gmail, number):
		self.my_connection = mysql.connector.connect(user="root", password="", host="localhost", port=3306, database='collagelibrary')
		self.my_cursor = self.my_connection.cursor()
		qry = "INSERT INTO users (username, fullname, password, gmail, number) VALUES (%s,%s,%s,%s,%s)"
		values = (username, fullname, password, gmail, number)
		self.my_cursor.execute(qry, values)
		self.my_connection.commit()
		return True

"""win=Tk()
SignIn(win)
win.mainloop()"""