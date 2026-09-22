'''class Book:
    def __init__(self, author, page_count):
        self.author =  author
        self.page_count = page_count
class Magazine:
    def __init__(self, chief_editor):
        self.chief_editor = chief_editor
class Publication(Book, Magazine):
    def __init__(self, name, author, page_count, chief_editor):
        self.name = name
        Book.__init__(self, author, page_count)
        Magazine.__init__(self, chief_editor)
        
    def print_information(self):
        print(f"{self.name} ({self.author} {self.page_count} {self.chief_editor})")
publications = []
publications.append(Publication("Donald Duck", "Aki Hyyppä"))
publications.append(Publication("Compartment No. 6", "Rosa Liksom", "192"))
for e in publications:
    e.print_information()'''
class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Page count: {self.page_count}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Name: {self.name}")
        print(f"Chief editor: {self.chief_editor}")


# Main program
magazine = Magazine("Donald Duck", "Aki Hyyppä")
book = Book("Compartment No. 6", "Rosa Liksom", 192)

magazine.print_information()
book.print_information()


