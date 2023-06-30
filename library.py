class library:
    def __init__(self):
        self.noBooks = 0
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def removebook(self, book):
        self.books.remove(book)
        print("Aftee removing that book: ", len(self.books))
        for b in self.books:
            print(b)
        

    def display(self):
        print(f"The library has {self.noBooks} books. The  books are")
        for book in self.books:
            print(book)



l = library()
l.addBook("Harry potter")
l.addBook("LifeLine")
l.display()
l.removebook("Harry potter")
l.display()
