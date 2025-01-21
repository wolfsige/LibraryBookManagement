import Book

def main():
    more = "y"
    while more == "Y" or more == "y":
        menu_num = menu()
        match menu_num:
            case 1:
                the_book = add_book()
                write_library(the_book)
            case 2:
                book_name = input("What is the title of the book you are looking for? ").upper()
                check_out_book(book_name)
            case 3:
                book_name_in = input("What is the title of the book you are returning? ").upper()
                check_in_book(book_name_in)
            case 4:
                the_library = read_library()
                show_library(the_library)
            case _:
                exit_app = input("Would you like to Exit the program (y/n)? ")
                if exit_app == "y" or exit_app == "Y":
                    print()  # Console Readability
                    print("Thank you for visiting our Library. Come again soon!")
                    print("Exited Program")
                    exit()
        print()  # Console Readability
        more = input("Return to main menu? (y/n): ")
        print("Thank you for visiting our Library. Come again soon!")
        print("Exited Program")

def check_in_book(returning_book):
    found_books = read_library()

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

def check_out_book(searching_book):
    found_books = read_library()

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
    try:
        print("1. Add Book\n"
              "2. Check Out Book\n"
              "3. Return Book\n"
              "4. View Books\n"
              "Enter any key to Exit\n"
              )
        num = int(input("Enter menu number: "))
        return num
    except ValueError:
        print()

def add_book():
    title = input("What is the books Title: ").upper()
    author = input("What is the books Author: ").upper()
    check_out = 1
    print()  # Console Readability

    the_book = Book.Book(title, author, check_out)

    return the_book

def show_library (books):
    if len(books) == 0:
        print() # Console Readability
        print("The Library seems empty! Maybe you should add a Book!")
        print() # Console Readability
    else:
        for book in books:
            print() # Console Readability
            print(book)


def write_library(book_object):
    with open("Library.txt", "a") as lib:
        lib.write(book_object.getTitle())
        lib.write("\n")
        lib.write(book_object.getAuthor())
        lib.write("\n")
        lib.write(str(book_object.getCheck_out_Status()))
        lib.write("\n")

def read_library():
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