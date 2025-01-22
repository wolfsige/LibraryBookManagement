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
    """
        Searches for a book in the library and updates its check-out status.

        This function reads the library from Library.txt and searches for a book
        matching the provided title. If found, the book's check_out_status is set
        to 1 (checked in), and the library file is updated to reflect the change.

        Parameters:
        returning_book (str): The title of the book to search for in the library.

        Returns:
        none
    """
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
    """
        Searches for a book in the library and updates its check-out status.

        This function reads the library from Library.txt and searches for a book
        matching the provided title. If found, the book's check-out status is set
        to 0 (checked out), and the library file is updated to reflect the change.

        Parameters:
        searching_book (str): The title of the book to search for in the library.

        Returns:
        none
    """
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
    """
        Prompts the user to enter a number corresponding to the number next to the printed menu option.

        this function has the user input a number to navigate the program.
        If a number that is not present on the menu, or a value such as a string,
        is tried the function defaults to exiting the program.

        Parameters:
        none

        Returns:
        num: return the user input to be used with a match/case in main()
    """

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
    """
        Prompts the user to input book details (title and author) and defaults check out status to 1, aka checked in.
        The inputs (author and title) are both made uppercase and then the_book object is created.

        Parameters:
        None

        Returns:
        the_book: returned to be used by write_library()
    """

    title = input("What is the books Title: ").upper()
    author = input("What is the books Author: ").upper()
    check_out = 1
    print()  # Console Readability

    the_book = Book.Book(title, author, check_out)

    return the_book

def show_library (books):
    """
        Uses an if statement to check the books parameter. iIf it is an empty list it tells the user they should add
        a book. If the list is not empty, the user is shown all the books in the library.

        Parameters:
        books (list): a list of all the read information from Library.txt passed from read_library()
                    each represented as a string.

        Returns:
        none
    """

    if len(books) == 0:
        print() # Console Readability
        print("The Library seems empty! Maybe you should add a Book!")
        print() # Console Readability
    else:
        for book in books:
            print() # Console Readability
            print(book)


def write_library(book_object):
    """
        Using the_book object passed from add_book() this function opens the text file and appends
        with the details of the user inputs from add_book() (title, author, and default check_in_status)


        Parameters:
        book_object (Book): An instance of the Book class, containing the title, author,
                        and check_out status of a book.

        Returns:
        none
    """

    with open("Library.txt", "a") as lib:
        lib.write(book_object.getTitle())
        lib.write("\n")
        lib.write(book_object.getAuthor())
        lib.write("\n")
        lib.write(str(book_object.getCheck_out_Status()))
        lib.write("\n")

def read_library():
    """
        Opens Library.txt to read the file and collect the information (title, author, check_out) putting it
        into a list.

        Parameters:
        none

        Returns:
        all_books: returns the full file of Library.txt as a list which will be used by show_library()
        """

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