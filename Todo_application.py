# pylint: disable=invalid-name

import os
import time

def open_file(file: str):
    '''
    Create a File if not exit and return the read mode file.

            Parameters:
                    file (str): File Name
            Returns:
                    FilePath (str): Returns the path of file
    '''
    choice = "y"
    while not os.path.isfile(file):
        print("File Not Exits")
        choice = input("Do you want to create new file (Y/n): ").casefold()
        if choice == 'y':
            write_open_file = open(file, 'w')
            write_open_file.close()
            print("File Successfully Created")
        elif choice == 'n':
            print("No File is Created Please Enter Data in ToDo List to create file")
            break
        else:
            print("Please Enter the valid input : ")
    if choice == 'y' and os.path.isfile(file):
        read_open_file = open(file, 'r')
        return read_open_file


def close_file(file: str)-> None:
    '''
    Close the open file.

            Parameters:
                    file (str): File Name
            Returns:
                    None
    '''
    file.close()


def get_valid_integer(massage: str) -> int:
    '''
    Return the Valid Integer values and check valid inputs from user.
            Parameters:
                    massage (str): Massage to show user
            Returns:
                    integer (int): valid integer number
    '''
    user_entry = ''
    try:
        user_entry = int(input(massage))
        return user_entry
    except (TypeError, ValueError) as err:
        print(f'\n"{err}" , Please Enter the Integer Number')

    except EOFError as err:
        print(f'\n"{err}" , Cannot Read This Please input something else')


def add_item(task: str) -> None:
    '''
    Add Item in Text File to Maintain the ToDo List.
            Parameters:
                    Task (str): Task to add in Files
            Returns:
                    Massege : Returns the massage for successfully added task or not.
    '''
    if os.path.isfile('todo.txt'):
        todo = open('todo.txt', 'r+')
        contents = todo.read()
    else:
        todo = open('todo.txt', 'w')
        contents = []

    if task in contents:
        print("\n" + ("*"*40))
        print("You have Already this task in your Schedule")
        print("*"*40)

        input_name = input(
            "\nEnter again to add item : ").casefold().rstrip()
        add_item(input_name.title())

    else:
        print(task, file=todo)
        print("\n" + ("*"*40))
        print(f"Successfully added '{task}' in task list")
        print("*"*40)

    todo.close()


def done_task():
    '''
    Remove the Item from ToDo Text File.
            Parameters:
                    None
            Returns:
                    Massege : Returns the massage for successfully removed the Task
    '''
    contents = view_task()

    if contents:

        choice = get_valid_integer(
            "Press the respective ID to Done the Status : ")
        if choice is not None:
            choice = choice - 1

            if choice in range(0, len(contents)):

                removed_item = contents.pop(choice)

                if not contents:
                    with open('todo.txt', 'w') as emptyfile:
                        print(file=emptyfile, end="")
                else:
                    writefile = open('todo.txt', 'w')
                    for item in contents:
                        writefile.write(item)
                    writefile.close()

                print("\n" + ("*"*50))
                print(
                    f'You have Successfully remove item {removed_item.rstrip()}')
                print("*"*50)

            else:
                print("\nYou have enter invalid item number please enter again ..")

    else:
        print("\nNo Item left to be Done")


def view_task():
    '''
    View the Item from ToDo Text File.
            Parameters:
                    None
            Returns:
                    Massege : Returns the massage for all the items in ToDO File
    '''

    todo = open_file('todo.txt')
    contents = []
    if todo is not None:
        contents = todo.readline()
        close_file(todo)

    if contents:

        for index, item in enumerate(contents):
            print("-"*40)
            print(f"Item No {index+1} to do ==> {item.rstrip()}")
            print("-"*40)
        time.sleep(1)

    else:
        print("\n" + ("*"*30))
        print("No Status to Do")
        print("*"*30)

    return contents


if __name__ == '__main__':

    print("*"*40)
    print("Welcome to Command Line To Do Application")
    print("*"*40)

    while True:

        print("\n\t------------------------")
        print("\tEnter 1 to add Item : ")
        print("\t------------------------")
        print("\tEnter 2 to Done Item : ")
        print("\t------------------------")
        print("\tEnter 3 to View Item : ")
        print("\t------------------------")
        print("\tEnter 4 to Exit : ")
        print("\t------------------------")

        user_input = get_valid_integer("\nEnter Your choice : ")

        if user_input == 1:
            do_item = input("What is to be done : ").casefold().rstrip()
            add_item(do_item.title())
        elif user_input == 2:
            done_task()

        elif user_input == 3:
            view_task()

        elif user_input == 4:
            print("Thanks For using TODO Application Please come again ..")
            break

        else:
            print("\nYou have Enter the wrong input, Please enter again")
