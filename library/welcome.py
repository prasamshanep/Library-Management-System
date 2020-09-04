from tkinter import *
from tkinter import ttk
import add_book
from PIL import ImageTk,Image

class Admin():
	def __init__(self,window):
		self.win=window
		self.win.title("Library")
		self.win.geometry('1920x1200')
		self.win.config(bg="white")
		self.backg = ImageTk.PhotoImage(file = "background.png")
		self.bg_lbl = Label(self.win,image = self.backg).pack()
		self.heading=Label(self.win,text="Welcome Admin",fg="black",width=40,height=1,font=('algerian',20,'bold'),bg="saddlebrown",activebackground="grey")
		self.heading.place(x=0,y=5,relwidth=1)
		self.show_menu()

	def show_menu(self):
		my_books = Menu(self.win)
		self.win.config(menu=my_books)
		exit_books = Menu(my_books, tearoff = False )
		my_books.add_cascade(label="Exit", menu=exit_books)
		exit_books.add_cascade(label="Logout", command=self.win.quit)


		def btn_add():
			self.add_window=Toplevel(self.win)
			add_book.BookAdd(self.add_window)
		
		self.add=Button(self.win,text="Add Books",fg="black",width=30,height=2,font=('Monotype Corsiva',12,'bold'),bg="saddlebrown",activebackground="grey",command = btn_add)
		self.add.place(x=20,y=160)

		def btn_update():
			self.update_window=Toplevel(self.win)
			add_book.BookUpdate(self.update_window)
	

		self.update=Button(self.win,text="Update Book",fg="black",width=30,height=2,font=('Monotype Corsiva',12,'bold'),bg="saddlebrown",activebackground="grey", command = btn_update)
		self.update.place(x=320,y=160)


		def btn_delete():
			self.delete_window=Toplevel(self.win)
			add_book.BookDelete(self.delete_window)
	
		self.delete=Button(self.win,text="Delete Book",fg="black",width=30,height=2,font=('Monotype Corsiva',12,'bold'),bg="saddlebrown",activebackground="grey", command = btn_delete)
		self.delete.place(x=620,y=160)

		def btn_search():
			self.search_window=Toplevel(self.win)
			add_book.BookSearch(self.search_window)
	
		self.search=Button(self.win,text="Search Book",fg="black",width=30,height=2,font=('Monotype Corsiva',12,'bold'),bg="saddlebrown",activebackground="grey", command = btn_search)
		self.search.place(x=920,y=160)

		def btn_issued():
			self.issued_window=Toplevel(self.win)
			add_book.IssuedView(self.issued_window)

		self.issued=Button(self.win,text="Issued Book",fg="black",width=30,height=2,font=('Monotype Corsiva',12,'bold'),bg="saddlebrown",activebackground="grey",command = btn_issued)
		self.issued.place(x=1220,y=160)

"""

win=Tk()
Admin(win)
win.mainloop()"""