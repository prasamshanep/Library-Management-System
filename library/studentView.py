from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class ViewBook():
	def __init__(self,window):
		self.win=window
		self.win.geometry('600x500+20+270')
		self.win.title("Library")
		self.win.config(bg="slategray")
		self.win.wm_attributes("-transparentcolor", "slategray")
		self.book = Book()
		self.frame = Frame(self.win, bd = 4, relief = RIDGE)
		self.frame.place(x=50, y=100)
		self.sbar = Scrollbar(self.frame, orient = HORIZONTAL)
		self.sbary = Scrollbar(self.frame, orient = VERTICAL)
		self.book_tree = ttk.Treeview(self.frame, columns=('name', 'author','bookid'),xscrollcommand=self.sbar.set, yscrollcommand=self.sbary.set)

		self.sbar.pack(side=BOTTOM, fill=X)
		self.sbary.pack(side=RIGHT, fill=Y)
		self.sbar.config(command=self.book_tree.xview)
		self.sbary.config(command=self.book_tree.yview)
		self.book_tree['show'] = 'headings'
		self.book_tree.column('name', width=150)
		self.book_tree.column('bookid', width=150)
		self.book_tree.column('author', width=150)
		self.book_tree.heading('name', text="Book Name")
		self.book_tree.heading('bookid', text="Book ID")
		self.book_tree.heading('author', text="Author Name")
		self.book_tree.pack(fill = BOTH, expand = 1)
		self.show_book_tree()
	def show_book_tree(self):
		self.book_tree.delete(*self.book_tree.get_children())
		data = self.book.show_book()
		for i in data:
			self.book_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3]))

class IssueBook():
	def __init__(self,window):
		self.win=window
		self.win.geometry('1000x500+320+270')
		self.win.title("Library")
		self.win.config(bg="slategray") 
		self.win.wm_attributes("-transparentcolor", "slategray")
		self.update_index = ""
		self.book = Book()
		self.heading=Label(self.win,text="Issue Book",fg="black",width=40,height=1,font=('algerian',20,'bold'),bg="saddlebrown",activebackground="grey")
		self.heading.place(x=0,y=5,relwidth=1)

		self.book_name=Label(self.win,text="Book Name",fg="black",width=20,height=2,font=('Monotype Corsiva',12,'bold'),bg="saddlebrown",activebackground="grey")
		self.book_name.place(x=50,y=100)
		self.entry_name=Entry(self.win,font=('Arial',15,'bold'))
		self.entry_name.place(x=300,y=100)

		self.book_id=Label(self.win,text="Book ID",fg="black",width=20,height=2,font=('Monotype Corsiva',12,'bold'),bg="saddlebrown",activebackground="grey")
		self.book_id.place(x=50,y=150)
		self.entry_id=Entry(self.win,font=('Arial',15,'bold'))
		self.entry_id.place(x=300,y=150)

		self.book_username=Label(self.win,text="username",fg="black",width=20,height=2,font=('Monotype Corsiva',12,'bold'),bg="saddlebrown",activebackground="grey")
		self.book_username.place(x=50,y=200)
		self.entry_username=Entry(self.win,font=('Arial',15,'bold'))
		self.entry_username.place(x=300,y=200)

		self.issue_date=Label(self.win,text="Issued date",fg="black",width=20,height=2,font=('Monotype Corsiva',12,'bold'),bg="saddlebrown",activebackground="grey")
		self.issue_date.place(x=50,y=250)
		self.entry_date=Entry(self.win,font=('Arial',15,'bold'))
		self.entry_date.place(x=300,y=250)

		self.frame = Frame(self.win, bd = 4, relief = RIDGE)
		self.frame.place(x=550, y=100)
		self.sbar = Scrollbar(self.frame, orient = HORIZONTAL)
		self.sbary = Scrollbar(self.frame, orient = VERTICAL)
		self.book_tree = ttk.Treeview(self.frame, columns=('name', 'bookid'),xscrollcommand=self.sbar.set, yscrollcommand=self.sbary.set)

		self.sbar.pack(side=BOTTOM, fill=X)
		self.sbary.pack(side=RIGHT, fill=Y)
		self.sbar.config(command=self.book_tree.xview)
		self.sbary.config(command=self.book_tree.yview)
		self.book_tree['show'] = 'headings'
		self.book_tree.column('name', width=200)
		self.book_tree.column('bookid', width=100)
		self.book_tree.heading('name', text="Book Name")
		self.book_tree.heading('bookid', text="Book ID")
		self.book_tree.pack(fill = BOTH, expand = 1)
		self.show_book_tree()


		self.item_add=Button(self.win,text="Issue",fg="white",width=20,height=2,font=('algerian',10,'bold'),bg="black",activebackground="grey", command = self.issueBook)
		self.item_add.place(x=200,y=300)

		self.show_book_tree()

	def show_book_tree(self):
		self.book_tree.delete(*self.book_tree.get_children())
		data = self.book.show_book()
		for i in data:
			self.book_tree.insert("", "end", value=(i[1], i[0]))
		self.book_tree.bind("<Double-1>", self.on_book_select)

	def on_book_select(self, event):
		selected_row = self.book_tree.selection()[0]
		selected_book = self.book_tree.index(selected_row)
		all_books = self.book.show_book()
		selected_item = all_books[selected_book]
		self.selected_row = selected_item[0]
		self.entry_name.delete(0, END)
		self.entry_name.insert(0, selected_item[1])
		self.entry_id.delete(0, END)
		self.entry_id.insert(0, selected_item[0])

	def issueBook(self):
		bookname = self.entry_name.get()
		bookid = self.entry_id.get()
		username = self.entry_username.get()
		issuedate = self.entry_date.get()
		try:
			if bookname == "" or bookid == "" or username == "" or issuedate == "":
				 messagebox.showerror("Error", 'Please insert all information')

			else:
				self.book.issue_book(bookname, bookid, username, issuedate)
				messagebox.showinfo("Issued", "Book issued")
				self.upadate_index = ""
				self.entry_name.delete(0,END)
				self.entry_id.delete(0,END)
				self.entry_username.delete(0,END)
				self.entry_date.delete(0,END)
		except:
			messagebox.showerror("Error", 'Try Again')


class IssuedView():
	def __init__(self,window):
		self.win=window
		self.win.geometry('1000x500+500+270')
		self.win.title("Library")
		self.win.config(bg="slategray") 
		self.win.wm_attributes("-transparentcolor", "slategray")
		self.update_index = ""
		self.book = Book()
		self.heading=Label(self.win,text="Issued Book View",fg="black",width=40,height=1,font=('algerian',20,'bold'),bg="saddlebrown",activebackground="grey")
		self.heading.place(x=0,y=5,relwidth=1)
		self.book_username=Label(self.win,text="username",fg="black",width=20,height=2,font=('Monotype Corsiva',12,'bold'),bg="saddlebrown",activebackground="grey")
		self.book_username.place(x=50,y=200)
		self.entry_username=Entry(self.win,font=('Arial',15,'bold'))
		self.entry_username.place(x=250,y=210)
		self.item_show = Button(self.win,text="View",fg="white",width=20,height=2,font=('algerian',10,'bold'),bg="black",activebackground="grey", command = self.show_issued)
		self.item_show.place(x=200,y=300)

		self.book_tree = ttk.Treeview(self.win, columns=('id', 'bookid', 'bookname', 'username', 'issuedate','fine'))
		self.book_tree.place(x=500, y=100)
		self.book_tree['show'] = 'headings'
		self.book_tree.column('id', width=80)
		self.book_tree.column('bookid', width=80)
		self.book_tree.column('bookname', width=80)
		self.book_tree.column('username', width=80)
		self.book_tree.column('issuedate', width=80)
		self.book_tree.column('fine', width=80)
		self.book_tree.heading('id', text="Issue ID")
		self.book_tree.heading('bookid', text="Book Name")
		self.book_tree.heading('bookname', text="BookID")
		self.book_tree.heading('username', text="Username")
		self.book_tree.heading('issuedate', text="IssueDate")
		self.book_tree.heading('fine', text="Fine")

	def show_issued(self):
		self.my_connection = mysql.connector.connect(user="root", password="", host="localhost", port=3306, database='collagelibrary')
		self.my_cursor = self.my_connection.cursor() 
		selected = self.entry_username.get()
		if selected == "":
			test = Label(self.win, text = "Please insert your username")
			test.place(x=350, y=200)
		else:
			sql = "SELECT * FROM issue WHERE username = %s"
		username = (selected,)
		result = self.my_cursor.execute(sql, username)
		result = self.my_cursor.fetchall()
		if len(result)!=0:
			self.book_tree.delete(*self.book_tree.get_children())
			for row in result:
				self.book_tree.insert('',END,values=row)
		if not result:
			messagebox.showerror("Error", "No data found")

class ReturnBook(IssuedView):

	def __init__(self,window):

		super().__init__(window)
		self.heading=Label(self.win,text="Return Book",fg="black",width=40,height=1,font=('algerian',20,'bold'),bg="saddlebrown",activebackground="grey")
		self.heading.place(x=0,y=5,relwidth=1)
		self.book_id=Label(self.win,text="Book ID",fg="black",width=20,height=2,font=('Monotype Corsiva',12,'bold'),bg="saddlebrown",activebackground="grey")
		self.book_id.place(x=50,y=250)
		self.entry_bookid=Entry(self.win,font=('Arial',15,'bold'))
		self.entry_bookid.place(x=250,y=260)
		self.book_add=Button(self.win,text="Return",fg="white",width=15,height=2,font=('algerian',10,'bold'),bg="black",activebackground="grey", command = self.delete_book)
		self.book_add.place(x=210,y=350)

	def delete_book(self):
		bookid = self.entry_bookid.get()
		if bookid == "":
			messagebox.showerror('Error' , 'Insert BOOKID')
		else:
			self.book.delete_books(bookid)
			messagebox.showinfo('Book', "Book Returned")

class Book (object):
    def __init__(self):
        self.my_connection = mysql.connector.connect(user="root", password="", host="localhost", port=3306, database='collagelibrary')
        self.my_cursor = self.my_connection.cursor() 

    def show_book(self):
        all_books = []
        qry = "SELECT * FROM Bookss"
        self.my_cursor.execute(qry)
        all_books = self.my_cursor.fetchall()
        return all_books

    def issue_book(self, bookname, bookid, username, issuedate):
        qry = "INSERT INTO issue ( bookname, bookid, username, issuedate) VALUES (%s,%s,%s,%s)"
        values = (bookname, bookid, username, issuedate)
        self.my_cursor.execute(qry, values)
        self.my_connection.commit()
        return True

    def delete_books(self,bookid):
        qry = "DELETE FROM issue WHERE bookid = %s"
        value = (bookid,)
        self.my_cursor.execute(qry,value)
        self.my_connection.commit()

