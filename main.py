import Book

def main():
    title = input("What is the books Title: ")
    author = input("What is the books Author: ")
    check_out = int(input("Enter 0 if the book is available, 1 if the book is checked out: "))
    print() #Console Readability

    the_book = Book.Book(title, author, check_out)

    with open("Library.txt", "a") as lib:
        lib.write(the_book.getTitle())
        lib.write("\n")
        lib.write(the_book.getAuthor())
        lib.write("\n")
        lib.write(str(the_book.getCheck_out_Status()))
        lib.write("\n")

    with open("Library.txt", "r") as r_lib:
        title = r_lib.readline().rstrip("\n")
        while title != "":
            author = r_lib.readline().rstrip("\n")
            check_out = r_lib.readline().rstrip()

            the_book = Book.Book(title, author, int(check_out))
            print(the_book.__str__())
            print() #Console readability

            title = r_lib.readline().rstrip("\n")

main()