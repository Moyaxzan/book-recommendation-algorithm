from part1 import *
from part2 import *
from part3 import *
### MENU FUNCTIONS

def menu_part1():
    print("Write 1 to display books")
    print("Write 2 to add a reader")
    print("Write 3 to view a reader")
    print("Write 4 to edit a reader")
    print("Write 5 to delete a reader")
    print("Write 'back' to return to the last menu")
    choice = input("What do you want to do ?\n")
    if choice == "1":
        displayBooks()
    if choice == "2":
        addReader()
    if choice == "3":
        pseudo = input("what pseudo do you want to view ?\n")
        viewReader(pseudo)
    if choice == "4":
        pseudo = input("what pseudo do you want to edit ?\n")
        editReader(pseudo)
    if choice == "5":
        pseudo = input("what pseudo do you want to edit ?\n")
        deleteReader(pseudo)
    if choice == "back":
        base_menu()


def menu_part2():
    print("Write 1 to add a book")
    print("Write 2 to edit a book")
    print("Write 3 to delete a book")
    print("Write 'back' to return to the last menu")
    choice = input("What do you want to do ?\n")
    if choice == "1":
        addBook()
    if choice == "2":
        editBook()
    if choice == "3":
        deleteBook()
    if choice == "back":
        base_menu()


def base_menu():
    print("Write 1 to access part1 functions")
    print("Write 2 to access part2 functions")
    print("Write 3 to access part3 functions")
    choice = int(input("What do you want to do ?\n"))
    if choice == 1:
        menu_part1()
    if choice == 2:
        menu_part2()
    if choice == 3:
        pass

