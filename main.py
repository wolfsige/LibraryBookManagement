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
                print("coming soon")
            case 3:
                print("coming soon")
            case 4:
                the_library = readLibrary()
                showLibrary (the_library)
            case _:
                print("Exited Program")
        more = input("Return to main menu? (y/n): ")

def menu():
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
    for book in books:
        print(book)
        print() # Console Readability


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