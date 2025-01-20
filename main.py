import Book

def main():
    more = "y"
    while more == "Y" or more == "y":
        menu_num = menu()
        match menu_num:
            case 1:
                the_book = addBook()
                writeLibrary(the_book)
            case 2:
                book_name = input("What is the title of the book you are looking for? ")
                check_out(book_name)
            case 3:
                book_name_in = input("What is the title of the book you are returning? ")
                check_in(book_name_in)
            case 4:
                the_library = readLibrary()
                showLibrary(the_library)
            case _:
                print("Exited Program")
        print()  # Console Readability
        more = input("Return to main menu? (y/n): ")
    print() # Console Readability
    print("Thank you for visiting our Library. Come again soon!")

def check_in(returning_book):
    found_books = readLibrary()

    for x in found_books:
        if x.getTitle() == returning_book:
            print("Thank you for returning this book!")
            x.setCheck_out_Status(1)

    with open("Library.txt", "w") as lib:
        for y in found_books:
            lib.write(y.getTitle())
            lib.write("\n")
            lib.write(y.getAuthor())
            lib.write("\n")
            lib.write(str(y.getCheck_out_Status()))
            lib.write("\n")

def check_out(searching_book):
    found_books = readLibrary()

    for x in found_books:
        if x.getTitle() == searching_book:
            print("We found the book!")
            x.setCheck_out_Status(0)

    with open("Library.txt", "w") as lib:
        for y in found_books:
            lib.write(y.getTitle())
            lib.write("\n")
            lib.write(y.getAuthor())
            lib.write("\n")
            lib.write(str(y.getCheck_out_Status()))
            lib.write("\n")

def menu():
    print() # Console Readability
    print("1. Add Book\n"
          "2. Check Out Book\n"
          "3. Return Book\n"
          "4. View Books\n"
          "Enter any key to Exit\n"
          )
    num = int(input("Enter menu number: "))
    return num

def addBook():
    title = input("What is the books Title: ")
    author = input("What is the books Author: ")
    check_out = int(input("Enter 0 if the book is available, 1 if the book is checked out: "))
    print()  # Console Readability

    the_book = Book.Book(title, author, check_out)

    return the_book

def showLibrary (books):
    if len(books) == 0:
        print() # Console Readability
        print("The Library seems empty! Maybe you should add a Book!")
        print() # Console Readability
    else:
        for book in books:
            print() # Console Readability
            print(book)


def writeLibrary(object):
    with open("Library.txt", "a") as lib:
        lib.write(object.getTitle())
        lib.write("\n")
        lib.write(object.getAuthor())
        lib.write("\n")
        lib.write(str(object.getCheck_out_Status()))
        lib.write("\n")

def readLibrary():
    with open("Library.txt", "r") as r_lib:
        all_books = []
        title = r_lib.readline().rstrip("\n")
        while title != "":
            author = r_lib.readline().rstrip("\n")
            check_out = r_lib.readline().rstrip()

            the_book = Book.Book(title, author, int(check_out))
            all_books.append(the_book)

            title = r_lib.readline().rstrip("\n")

        return all_books
main()