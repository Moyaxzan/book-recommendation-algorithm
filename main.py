# from part1 import
from part2 import *
from part3 import *

if __name__ == "__main__":
    power = 1
    print("Hi user ! don't forget, "
          "you can back at any time just by writing 'back' and exit by just writting 'exit'. "
          "Enjoy !")
    while power == 1:
        print("Write 1 to access part1 (readers part)")
        print("Write 2 to access part2 functions (books part)")
        print("Write 3 to access part3 functions (ratings/recommendations part)")
        choice = input("What do you want to do ?\n")
        if choice == "1":
            power = menu_part1()
        elif choice == "2":
            power = menu_part2()
        elif choice == "3":
            power = menu_part3()
        elif choice == "back":
            print("You cannot go back from here. \n")
        elif choice == "exit":
            power = 0
    print("\nHope you enjoyed ! Bye !")
