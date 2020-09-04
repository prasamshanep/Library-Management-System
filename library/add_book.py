from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class BookAdd():
    def __init__(self,window):
        
        self.win=window
        self.win.geometry('1300x500+20+270')
        self.win.title("Library")
        self.win.config(bg="slategray") 
        self.win.wm_attributes("-transparentcolor", "slategray")
        self.update_index = ""
        self.selected_row = ""
        self.book = Book()
        self.heading=Label(self.win,text="Add Book",fg="black",width=40,height=1,font=('algerian',20,'bold'),bg="saddlebrown",activebackground="grey")
        self.heading.place(x=0,y=5,relwidth=1)
        self.book_name=Label(self.win,text="Book Name",fg="black",width=20,height=2,font=('Monotype Corsiva',12,'bold'),bg="saddlebrown",activebackground="grey")
        self.book_name.place(x=50,y=100)
        self.entry_name=Entry(self.win,font=('Arial',15,'bold'))
        self.entry_name.place(x=300,y=100)
        self.book_id=Label(self.win,text="Book ID",fg="black",width=20,height=2,font=('Monotype Corsiva',12,'bold'),bg="saddlebrown",activebackground="grey")
        self.book_id.place(x=50,y=150)
        self.entry_id=Entry(self.win,font=('Arial',15,'bold'))
        self.entry_id.place(x=300,y=150)
        self.book_author=Label(self.win,text="Author",fg="black",width=20,height=2,font=('Monotype Corsiva',12,'bold'),bg="saddlebrown",activebackground="grey")
        self.book_author.place(x=50,y=150)
        self.entry_author=Entry(self.win,font=('Arial',15,'bold'))
        self.entry_author.place(x=300,y=150)
        self.book_quantity=Label(self.win,text="Quantity",fg="black",width=20,height=2,font=('Monotype Corsiva',12,'bold'),bg="saddlebrown",activebackground="grey")
        self.book_quantity.place(x=50,y=200)
        self.entry_quantity=Entry(self.win,font=('Arial',15,'bold'))
        self.entry_quantity.place(x=300,y=200)
        self.frame = Frame(self.win, bd = 4, relief = RIDGE)
        self.frame.place(x=550, y=100)
        self.sbar = Scrollbar(self.frame, orient = HORIZONTAL)
        self.sbary = Scrollbar(self.frame, orient = VERTICAL)
        self.book_tree = ttk.Treeview(self.frame, columns=('bookid','name', 'author', 'quantity'),xscrollcommand=self.sbar.set, yscrollcommand=self.sbary.set)
        self.sbar.pack(side=BOTTOM, fill=X)
        self.sbary.pack(side=RIGHT, fill=Y)
        self.sbar.config(command=self.book_tree.xview)
        self.sbary.config(command=self.book_tree.yview)
        self.book_tree['show'] = 'headings'
        self.book_tree.column('name', width=150)
        self.book_tree.column('bookid', width=150)
        self.book_tree.column('author', width=150)
        self.book_tree.column('quantity', width=150)
        self.book_tree.heading('name', text="Book Name")
        self.book_tree.heading('bookid', text="Book ID")
        self.book_tree.heading('author', text="Author Name")
        self.book_tree.heading('quantity', text="Quantity")
        self.book_tree.pack(fill = BOTH, expand = 1)
        self.show_book_tree()

        
        self.book_add=Button(self.win,text="ADD",fg="white",width=20,height=2,font=('algerian',10,'bold'),bg="black",activebackground="grey",command = self.add_book )
        self.book_add.place(x=200,y=300)

    def add_book(self):
        if self.update_index != "":
            messagebox.showerror("Error", "Please inter all values first")
        else:
            name = self.entry_name.get()
            bookid = self.entry_id.get()
            author = self.entry_author.get()
            quantity = self.entry_quantity.get()
            try:
                self.book.add_book(name, bookid, author,quantity)
                messagebox.showinfo('Book', "Book Added")
                self.show_book_tree()
                self.entry_name.delete(0,END)
                self.entry_author.delete(0,END)
                self.entry_quantity.delete(0,END)
            except:
                messagebox.showerror("Error", 'Can not be added !!!')

    def show_book_tree(self):
        self.book_tree.delete(*self.book_tree.get_children())
        data = self.book.show_book()
        for i in data:
            self.book_tree.insert("", "end", value=(i[0], i[1], i[2], i[3]))
          
class BookUpdate(BookAdd):
    def __init__(self,window):
        super().__init__(window)
        self.win.geometry('1250x500+280+270')
        self.heading=Label(self.win,text="Update Book",fg="black",width=40,height=1,font=('algerian',20,'bold'),bg="saddlebrown",activebackground="grey")
        self.heading.place(x=0,y=5,relwidth=1)
        self.book_update=Button(self.win,text="Update",fg="white",width=20,height=2,font=('algerian',10,'bold'),bg="black",activebackground="grey",command = self.update_book )
        self.book_update.place(x=200,y=300)     

    def show_book_tree(self):
        self.book_tree.delete(*self.book_tree.get_children())
        data = self.book.show_book()
        for i in data:
            self.book_tree.insert("", "end", value=(i[0], i[1], i[2], i[3]))
        self.book_tree.bind("<Double-1>", self.on_book_select)
      
        
    def on_book_select(self, event):
        selected_row = self.book_tree.selection()[0]
        selected_book = self.book_tree.index(selected_row)
        all_books = self.book.show_book()
        selected_item = all_books[selected_book]
        self.selected_row = selected_item[0]
        self.entry_name.delete(0, END)
        self.entry_name.insert(0, selected_item[1])
        self.entry_author.delete(0, END)
        self.entry_author.insert(0, selected_item[2])
        self.entry_quantity.delete(0, END)
        self.entry_quantity.insert(0, selected_item[3])


    def update_book(self):
        name = self.entry_name.get()
        author = self.entry_author.get()
        quantity = self.entry_quantity.get()

        if name == "" or author == "" or quantity == "":
            messagebox.showerror('Error' , 'Select A Row and insert all value')

        else:
            try:
                self.book.update(self.selected_row, name, author, quantity)
                messagebox.showinfo('Updates', "Data Updated sucessfully.")
                self.show_book_tree()
            except:
                messagebox.showerror("Error", "Try Again")


class BookDelete():
    def __init__(self,window):
        self.win=window
        self.win.geometry('500x500+620+270')
        self.win.title("Library")
        self.win.config(bg="slategray") 
        self.win.wm_attributes("-transparentcolor", "slategray")
        self.update_index = ""
        self.book = Book()
        self.heading=Label(self.win,text="Delete Book",fg="black",width=40,height=1,font=('algerian',20,'bold'),bg="saddlebrown",activebackground="grey")
        self.heading.place(x=0,y=5,relwidth=1)

        self.book_id = Label(self.win,text="Book ID",fg="black",width=20,height=2,font=('Monotype Corsiva',12,'bold'),bg="saddlebrown",activebackground="grey")
        self.book_id.place(x=50,y=100)
        self.entry_id=Entry(self.win,font=('Arial',15,'bold'))
        self.entry_id.place(x=250,y=110)
        self.frame = Frame(self.win, bd = 4, relief = RIDGE)
        self.frame.place(x=20, y=200)
        self.sbar = Scrollbar(self.frame, orient = HORIZONTAL)
        self.sbary = Scrollbar(self.frame, orient = VERTICAL)
        self.book_tree = ttk.Treeview(self.frame, columns=('name','author','bookid'),xscrollcommand=self.sbar.set, yscrollcommand=self.sbary.set)

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
        
        

        self.book_add=Button(self.win,text="Delete",fg="white",width=15,height=1,font=('algerian',10,'bold'),bg="black",activebackground="grey", command = self.delete_book)
        self.book_add.place(x=200,y=150)

    def show_book_tree(self):
        self.book_tree.delete(*self.book_tree.get_children())
        data = self.book.show_book()
        for i in data:
            self.book_tree.insert("", "end", value=(i[0], i[1], i[2], i[3]))

    def delete_book(self):
        bookid = self.entry_id.get()
        if bookid == "":
            messagebox.showinfo('Error' , 'Insert BOOKID')
        else:
            try:
                self.book.delete_books(bookid)
                messagebox.showinfo('Book', "Book deleted")
                self.show_book_tree()
            except:
                messagebox.showerror('Error', 'Try Again')
                    
class BookSearch():
    def __init__(self,window):
        self.win=window
        self.win.geometry('500x500+920+270')
        self.win.title("Library")
        self.win.config(bg="slategray") 
        self.win.wm_attributes("-transparentcolor", "slategray")
        self.heading=Label(self.win,text="Search Book",fg="black",width=40,height=1,font=('algerian',20,'bold'),bg="saddlebrown",activebackground="grey")
        self.heading.place(x=0,y=5,relwidth=1)

        self.entry_search=Entry(self.win,font=('Arial',15,'bold'))
        self.entry_search.place(x=150,y=150)

        self.book_search=Button(self.win,text="Search",fg="white",width=15,height=1,font=('algerian',10,'bold'),bg="black",activebackground="grey", command = self.search_book)
        self.book_search.place(x=180,y=210)

        self.drop = ttk.Combobox(self.win, value = ["Search By... ", "Book Name", "Author Name", "BookID"])
        self.drop.current(0)
        self.drop.place(x=180,y=100)

        self.book_tree = ttk.Treeview(self.win, columns=('name', 'bookid', 'author'))
        self.book_tree.place(x=100, y=250)
        self.book_tree['show'] = 'headings'
        self.book_tree.column('name', width=100)
        self.book_tree.column('bookid', width=100)
        self.book_tree.column('author', width=100)
        self.book_tree.heading('name', text="Book ID")
        self.book_tree.heading('bookid', text="Book Name")
        self.book_tree.heading('author', text="Author Name")

    def search_book(self):
        self.my_connection = mysql.connector.connect(user="root", password="", host="localhost", port=3306, database='collagelibrary')
        self.my_cursor = self.my_connection.cursor() 
       
        selected = self.drop.get()
        if selected == "Search By ...":
            test = Label(self.win, text = "Please select a drop down option")
            test.place(x=180, y=125)
          
        if selected == "Book Name":
            sql = "SELECT * FROM Bookss WHERE name = %s"
        if selected == "Author Name":
            sql = "SELECT * FROM Bookss WHERE author = %s"
        if selected == "BookID":
            sql = "SELECT * FROM Bookss WHERE bookid = %s"
            
        searched = self.entry_search.get()
        name = (searched,)
        result = self.my_cursor.execute(sql, name)
        result = self.my_cursor.fetchall()

        if len(result)!=0:
            self.book_tree.delete(*self.book_tree.get_children())
            for row in result:
                self.book_tree.insert('',END,values=row)

        if not result:
           messagebox.showerror("Error", "No data found")

class IssuedView():
    def __init__(self,window):
        self.win=window
        self.win.geometry('1000x500+500+270')
        self.win.title("Library")
        self.win.config(bg="slategray") 
        self.win.wm_attributes("-transparentcolor", "slategray")
        self.selected_row = ""
        self.book = Book()
        self.heading=Label(self.win,text="Issued Book View",fg="black",width=40,height=1,font=('algerian',20,'bold'),bg="saddlebrown",activebackground="grey")
        self.heading.place(x=0,y=5,relwidth=1)
        self.book_username=Label(self.win,text="username",fg="black",width=20,height=2,font=('Monotype Corsiva',12,'bold'),bg="saddlebrown",activebackground="grey")
        self.book_username.place(x=50,y=200)
        self.entry_username=Entry(self.win,font=('Arial',15,'bold'))
        self.entry_username.place(x=250,y=210)
        self.book_fine=Label(self.win,text="Fine",fg="black",width=20,height=2,font=('Monotype Corsiva',12,'bold'),bg="saddlebrown",activebackground="grey")
        self.book_fine.place(x=50,y=250)
        self.entry_fine=Entry(self.win,font=('Arial',15,'bold'))
        self.entry_fine.place(x=250,y=260)
        self.item_show = Button(self.win,text="Add",fg="white",width=20,height=2,font=('algerian',10,'bold'),bg="black",activebackground="grey", command = self.update_issue)
        self.item_show.place(x=200,y=300)

        self.book_tree = ttk.Treeview(self.win, columns=( 'bookname','bookid', 'username', 'issuedate','fine'))
        self.book_tree.place(x=500, y=100)
        self.book_tree['show'] = 'headings'
        self.book_tree.column('bookname', width=150)
        self.book_tree.column('bookid', width=80)
        self.book_tree.column('username', width=80)
        self.book_tree.column('issuedate', width=80)
        self.book_tree.column('fine', width=80)
        self.book_tree.heading('bookname', text="BookName")
        self.book_tree.heading('bookid', text="Book ID")
        self.book_tree.heading('username', text="Username")
        self.book_tree.heading('issuedate', text="IssueDate")
        self.book_tree.heading('fine', text="Fine")
        self.show_book_tree()

    def show_book_tree(self):
        self.book_tree.delete(*self.book_tree.get_children())
        data = self.book.show_issue()
        for i in data:
            self.book_tree.insert("", "end", text=i[0], value=(i[1], i[2], i[3], i[4], i[5]))
            self.book_tree.bind("<Double-1>", self.on_book_select)
      

    def on_book_select(self, event):
        selected_row = self.book_tree.selection()[0]
        selected_book = self.book_tree.index(selected_row)
        all_books = self.book.show_issue()
        selected_item = all_books[selected_book]
        self.selected_row = selected_item[0]
        self.entry_username.delete(0, END)
        self.entry_username.insert(0, selected_item[3])
        self.entry_fine.delete(0, END)
        self.entry_fine.insert(0, selected_item[5])

    def update_issue(self):
        fine = self.entry_fine.get()

        if self.book.fine(self.selected_row,fine):
            messagebox.showinfo('Updates', "Data Updated sucessfully.")
            self.show_book_tree()
        
class Book (object):
    def __init__(self):
        self.my_connection = mysql.connector.connect(user="root", password="", host="localhost", port=3306, database='collagelibrary')
        self.my_cursor = self.my_connection.cursor() 
       
    def add_book(self, name, bookid, author, quantity):
        qry = "INSERT INTO Bookss ( id,name, author, quantity) VALUES (%s,%s,%s,%s)"
        values = (bookid,name, author, quantity)
        self.my_cursor.execute(qry, values)
        self.my_connection.commit()
        return True

    def show_book(self):
        all_books = []
        qry = "SELECT * FROM Bookss"
        self.my_cursor.execute(qry)
        all_books = self.my_cursor.fetchall()
        return all_books

    def delete_books(self,bookid):
        qry = "DELETE FROM Bookss WHERE id = %s"
        value = (bookid,)
        self.my_cursor.execute(qry,value)
        self.my_connection.commit()
        return True

    def update(self, row, name, author, quantity):
        qry="UPDATE Bookss SET name=%s ,author =%s, quantity =%s  WHERE id =%s"
        values = (name, author, quantity,row)
        self.my_cursor.execute(qry,values)
        self.my_connection.commit()
        return True

    def show_issue(self):
        all_books = []
        qry = "SELECT * FROM issue"
        self.my_cursor.execute(qry)
        all_books = self.my_cursor.fetchall()
        return all_books

    def fine(self, row, fine): 
        qry="UPDATE issue SET fine=%s WHERE id = %s"
        values = (fine, row)
        self.my_cursor.execute(qry,values)
        self.my_connection.commit()
        return True
