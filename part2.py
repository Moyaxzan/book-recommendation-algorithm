reader_file = "./Ressources/readers.txt"
books_read_file = "./Ressources/booksread.txt"
books_file = "./Ressources/books.txt"
###  PART TWO PRIMARY FUNCTIONS

def addBook():
    list_of_books = open(books_file, "r")
    list_of_books_readlines = list_of_books.readlines()
    book_to_append = input("What book do you want to add ?\n")
    while book_to_append in [x.replace('\n', '') for x in list_of_books_readlines]:
        print("The book is already in the list\n")
        book_to_append = input("What book do you want to add ? Write 'back' to go back.\n")
        if book_to_append == "back":
            break
    if book_to_append == "back":
        return
    print(list_of_books_readlines)
    list_of_books = open(books_file, "a")
    list_of_books.write(book_to_append + "\n")


def editBook():
    list_of_books = open(books_file, "r")
    list_of_books_readlines = list_of_books.readlines()
    remake = True
    while remake:
        book_to_edit = input("Which book do you want to edit ? Write 'back' to go back.\n")
        while book_to_edit not in [x.replace('\n', '') for x in list_of_books_readlines] and book_to_edit != "back":
            print("The book is not in the list")
            book_to_edit = input("Which book do you want to edit ? Write 'back' to go back.\n")
        if book_to_edit == "back":
            return
        new_name_book = input("What is the new name of the book ? Write 'back' to go back.\n")
        if new_name_book == "back":
            remake = True
        else:
            remake = False
    index = getIndexBook(book_to_edit)
    list_of_books_readlines[index] = new_name_book + "\n"
    list_of_books = open(books_file, "w")
    list_of_books.writelines(list_of_books_readlines)


def deleteBook():
    list_of_books = open(books_file, "r")
    list_of_books_readlines = list_of_books.readlines()
    book_to_delete = input("Which book do you want to delete ? \n")
    while book_to_delete not in [x.replace('\n', '') for x in list_of_books_readlines]:
        print("The book is not in the list")
        book_to_delete = input("Which book do you want to delete ? \n")
    index = getIndexBook(book_to_delete)
    list_of_books_readlines[index] = "\n"
    list_of_books = open(books_file, "w")
    list_of_books.writelines(list_of_books_readlines)


### PART TWO SECONDARY FUNCTIONS


def getIndexBook(book):
    list_of_books = open(books_file, "r")
    list_of_books_readlines = list_of_books.readlines()
    for i in range(len(list_of_books_readlines)):
        if list_of_books_readlines[i].replace("\n", "") == book:
            index = i
    return index

