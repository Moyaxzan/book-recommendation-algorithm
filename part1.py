# PART 1 : Reader profiles, made by Gwendal HOLLOCOU and Tao SAINT PAUL AMOURDAM.
# This file contains every functions related to the readers profiles.
from part3 import *
reader_file = "./Ressources/readers.txt"
books_read_file = "./Ressources/booksread.txt"
books_file = "./Ressources/books.txt"
scoring_matrix_file = "Ressources/rating_matrix.txt"
dicogenre = {1: "sci-fi", 2: "Biography", 3: "Horror", 4: "Romance", 5: "Fable", 6: "History", 7: "Comedy"}

#  PART ONE PRIMARY FUNCTIONS


# This function allows to navigate through part1 functions
def menu_part1():
    print("Write 1 to display books")
    print("Write 2 to add a reader")
    print("Write 3 to view a reader")
    print("Write 4 to edit a reader")
    print("Write 5 to delete a reader")
    print("Write 'back' to return to the last menu")
    choice = input("What do you want to do ?\n")
    power = 1
    if choice == "1":
        displayBooks()
    elif choice == "2":
        power = addReader()
    elif choice == "3" or choice == "4" or choice == "5":
        list_prompt = ["view", "edit", "delete"]
        input_string = "what pseudo do you want to " + str(list_prompt[int(choice)-3]) + "? \n"
        pseudo = input(input_string)
        if pseudo == "back":
            return menu_part1()
        elif pseudo == "exit":
            power = 0
        if choice == "3":
            viewReader(pseudo)
        elif choice == "4":
            power = editReader(pseudo)
        elif choice == "5":
            deleteReader(pseudo)
    elif choice == "back":
        return 1
    elif choice == "exit":
        power = 0
    else:
        print("invalid input. try again.")
        return menu_part1()
    if power == 0:
        return 0
    else:
        return 1


# This functions displays every books in "books.txt" file.
def displayBooks(list_of_books=books_file):
    # Open the "books.txt" file
    f = open(list_of_books, "r")
    # Puts every books into a list "books"
    books = f.readlines()
    cpt = 1
    for i in books:
        if i != "\n":
            print(str(cpt) + ".", i)
            cpt += 1


# This function adds a reader in "booksread.txt" and "readers.txt" files
def addReader():
    # Open the "readers.txt" and "booksread.txt" files
    readers = open(reader_file, "a")
    books_read = open(books_read_file, "a")
    matrix_file = open(scoring_matrix_file, "r")
    books = open(books_file , "r")
    books_lines = books.readlines()
    matrix = matrix_file.readlines()
    # Calls createLineReader() which create the right line to insert into "readers.txt" and "booksread.txt" files
    line_reader_file, line_books_read, line_matrix = createLineReader()
    if line_reader_file is None and line_books_read is None and line_matrix is None:
        return menu_part1()
    elif line_reader_file == 0 and line_books_read == 0 and line_matrix == 0:
        return 0
    # Write into "readers.txt" and "booksread.txt" the lines we just created
    readers.write(line_reader_file)
    books_read.write(line_books_read)
    matrix_file.close()
    matrix_file = open(scoring_matrix_file, "a")
    matrix_file.write(line_matrix)
    matrix_file.close()
    readers.close()
    books_read.close()


# This function allows to view informations about a reader using its pseudonym.
def viewReader(pseudonym):
    # Opens the "readers.txt" and create a string of the lines
    readers = open(reader_file, "r")
    readers_lines = readers.read()
    if pseudonym in readers_lines:
        readers_line_splitted = readers_lines.split("\n")
        for cpt in range(len(readers_line_splitted)):
            if pseudonym in readers_line_splitted[cpt]:
                pronoun = "He/She"
                lineSplited = readers_line_splitted[cpt].split(", ")
                if int(lineSplited[1]) == 1:
                    genderstr = "is a man."
                    pronoun = "He"
                elif int(lineSplited[1]) == 2:
                    genderstr = "is a women."
                    pronoun = "She"
                else:
                    genderstr = "has not registered as men or woman."
                if int(lineSplited[2]) == 1:
                    agestr = "is 18 years old"
                elif int(lineSplited[2]) == 2:
                    agestr = "is between 18 and 25 years old"
                else:
                    agestr = "is more than 25 years old"
                genre = dicogenre[int(lineSplited[3])]
                print(lineSplited[0], genderstr, pronoun, agestr, "and likes", genre, "books.")
    else:
        print("This pseudonym is not registered")


# This function allows to edit a reader's profile using its pseudonym.
def editReader(pseudonym):
    list_of_readers=list_pseudonym()
    if pseudonym in list_of_readers:
        readers = open(reader_file, "r")
        book_reads = open(books_read_file, "r")
        matrix = open(scoring_matrix_file, "r")
        readers_lines = readers.readlines()
        book_reads_lines = book_reads.readlines()
        matrix_lines = matrix.readlines()
        line_readers, line_books_read, line_matrix = createLineReader(pseudonym)
        if line_readers == None and line_books_read == None and line_matrix == None:
            return menu_part1()
        elif line_readers == 0 and line_books_read == 0 and line_matrix == 0:
            return 0
        index = getIndexPseudonym(pseudonym)
        readers_lines[index] = line_readers
        book_reads_lines[index] = line_books_read
        matrix_lines[index] = line_matrix
        readers = open(reader_file, "w")
        book_reads = open(books_read_file, "w")
        matrix = open(scoring_matrix_file, "w")
        readers.writelines(readers_lines)
        book_reads.writelines(book_reads_lines)
        matrix.writelines(matrix_lines)
        readers.close()
        book_reads.close()
        matrix.close()
    else:
        print("The user you want to edit is not registere")


# This functions allows to delete a readers's profile using its pseudonym.
def deleteReader(pseudonym):
    readers = open(reader_file, "r")
    book_reads = open(books_read_file, "r")
    scoring_matrix = open(scoring_matrix_file, "r")
    matrix_lines = scoring_matrix.readlines()
    readers_lines = readers.readlines()
    book_reads_lines = book_reads.readlines()
    index = getIndexPseudonym(pseudonym)
    readers_lines.pop(index)
    book_reads_lines.pop(index)
    matrix_lines.pop(index)
    readers = open(reader_file, "w")
    book_reads = open(books_read_file, "w")
    scoring_matrix = open(scoring_matrix_file, "w")
    readers.writelines(readers_lines)
    book_reads.writelines(book_reads_lines)
    scoring_matrix.writelines(matrix_lines)
    scoring_matrix.close()
    readers.close()
    book_reads.close()


# PART ONE SECONDARY FUNCTIONS


# This function returns the index of a reader in "booksread.txt" and "readers.txt" using its pseudonym.
def getIndexPseudonym(pseudonym):
    list_of_pseudonym = list_pseudonym()
    for i in range(len(list_of_pseudonym)):
        if list_of_pseudonym[i] == pseudonym:
            index = i
    return index


# This function returns the lines to append to "books.txt", "readers.txt" and "booksread.txt" and
# may use a pseudonym in case it is used by editReader()
def createLineReader(*pseudonym):
    pseudobool = True
    genderbool = True
    agebool = True
    readingStylebool = True
    list_of_books = open(books_file, "r")
    list_pseudonyms = list_pseudonym()
    books_lines = list_of_books.readlines()
    while pseudobool:
        pseudo = input("What is your pseudonym ?\n")
        if pseudo == "back":
            return None, None, None
        elif pseudo == "exit":
            return 0, 0, 0
        if len(pseudo) >= 3 and "," not in pseudo:
            pseudobool = False
        else:
            print("invalide input : your pseudonym must exceed 2 characters and must not contain special characters.")
            pseudobool = True
        if pseudo not in list_pseudonyms :
            if not pseudobool :
                pseudobool = False
        elif pseudonym != ():
            if pseudonym[0] == pseudo:
                pseudobool = False
        else:
            print("invalide input : pseudonym already taken")
            pseudobool = True

    while genderbool:
        print("PRESS : ")
        print("1 if you are a man")
        print("2 if you are a woman")
        print("3 if you don't want to specify")
        gender = input()
        if gender == "1" or gender == "2" or gender == "3":
            genderbool = False
        elif gender == "back":
            return None, None, None
        elif gender == "exit":
            return 0, 0, 0
        else:
            print("invalide input : you need to type 1, 2 or 3")
    while agebool:
        print("PRESS : ")
        print("1 if you are 18 years old")
        print("2 if you are between 18 and 25 years old")
        print("3 if you are over 25 years old")
        age = input()
        if age == "1" or age == "2" or age == "3":
            agebool = False
        elif age == "back":
            return None, None, None
        elif age == "exit":
            return 0, 0, 0
        else:
            print("invalide input : you need to type 1, 2 or 3")
    while readingStylebool:
        print("""PRESS A NUMBER
                    1. sci-fi
                    2. Biography
                    3. Horror
                    4. Romance
                    5. Fable
                    6. History
                    7. Comedy""")
        readingStyle = input()
        try:
            int(readingStyle)
            if int(readingStyle) >= 1 and int(readingStyle) <= 7:
                readingStylebool = False
            else:
                print("invalide input : you need to type a number between 1 and 7")
        except:
            if readingStyle == "back":
                return None, None, None
            elif readingStyle == "exit":
                return 0, 0, 0
            else:
                print("invalide input : you need to type a number between 1 and 7")
    line_reader = str(pseudo) + ", " + str(gender) + ", " + str(age) + ", " + str(readingStyle) + "\n"
    print("Which books have you read ?")

    # Prints every books in the file books.txt
    displayBooks()
    appendBool = True

    # Initialize two strings that we will append to the books read and
    # rating matrix files when the user is over adding books
    line_books_read, line_matrix = "", ""
    # Adds the pseudonym of the user
    line_books_read += str(pseudo) + ","
    for i in range(len(books_lines)-countDeletedBooks()):
        if i == (len(books_lines)-countDeletedBooks())-1:
            line_matrix += "0\n"
        else:
            line_matrix += "0 "
    line_matrix_to_append = line_matrix

    # This while adds every book the user has read
    registered_book = []
    while appendBool:
        input_books = input("Enter the number of the book you've read or 'over' if you are finished\n")
        try:
            int(input_books)
            if input_books in registered_book:
                print("You have already registered this book\n")
            else:
                registered_book.append(input_books)
                mark = input("Rate this book from 1 to 5. (You can write 'skip' to skip rating this book)\n")
                while int(mark) < 0 or int(mark) > 5:
                    mark = int(input("Rate this book, from 1 to 5\n"))
                if mark != "skip":
                    line_books_read += input_books + ","
                    input_books = int(input_books) -1
                    liste_line_matrix = list(line_matrix_to_append)
                    for i in range(len(liste_line_matrix)):
                        if i == int(input_books)*2:
                            liste_line_matrix[i] = mark
                    line_matrix_to_append = "".join(liste_line_matrix)
        except:
            if input_books == "back":
                return None,None, None
            elif input_books == "exit":
                return 0, 0, 0
            elif input_books == "over":
                appendBool = False
    line_books_read = line_books_read[0:len(line_books_read) - 1]
    line_books_read += "\n"
    return line_reader, line_books_read, line_matrix_to_append

