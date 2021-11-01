import os
import time


class ToDo:
    """
    A ToDo class to maintain the daily task work of user

    ...

    Attributes
    ----------
    file : str
        File name to record toDo list

    Methods
    -------
    add_item(input_item):
        add the item in todo file

    done_item():
        remove the completed item from file

    view_item():
        View the all items in files

    static method
    open_file(file: str):
        use to create or read the file

    static method
    get_valid_integer(massage: str):
        use to ensure the valid integer data from user
    """

    def __init__(self, file):
        self.file = file

    def add_item(self, input_item):
        '''
        Add Item in Text File to Maintain the ToDo List.
                Parameters:
                        Task (str): Task to add in Files
                Returns:
                        Massege : Returns the massage for successfully added task or not.
        '''
        if os.path.isfile(self.file):
            todo_file = open(self.file, 'r+')
            contents = todo_file.read()
        else:
            todo_file = open(self.file, 'w')
            contents = []

        if input_item in contents:
            print("You have Already this task in your Schedule")
            new_task_input = input(
                "\nEnter again to add item : ").title().rstrip()
            self.add_item(new_task_input)

        else:
            print(input_item, file=todo_file)
            print("\n" + ("*"*40))
            print(f"Successfully added '{input_item}' in task list")
            print("*"*40)
        todo_file.close()

    def done_item(self):
        '''
        Remove the Item from ToDo Text File.
                Parameters:
                        None
                Returns:
                        Massege : Returns the massage for successfully removed the Task
        '''
        contents = self.view_items()

        if contents:
            choice = ToDo.get_valid_integer(
                "Enter the respective item Number for Done Task : ")
            if choice is not None:
                choice = choice - 1

                if choice in range(len(contents)):
                    done_task = contents.pop(choice)

                    if not contents:
                        with open(self.file, 'w') as emptyfile:
                            print(file=emptyfile, end="")
                    else:
                        update_todo_file = open(self.file, 'w')
                        for item in contents:
                            update_todo_file.write(item)
                        update_todo_file.close()

                    print("\n" + ("*"*50))
                    print(
                        f'You have Successfully remove item {done_task.rstrip()}')
                    print("*"*50)
                else:
                    print("\nYou have enter invalid item number please enter again ..")

    def view_items(self):
        '''
        View the Item from ToDo Text File.
                Parameters:
                        None
                Returns:
                        Massege : Returns the massage for all the items in ToDO File
        '''

        todo_file = ToDo.open_file(self.file)
        contents = []
        if todo_file is not None:
            contents = todo_file.readlines()
            todo_file.close()

        if contents:
            for index, context in enumerate(contents):
                print("-"*40)
                print(f"Item No {index+1} to do ==> {context.rstrip()}")
                print("-"*40)
            time.sleep(1)
        else:
            print("\n" + ("*"*30))
            print("No Status to Do")
            print("*"*30)

        return contents


    @staticmethod
    def open_file(file):
        '''
        Create a File if not exit and return the read mode file.

                Parameters:
                        file (str): File Name
                Returns:
                        FilePath (str): Returns the path of file
        '''

        while not os.path.isfile(file):

            print("No File is Found")
            choice = input(
                "Do you want to Create new file (Y/n) : ").casefold()

            if choice == 'y':
                open(file, 'w').close()
                print("File Created Successfully")
            elif choice == 'n':
                print("No File is Created Please Enter Data in ToDo List to create file")
                break
            else:
                print("You have Enter the Wrong input, kindly input again ..")

        else:
            read_todo_file = open(file, 'r')
            return read_todo_file

    @staticmethod
    def get_valid_integer(massage):
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


if __name__ == '__main__':

    print("*"*40)
    print("Welcome to Command Line To Do Application")
    print("*"*40)
    USER_TASK = ToDo('ToDo_List.txt')

    while True:

        print("\n\t------------------------")
        print("\tEnter 1 to Add Item : ")
        print("\t------------------------")
        print("\tEnter 2 to Done Item : ")
        print("\t------------------------")
        print("\tEnter 3 to View Item : ")
        print("\t------------------------")
        print("\tEnter 4 to Exit : ")
        print("\t------------------------")

        USER_INPUT = USER_TASK.get_valid_integer("\nEnter Your choice : ")

        if USER_INPUT == 1:
            DO_ITEM = input("What is to be done : ").casefold().rstrip()
            USER_TASK.add_item(DO_ITEM.title())
        elif USER_INPUT == 2:
            USER_TASK.done_item()

        elif USER_INPUT == 3:
            USER_TASK.view_items()

        elif USER_INPUT == 4:
            print("Thanks For using TODO Application Please come again ..")
            break

        else:
            print("\nYou have Enter the wrong input, Please enter again")
