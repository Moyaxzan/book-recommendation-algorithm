reader_file = "./Ressources/readers.txt"
books_read_file = "./Ressources/booksread.txt"
books_file = "./Ressources/books.txt"
scoring_matrix_file = "Ressources/rating_matrix.txt"
similarity_matrix_file = "Ressources/similarity_matrix.txt"



# PART THREE PRIMARY FUNCTIONS

def menu_part3():
    print("Write 1 to reset the matrix")
    print("Write 2 to get the matrix")
    print("Write 3 to rate a book")
    choice = input("What do you want to do ?\n")
    power = 1
    if choice == "1":
        resetRatingMatrix()
    elif choice == "2":
        getScoringMatrix()
    elif choice == "3":
        pseudo = input("what is your pseudonym ?\n")
        while pseudo not in list_pseudonym():
            pseudo = input("what is your pseudonym ?\n")
        power = rateBook(pseudo)
    elif choice == "4":
        resetSimilarityMatrix()
    if power == 0:
        return 0
    else:
        return 1

def resetRatingMatrix():
    matrix_columns = []
    matrix_lines = []
    list_of_books = open(books_file, "r")
    readers = open(reader_file, "r")
    matrix_file = open(scoring_matrix_file, "w")
    list_of_books_lines = list_of_books.readlines()
    readers_lines = readers.readlines()
    for i in list_of_books_lines:
        if i != "\n":
            matrix_columns.append(i)
    for i in readers_lines:
        matrix_lines.append(str(i)[:-1])
    matrix = [["0" for j in range(len(matrix_columns))] for i in range(len(matrix_lines))]
    writeInFileMatrix(scoring_matrix_file, matrix)

def getScoringMatrix():
    matrix_file = open(scoring_matrix_file, "r")
    matrix = []
    matrix_to_append = matrix_file.readlines()
    for i in matrix_to_append:
        matrix.append(i.replace("\n", "").split(" "))
    return matrix


def rateBook(reader, index_book = -1, mark = -1, index_reader = -1):
    books = open(books_file, "r")
    matrix = getScoringMatrix()
    books_lines = books.readlines()
    if index_book == -1:
        index_reader = getIndexPseudonym(reader)
        list_books_read = reader_books(reader)
        cpt = 0
        for book in list_books_read:
            print(str(cpt+1) + ".", books_lines[int(book)])
            cpt += 1
        num_book_to_rate = int(input("Which book do you want to rate ?\n"))
        index_book = int(list_books_read[num_book_to_rate-1])
        mark = int(input("Rate this book, from 1 to 5\n"))
        while mark < 0 or mark > 5:
            mark = int(input("Rate this book, from 1 to 5\n"))
    matrix[index_reader][index_book - countDeletedBooks()] = str(mark)
    writeInFileMatrix(scoring_matrix_file, matrix)

def resetSimilarityMatrix():
    books_readers = open(books_read_file, "r")
    similarity_matrix = open(similarity_matrix_file, "w")
    rating_matrix = getScoringMatrix()
    books_readers_lines = books_readers.readlines()
    ### Initializes the similarity matrix to 0s
    similarity_matrix_to_write = [["0" for j in range(len(books_readers_lines))] for i in range(len(books_readers_lines))]
    writeInFileMatrix(similarity_matrix_file, similarity_matrix_to_write)


### PART THREE SECONDARY FUNCTIONS

def reader_books(reader):
    books_read = open(books_read_file, "r")
    books_read_lines = books_read.readlines()
    for line in books_read_lines:
        list_line = line.split(",")
        if list_line[0] == reader:
            list_line[len(list_line)-1] = list_line[len(list_line)-1].replace('\n', '')
            return list_line[1:len(list_line)]

def getIndexPseudonym(pseudonym):
    list_of_pseudonym = list_pseudonym()
    for i in range(len(list_of_pseudonym)):
        if list_of_pseudonym[i] == pseudonym:
            index = i
    return index


def writeInFileMatrix(file,list):
    matrix_file = open(file, "w")
    for i in range(len(list)):
        for j in range(len(list[i])):
            if j == len(list[i]) - 1:
                matrix_file.write(list[i][j])
            else:
                matrix_file.write(list[i][j] + " ")
        matrix_file.write("\n")

def countDeletedBooks():
    count=0
    books = open(books_file, "r")
    books_readlines= books.readlines()
    for i in books_readlines:
        if i=="\n":
            count+=1
    return count
def list_pseudonym():
    f = open(reader_file, "r")
    cpt = 0
    readedFile = f.read()
    list_pseudonym = []
    for i in readedFile:
        if i == "\n":
            cpt += 1
    for i in range(cpt):
        list_pseudonym.append(readedFile.split("\n")[i].split(",")[0])
    return list_pseudonym
