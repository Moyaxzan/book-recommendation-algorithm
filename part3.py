reader_file = "./Ressources/readers.txt"
books_read_file = "./Ressources/booksread.txt"
books_file = "./Ressources/books.txt"
scoring_matrix_file = "Ressources/rating_matrix.txt"

from part1 import *

# PART THREE PRIMARY FUNCTIONS

def menu_part3():
    print("Write 1 to reset the matrix")
    print("Write 2 to get the matrix")
    print("Write 3 to rate a book")
    choice = input("What do you want to do ?\n")
    power = 1
    if choice == "1":
        resetMatrix()
    elif choice == "2":
        getMatrix()
    elif choice == "3":
        pseudo = input("what is your pseudonyme ?\n")
        while pseudo not in list_pseudonym():
            pseudo = input("what is your pseudonyme ?\n")
        power = rateBook(pseudo)
    if power == 0:
        return 0
    else:
        return 1

def resetMatrix():
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
    for i in range(len(matrix_lines)):
        for j in range(len(matrix_columns)):
            if j == len(matrix_columns) - 1:
                matrix_file.write(matrix[i][j])
            else:
                matrix_file.write(matrix[i][j] + " ")
        matrix_file.write("\n")

def getMatrix():
    matrix_file = open(scoring_matrix_file, "r")
    matrix = []
    matrix_to_append = matrix_file.readlines()
    for i in matrix_to_append:
        matrix.append(i.replace("\n", "").split(" "))
    return matrix

def rateBook(reader, *args):
    books = open(books_file, "r")
    matrix = getMatrix()
    books_lines = books.readlines()
    if args == ():
        list_books_read = reader_books(reader)
        cpt = 0
        for book in list_books_read:
            print(str(cpt+1) + ".", books_lines[int(book)])
            cpt += 1
        book_to_rate = input("Which book do you want to rate ?\n")
    else:
        book_to_rate = args[0]
    note = int(input("Rate this book, from 1 to 5\n"))

def reader_books(reader):
    books_read = open(books_read_file, "r")
    books_read_lines = books_read.readlines()
    for line in books_read_lines:
        list_line = line.split(",")
        if list_line[0] == reader:
            list_line[len(list_line)-1] = list_line[len(list_line)-1].replace('\n', '')
            return list_line[1:len(list_line)]





