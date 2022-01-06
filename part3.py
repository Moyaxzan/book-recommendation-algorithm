# PART 3 : Recommendation, made by Gwendal HOLLOCOU and Tao SAINT PAUL AMOURDAM.
# This file contains every functions related to the ratings and recommendations.
# It has a back & exit system, using returns all along the file : basically,
# If a menu returns 1, it'll go back to run the main.py and so the program
# keep going. However, if a menu returns 0, it'll close the whole program and end the execution.

# We use sqrt for the Cosine Similarity
from math import sqrt

reader_file = "Resources/readers.txt"
books_read_file = "Resources/booksread.txt"
books_file = "Resources/books.txt"
scoring_matrix_file = "Resources/rating_matrix.txt"
similarity_matrix_file = "Resources/similarity_matrix.txt"

# PART THREE PRIMARY FUNCTIONS


# This function allows to navigate through part3 functions
def menu_part3():
    power = 1
    print("Write 1 to rate a book")
    print("Write 2 to get recommended a book")
    choice = input("What do you want to do ?\n")
    if choice == "1":
        pseudo = input("what is your pseudonym ?\n")
        while pseudo not in list_pseudonym():
            if pseudo == 'back':
                return menu_part3()
            elif pseudo == 'exit':
                return 0
            pseudo = input("what is your pseudonym ?\n")
        power = rateBook(pseudo)
        if power == 1:
            return menu_part3()

    elif choice == "2":
        pseudo = input("what is your pseudonym ?\n")
        while pseudo not in list_pseudonym():
            if pseudo == 'back':
                return menu_part3()
            elif pseudo == 'exit':
                return 0
            pseudo = input("what is your pseudonym ?\n")
        power = recommendBook(pseudo)
        if power == 1:
            return menu_part3()

    elif choice == "reset_scoring":
        resetRatingMatrix()
    elif choice == "reset_similarity":
        resetSimilarityMatrix()
    elif choice == "back":
        return 1
    elif choice == "exit":
        power = 0
    else:
        print("Invalid input")
        return menu_part3()

    if power == 0:
        return 0
    else:
        return 1


# This function allows to rate a book using the reader's name.
# It may take index_book, mark and index_reader as inputs if coming
# from addReader() since in this case it already knows which book to rate with which mark,
# otherwise they are defined with inputs.
def rateBook(reader, index_book=-1, mark=-1, index_reader=-1):
    books = open(books_file, "r")
    scoring_matrix = getMatrix(scoring_matrix_file)
    books_lines = books.readlines()
    # Determine whether the function is called from addReader() or not.
    if index_book == -1:
        index_reader = getIndexPseudonym(reader)
        list_books_read = reader_books(reader)

        cpt = 0
        # Display every books to allow the reader
        print(list_books_read)
        print(books_lines)
        for book in list_books_read:
            print(str(cpt+1) + ".", books_lines[int(book)-1])
            cpt += 1

        num_book_to_rate = input("Which book do you want to rate ?\n")
        if num_book_to_rate == 'back':
            return 1
        elif num_book_to_rate == 'exit':
            return 0

        mark = input("Rate this book, from 1 to 5\n")
        if mark == 'back':
            return rateBook(reader)
        elif mark == 'exit':
            return 0
        while int(mark) < 0 or int(mark) > 5:
            mark = int(input("Rate this book, from 1 to 5\n"))

        index_book = int(list_books_read[int(num_book_to_rate) - 1])
    # Insert the right mark in "rating_matrix.txt"
    scoring_matrix[index_reader][index_book - countDeletedBooks()] = str(mark)
    writeInFileMatrix(scoring_matrix_file, scoring_matrix)


def recommendBook(reader):
    # Computes the similarity matrix with the ratings from "rating_matrix.txt"
    resetSimilarityMatrix()
    similarity_matrix = getMatrix(similarity_matrix_file)
    rating_matrix = getMatrix(scoring_matrix_file)

    # Get the indexes of the reader and the books he has read
    books_read = reader_books(reader)
    index_reader = getIndexPseudonym(reader)
    max_similarity = 0.0
    index_max_sim_reader = -1
    books_not_in_common = []

    # If you didn't rate any books, you can't be similar to anyone so we avoid this case to happen.
    if emptyLine(rating_matrix[index_reader]):
        print("You must rate at least one book to get a book recommended")
        return 1
    # We look in the similarity_matrix to find another user with who the user is similar, and store that reader's
    # index and the score of similarity between the user and the reader.
    for i in range(len(similarity_matrix[index_reader])):
        j = similarity_matrix[index_reader][i]
        if float(j) > max_similarity and j != "0.00" and j != "1.00":
            max_similarity = float(j)
            index_max_sim_reader = i
    # If the maximum similarity found by the function stays at 0, it means that no one has read the same books as you.
    if max_similarity == 0:
        print("Sorry but you are not similar to any reader of our database...\n"
              "Maybe try to read more books in order to have some books recommended.")
        return 1

    # Create a list with every books the maximum similar reader has read that the user didn't read.
    books_read_max_sim = reader_books(getPseudonymIndex(index_max_sim_reader))
    for i in books_read_max_sim:
        if i not in books_read:
            books_not_in_common.append(i)
    if max_similarity >= 0.8:
        print("\nYou must like these books:\n")
    elif max_similarity >= 0.5:
        print("\nYou will probably like these books:\n")
    elif max_similarity >= 0.3:
        print("\nMaybe you will like these books:\n")
    else:
        print("\nYou could like these books:\n")

    # Prints every books of the list we just created.
    for k in range(len(books_not_in_common)):
        print(str(k+1) + ".", getBookWithIndex(books_not_in_common[k]).rstrip("\n"))
    selectbool = True
    # This "while" allow the user to select a book as read, and so add it to "booksread.txt" and "rating_matrix.txt"
    while selectbool:
        index_book = input("\nSelect a book\n")
        try:
            if 1 <= int(index_book) <= len(books_not_in_common):
                realindexbook = books_not_in_common[int(index_book)-1]
                selectbool = False
            else:
                print("invalid input: your number must be greater than 1 "
                      "and must not exceed " + str(len(books_not_in_common)))
        except ValueError:
            if index_book == "back":
                return 1
            elif index_book == "exit":
                return 0
            else:
                print("invalid input")

    # Get a mark from the user for the book he just selected
    mark = input("Give this book a mark, from 1 to 5\n")
    try:
        while int(mark) < 1 or int(mark) > 5:
            mark = input("Give this book a mark, from 1 to 5 included\n")
    except TypeError:
        if mark == "back":
            return recommendBook(reader)
        elif mark == "exit":
            return 0
        else:
            print("Please enter an integer, between 1 and 5")
    # This subfunction is writing in "booksread.txt" and "rating_matrix" the information needed
    addReadBook(index_reader, realindexbook, mark)


# This function stores a book and its mark given by an user in "booksread.txt" and "rating_matrix.txt"
def addReadBook(index_reader, index_book, mark):
    booksread = open(books_read_file, "r")
    scoring_matrix_lines = getMatrix(scoring_matrix_file)
    booksread_lines = booksread.readlines()

    booksread_lines[index_reader] = booksread_lines[index_reader].rstrip("\n")
    booksread_lines[index_reader] += "," + str(index_book) + "\n"
    booksread = open(books_read_file, "w")
    booksread.writelines(booksread_lines)

    scoring_matrix_lines[index_reader][int(index_book)-1] = mark
    writeInFileMatrix(scoring_matrix_file, scoring_matrix_lines)


# PART THREE SECONDARY FUNCTIONS


# This function resets the matrix to its original state.
def resetRatingMatrix():
    matrix_columns = []
    matrix_lines = []
    list_of_books = open(books_file, "r")
    readers = open(reader_file, "r")
    list_of_books_lines = list_of_books.readlines()
    readers_lines = readers.readlines()

    # These for computes how many lines (number of users) and columns (number of books) is needed in "rating_matrix.txt"
    for i in list_of_books_lines:
        if i != "\n":
            matrix_columns.append(i)
    for i in readers_lines:
        matrix_lines.append(str(i)[:-1])

    matrix = [["0" for j in range(len(matrix_columns))] for i in range(len(matrix_lines))]
    writeInFileMatrix(scoring_matrix_file, matrix)


# This function returns the name of a book from its index.
def getBookWithIndex(index):
    books = open(books_file, 'r')
    books_lines = books.readlines()
    return books_lines[int(index)-1]


# This function resets the similarity matrix to its original state
def resetSimilarityMatrix():
    books_readers = open(books_read_file, "r")
    similarity_matrix = open(similarity_matrix_file, "w")
    rating_matrix = getMatrix(scoring_matrix_file)
    books_readers_lines = books_readers.readlines()

    # Initializes the similarity matrix to 0s
    similarity_matrix_to_write = \
        [["0" for j in range(len(books_readers_lines))] for i in range(len(books_readers_lines))]

    similarity_matrix.close()
    for i in range(len(similarity_matrix_to_write)):
        for j in range(len(similarity_matrix_to_write)):
            if similarity_matrix_to_write[i][j] == "0":
                if i == j:
                    res = "1.00"
                elif not emptyLine(rating_matrix[i]) and not emptyLine(rating_matrix[j]):
                    res = round(float(cosineSimilarity(rating_matrix[i], rating_matrix[j])), 2)
                    res = ("%.2f" % res)
                    if res == 0.0:
                        res = "0.00"
                else:
                    res = "0.00"
                similarity_matrix_to_write[i][j], similarity_matrix_to_write[j][i] = str(res), str(res)
    writeInFileMatrix(similarity_matrix_file, similarity_matrix_to_write)


# This function computes the cosine similarity between two readers
def cosineSimilarity(notes1, notes2):
    numerator = 0
    norm1 = 0
    norm2 = 0
    for i in range(len(notes1)):
        numerator += (int(notes1[i]) * int(notes2[i]))
        norm1 += int(notes1[i]) ** 2
        norm2 += int(notes2[i]) ** 2
    res = numerator / (sqrt(norm1) * sqrt(norm2))
    return res


# This function will check if a list contains only zero. It returns True if a reader has not rated any books
def emptyLine(line):
    for i in line:
        if i != "0":
            return False
    return True


# This function returns a list of every books a reader has read using its pseudonym.
def reader_books(reader):
    books_read = open(books_read_file, "r")
    books_read_lines = books_read.readlines()
    for line in books_read_lines:
        list_line = line.split(",")
        if list_line[0] == reader:
            list_line[len(list_line)-1] = list_line[len(list_line)-1].replace('\n', '')
            return list_line[1:len(list_line)]


# This function returns the index of a reader using its pseudonym.
def getIndexPseudonym(pseudonym):
    list_of_pseudonym = list_pseudonym()
    for index in range(len(list_of_pseudonym)):
        if list_of_pseudonym[index] == pseudonym:
            return index


def getPseudonymIndex(index):
    list_of_pseudonym = list_pseudonym()
    return list_of_pseudonym[index]


# This function allows to write in the inputted file the inputted matrix with the right format. ( 0 1 0 1 0
#                                                                                                 1 0 1 1 1 )
def writeInFileMatrix(file, lst):
    matrix_file = open(file, "w")
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if j == len(lst[i]) - 1:
                matrix_file.write(lst[i][j])
            else:
                matrix_file.write(lst[i][j] + " ")
        matrix_file.write("\n")


# This function returns the number of books which are deleted in "books.txt"
def countDeletedBooks():
    count = 0
    books = open(books_file, "r")
    books_readlines = books.readlines()
    for i in books_readlines:
        if i == "\n":
            count += 1
    return count


# This function returns a list of every pseudonym in "readers.txt".
def list_pseudonym():
    f = open(reader_file, "r")
    cpt = 0
    readFile = f.read()
    lst_pseudonym = []
    for i in readFile:
        if i == "\n":
            cpt += 1
    for i in range(cpt):
        lst_pseudonym.append(readFile.split("\n")[i].split(",")[0])
    return lst_pseudonym


# This function allows to retrieve the matrix inside a variable of type list from the "rating_matrix.txt" file.
def getMatrix(file):
    matrix_file = open(file, "r")
    matrix = []
    matrix_to_append = matrix_file.readlines()
    for i in matrix_to_append:
        matrix.append(i.replace("\n", "").split(" "))
    return matrix
