reader_file = "./Ressources/readers.txt"
books_read_file = "./Ressources/booksread.txt"
books_file = "./Ressources/books.txt"
scoring_matrix_file = "./Ressources/scoring_matrix.txt"

from part1 import *

# PART THREE PRIMARY FUNCTIONS

def menu_part3():
    choice = input("What do you want to do ?\n")
    power=1
    if choice=="1":
        resetMatrix()
    elif choice=="2":
        getMatrix()
    elif choice=="3":
        power=rateBook("23")
    if power == 0:
        return 0
    else:
        return 1

def resetMatrix():
    matrix_columns=[]
    matrix_lines=[]
    list_of_books = open(books_file,"r")
    readers = open(reader_file,"r")
    matrix_file = open(scoring_matrix_file,"w")
    list_of_books_lines = list_of_books.readlines()
    readers_lines = readers.readlines()
    for i in list_of_books_lines:
        if i!="\n":
            matrix_columns.append(i)
    for i in readers_lines:
        matrix_lines.append(str(i)[:-1])
    matrix=[["0" for j in range(len(matrix_columns))] for i in range(len(matrix_lines))]
    for i in range(len(matrix_lines)):
        for j in range(len(matrix_columns)):
            if j == len(matrix_columns) - 1:
                matrix_file.write(matrix[i][j])
            else:
                matrix_file.write(matrix[i][j]+",")
        matrix_file.write("\n")

def getMatrix():
    matrix_file=open(scoring_matrix_file,"r")
    matrix=[]
    matrix_to_append=matrix_file.readlines()
    for i in matrix_to_append:
        matrix.append(i.replace("\n","").split(","))
    return matrix

def rateBook(*args,reader):
    books=open(books_file,"r")
    matrix=getMatrix()
    books_readlines=books.readlines()
    if args==():
        for i in range(len(books_readlines)):
            print(str(i) + ".", books_readlines[i])
        book_to_rate=input("Which book do you want to rate ?")
    else:
        book_to_rate=args[0]
    note=int(input("Rate this book, from 1 to 5"))






