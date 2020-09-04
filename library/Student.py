from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk,Image
import add_book
import studentView

class StudentWelcome:
	def __init__(self,window):
		
		self.win=window
		self.win.title("Library")
		self.win.geometry('1920x1200')
		self.win.config(bg="white")
		self.backg = ImageTk.PhotoImage(file = "background.png")
		bg_lbl = Label(self.win,image = self.backg).pack()

		self.heading=Label(self.win,text="Welcome Student",fg="black",width=40,height=1,font=('algerian',20,'bold'),bg="saddlebrown",activebackground="grey")
		self.heading.place(x=0,y=5,relwidth=1)
		self.show_menu()

	def show_menu(self):
		my_books = Menu(self.win)
		self.win.config(menu=my_books)
		exit_books = Menu(my_books, tearoff = False )
		my_books.add_cascade(label="Exit", menu=exit_books)
		exit_books.add_cascade(label="Logout", command=self.win.quit)

		def btn_view():
			self.view_window=Toplevel(self.win)
			studentView.ViewBook(self.view_window)

		self.view=Button(self.win,text="View Books",fg="black",width=30,height=2,font=('Monotype Corsiva',12,'bold'),bg="saddlebrown",activebackground="grey", command = btn_view)
		self.view.place(x=20,y=160)
		def btn_issue():
			self.issue_window=Toplevel(self.win)
			studentView.IssueBook(self.issue_window)

		self.issue=Button(self.win,text="Issue Book",fg="black",width=30,height=2,font=('Monotype Corsiva',12,'bold'),bg="saddlebrown",activebackground="grey", command = btn_issue)
		self.issue.place(x=320,y=160)

		def btn_return():
			self.delete_window=Toplevel(self.win)
			studentView.ReturnBook(self.delete_window)


		self.update_issue=Button(self.win,text="Return Issue",fg="black",width=30,height=2,font=('Monotype Corsiva',12,'bold'),bg="saddlebrown",activebackground="grey", command = btn_return)
		self.update_issue.place(x=620,y=160)

		def btn_search():
			self.search_window=Toplevel(self.win)
			add_book.BookSearch(self.search_window)

		self.search=Button(self.win,text="Search Book",fg="black",width=30,height=2,font=('Monotype Corsiva',12,'bold'),bg="saddlebrown",activebackground="grey", command = btn_search)
		self.search.place(x=920,y=160)

		def btn_issued():
			self.issued_window=Toplevel(self.win)
			studentView.IssuedView(self.issued_window)

		self.issued_list=Button(self.win,text="Issued Book",fg="black",width=30,height=2,font=('Monotype Corsiva',12,'bold'),bg="saddlebrown",activebackground="grey", command = btn_issued)
		self.issued_list.place(x=1220,y=160)

"""win=Tk()
StudentWelcome(win)
win.mainloop()"""
