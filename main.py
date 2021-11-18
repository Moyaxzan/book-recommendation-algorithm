from part1 import *
from part2 import *
from part3 import *

##todo faire le power off

if __name__ == "__main__":
    power = "on"
    print("Hi user ! don't forget, you can back at any time just by writing 'back'. Enjoy !")
    while power == "on":
        print("Write 1 to access part1 functions")
        print("Write 2 to access part2 functions")
        print("Write 3 to access part3 functions")
        choice = input("What do you want to do ?\n")
        if choice == "1":
            menu_part1()
        elif choice == "2":
            menu_part2()
        elif choice == "3":
            pass
        elif choice == "back":
            print("you cannot go back from here. \n")
        elif choice == "off":
            power = "off"
    print("\nHope you enjoyed ! Bye !")