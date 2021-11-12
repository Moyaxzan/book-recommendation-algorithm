reader_file = "./Ressources/readers.txt"
books_read_file = "./Ressources/booksread.txt"
books_file = "./Ressources/books.txt"
dicogenre = {1: "sci-fi", 2: "Biography", 3: "Horror", 4: "Romance", 5: "Fable", 6: "History", 7: "Comedy"}
##todo make a dico for all of arguments ?
###  PART ONE PRIMARY FUNCTIONS

def displayBooks(list_of_books=books_file):
    ### Open the "books.txt" file
    f = open(list_of_books, "r")
    ### Puts every books into a list "books"
    books = f.readlines()
    for i in range(len(books)):
        print(str(i) + ".", books[i])


def addReader():
    ### Open the "readers.txt" and "booksread.txt" files
    readers = open(reader_file, "a")
    books_read = open(books_read_file, "a")
    ### Calls createLineReader() which create the right line to insert into "readers.txt" and "booksread.txt" files
    line_reader_file, line_books_read = createLineReader()
    if line_reader_file == None and line_books_read == None:
        return
    ### Write into "readers.txt" and "booksread.txt" the lines we just created
    readers.write(line_reader_file)
    books_read.write(line_books_read)
    readers.close()
    books_read.close()


def viewReader(pseudonym):
    ### Opens the "readers.txt" and create a list of the lines
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
        print("no")


def editReader(pseudonym):
    readers = open(reader_file, "r")
    book_reads = open(books_read_file, "r")
    readers_lines = readers.readlines()
    book_reads_lines = book_reads.readlines()
    line_readers, line_books_read = createLineReader()
    if line_readers == None and line_books_read == None:
        return
    index = getIndexPseudonym(pseudonym)
    readers_lines[index] = line_readers
    book_reads_lines[index] = line_books_read
    readers = open(reader_file, "w")
    book_reads = open(books_read_file, "w")
    readers.writelines(readers_lines)
    book_reads.writelines(book_reads_lines)
    readers.close()
    book_reads.close()


def deleteReader(pseudonym):
    readers = open(reader_file, "r")
    book_reads = open(books_read_file, "r")
    readers_lines = readers.readlines()
    book_reads_lines = book_reads.readlines()
    index = getIndexPseudonym(pseudonym)
    readers_lines.pop(index)
    book_reads_lines.pop(index)
    readers = open(reader_file, "w")
    book_reads = open(books_read_file, "w")
    readers.writelines(readers_lines)
    book_reads.writelines(book_reads_lines)
    readers.close()
    book_reads.close()


### PART ONE SECONDARY FUNCTIONS

def getIndexPseudonym(pseudonym):
    list_of_pseudonym = list_pseudonym()
    for i in range(len(list_of_pseudonym)):
        if list_of_pseudonym[i] == pseudonym:
            index = i
    return index


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


def createLineReader():
    pseudobool = True
    genderbool = True
    agebool = True
    readingStylebool = True
    list_of_books = open(books_file, "r")
    list_pseudonyms = list_pseudonym()
    while pseudobool:
        pseudo = input("What is your pseudonym ?\n")
        if pseudo == "back":
            return None, None
        if len(pseudo) >= 3:
            pseudobool = False
        else:
            print("invalide input : your pseudonym must exceed 2 characters.")
        if pseudo not in list_pseudonyms:
            pseudobool = False
        else:
            print("invalide input : pseudonym already taken")
    while genderbool:
        print("PRESS : ")
        print("1 if you are a man")
        print("2 if you are a woman")
        print("3 if you don't want to specify")
        gender = input()
        if gender == "1" or gender == "2" or gender == "3":
            genderbool = False
        elif gender == "back":
            return None, None
        else:
            print("invalide input : you need to type 1, 2 or 3")
    while agebool:
        print("PRESS : ")
        print("1 if you are 18 years old")
        print("2 if you are between 18 and 25 years old")
        print("3 if you are over 25 years old")
        age = int(input())
        if age == 1 or age == 2 or age == 3:
            agebool = False
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
        readingStyle = int(input())
        if readingStyle >= 1 and readingStyle <= 7:
            readingStylebool = False
        else:
            print("invalide input : you need to type a number between 1 and 7")
    line_reader = str(pseudo) + ", " + str(gender) + ", " + str(age) + ", " + str(readingStyle) + "\n"
    print("Which books have you read ?")
    ### Prints every books in the file books.txt
    liste = list_of_books.readlines()
    for i in range(len(liste)):
        print(i, liste[i])
    appendBool = True
    ### Initialize a string that we will append to the file when the user is over adding books
    line_books_read = ""
    ### Adds the pseudonym of the user
    line_books_read += str(pseudo) + ","
    ### This while adds every book the user has read
    while appendBool:
        input_livres = input("Enter a number or 'over' if you are finished\n")
        try:
            int(input_livres)
            line_books_read += input_livres + ","
        except:
            if input_livres == "over":
                appendBool = False
    ### Remove the last comma to avoid having one too much
    line_books_read = line_books_read[0:len(line_books_read) - 1]
    line_books_read += "\n"
    return line_reader, line_books_read

