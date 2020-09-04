import mysql.connector

class qry:
    def __init__(self):
        self.my_connection = mysql.connector.connect(user="root", password="", host="localhost", port=3306,
                                                     database='collagelibrary')
        self.my_cursor = self.my_connection.cursor()

    def add_book(self, name, author, quantity):
        qry = "INSERT INTO Bookss (name, author, quantity) VALUES (%s,%s,%s)"
        values = (name, author, quantity)
        self.my_cursor.execute(qry, values)
        self.my_connection.commit()
        return True

    def delete_books(self,bookid):
        qry = "DELETE FROM Bookss WHERE id = %s"
        value = (bookid,)
        self.my_cursor.execute(qry,value)
        self.my_connection.commit()
        return True
        
    def search(self,name):
        qry="SELECT * FROM Bookss WHERE name = %s"
        value=(name,)
        self.my_cursor.execute(qry, value)
        data=self.my_cursor.fetchall()
        if len(data)>0:
            return True
        else:
            return False

    def signin(self,username,fullname, password, gmail, number):
        qry = "INSERT INTO users (username, fullname, password, gmail, number) VALUES (%s,%s,%s,%s,%s)"    
        values = (username, fullname, password, gmail, number)
        self.my_cursor.execute(qry, values)
        self.my_connection.commit()
        return True


    def login(self,username,password):
        qry="select * from users where username=%s and password=%s"
        values = (username , password)
        self.my_cursor.execute(qry, values)
        data= self.my_cursor.fetchone()
        if len(data)>0:
            return True
        else:
            return False

