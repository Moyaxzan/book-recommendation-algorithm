reader_file = "./Ressources/readers.txt"
books_read_file = "./Ressources/booksread.txt"
books_file = "./Ressources/books.txt"
scoring_matrix_file = "./Ressources/scoring_matrix.txt"

# PART THREE PRIMARY FUNCTIONS

def menu_part3():
    choice = input("What do you want to do ?\n")
    if choice=="1":
        resetMatrix()
    if choice=="2":
        printMatrix()
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
    for i in range(len(matrix)):
        matrix_file.writelines(str(matrix[i]))


def printMatrix():
    matrix_file=open(scoring_matrix_file,"r")
    matrix=matrix_file.readlines()
    for i in matrix:
        print(i)
    print(matrix)

