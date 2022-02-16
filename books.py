
class books:
    def __init__(self,name,author,price,no_pages):
            self.name=name
            self.author=author
            self.price=price
            self.no_pages=no_pages


a=input("Enter name of book: ")
b=input("Enter auther of book: ")
c=input("Enter price of book: ")
d=input("Enter no of page of the book: ")
print("------------------------------------------")
b1=books(a,b,c,d)
print("name of the book is",b1.name)
print("author of the book is",b1.author)
print("price of the book is",b1.price)
print("number of pages of the book is",b1.no_pages)
print("-------------------------------------------")