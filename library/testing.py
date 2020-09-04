from connection import qry
import unittest

class testing(unittest.TestCase):
    test=qry()
    def test_add_book(self):
        actual_result = self.test.add_book("Python","Ram","2")
        self.assertTrue(actual_result)

    def test_delete(self):
        actual_result = self.test.delete_books(2)
        self.assertTrue(actual_result)


    def test_search(self):
        actual_result = self.test.search("The Digital Flood")
        self.assertTrue(actual_result)

    def test_signin(self):
        actual_result = self.test.signin("190132","Prasamsha","Password","Prasamsha@gmail.com","23989898")
        self.assertTrue(actual_result)

    def test_login(self):
        actual_result = self.test.login("5555","Password")
        self.assertTrue(actual_result)

unittest.main()