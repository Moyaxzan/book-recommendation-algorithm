reader_file = "./Ressources/readers.txt"
books_read_file = "./Ressources/booksread.txt"
books_file = "./Ressources/books.txt"

###  PART TWO PRIMARY FUNCTIONS

def menu_part2():
    print("Write 1 to add a book")
    print("Write 2 to edit a book")
    print("Write 3 to delete a book")
    print("Write 'back' to return to the last menu")
    choice = input("What do you want to do ?\n")
    if choice == "1":
        addBook()
    elif choice == "2":
        editBook()
    elif choice == "3":
        deleteBook()
    elif choice == "back":
        return


def addBook():
    list_of_books = open(books_file, "r")
    list_of_books_readlines = list_of_books.readlines()
    book_to_append = input("What book do you want to add ?\n")
    while book_to_append in [x.replace('\n', '') for x in list_of_books_readlines]:
        print("The book is already in the list\n")
        book_to_append = input("What book do you want to add ? Write 'back' to go back.\n")
        if book_to_append == "back":
            return menu_part2()
    if book_to_append == "back":
        return menu_part2()
    list_of_books = open(books_file, "a")
    list_of_books.write(book_to_append + "\n")


def editBook():
    list_of_books = open(books_file, "r")
    list_of_books_readlines = list_of_books.readlines()
    book_to_edit, new_name_book = None, None
    backbool = True
    book_to_edit = input("Which book do you want to edit ? Write 'back' to go back.\n")
    while book_to_edit not in [x.replace('\n', '') for x in list_of_books_readlines] and book_to_edit != "back":
        print("The book is not in the list")
        book_to_edit = input("Which book do you want to edit ? Write 'back' to go back.\n")
    if book_to_edit != "back":
        new_name_book = input("What is the new name of the book ? Write 'back' to go back.\n")
    if new_name_book == "back" or book_to_edit == "back":
        backbool = False
    if backbool:
        index = getIndexBook(book_to_edit)
        list_of_books_readlines[index] = new_name_book + "\n"
        list_of_books = open(books_file, "w")
        list_of_books.writelines(list_of_books_readlines)
    else:
        menu_part2()

def deleteBook():
    list_of_books = open(books_file, "r")
    book_reads = open(books_read_file, "r")
    list_of_books_readlines = list_of_books.readlines()
    book_reads_readlines = book_reads.readlines()
    book_to_delete = input("Which book do you want to delete ? \n")
    if book_to_delete == "back":
        return menu_part2()
    while book_to_delete not in [x.replace('\n', '') for x in list_of_books_readlines]:
        print("The book is not in the list")
        book_to_delete = input("Which book do you want to delete ? \n")
        if book_to_delete == "back":
            return menu_part2()
    index = getIndexBook(book_to_delete)
    for i in range(len(book_reads_readlines)):
        if str(index) in book_reads_readlines[i]:
            book_reads_readlines[i]=book_reads_readlines[i].replace(","+str(index),"")
    list_of_books_readlines[index] = "\n"
    list_of_books = open(books_file, "w")
    book_reads = open(books_read_file,"w")
    list_of_books.writelines(list_of_books_readlines)
    book_reads.writelines(book_reads_readlines)

### PART TWO SECONDARY FUNCTIONS


def getIndexBook(book):
    list_of_books = open(books_file, "r")
    list_of_books_readlines = list_of_books.readlines()
    index = 0
    for i in range(len(list_of_books_readlines)):
        if list_of_books_readlines[i].replace("\n", "") == book:
            index = i
    return index

