import Book

def main():
    title = input("What is the books Title: ")
    author = input("What is the books Author: ")
    check_out = int(input("Enter 0 if the book is available, 1 if the book is checked out: "))

    the_book = Book.Book(title, author, check_out)

    print(the_book.__str__())

main()