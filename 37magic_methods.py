# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations.
#                 They allow developers to define or customize the behavior of objects

class Book:

    def __init__(self,title, author,num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self): # String representation of the object
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other): #less than
        return self.num_pages < other.num_pages

    def __gt__(self, other): #greater than
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    
    def __contains__(self,keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self,key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not found"
        

book1 = Book("The Hobbit","J.R.R. Tolkien", 310)
book2 = Book("Harry Potter and The Philosopher's Stone","J.K. Rowling",223)
book3 = Book("The Lion, the Witch and the Wardrobe","C.S. Lewis", 172)
book4 = Book("The Lion, the Witch and the Wardrobe","C.S. Lewis", 168)

# __str__
print(book1)
print(book2)
print(book3)
print(book4)

# __eq__
print(book1 == book2)
print(book3 == book4)

# __lt__
print(book2 < book3)
# __gt__
print(book2 < book3)
# __add__
print(book2 + book3)

# __contains__
print("Lion" in book3)

print(book1['title'])
print(book3['author'])
print(book3['num_pages'])
print(book3['gg'])