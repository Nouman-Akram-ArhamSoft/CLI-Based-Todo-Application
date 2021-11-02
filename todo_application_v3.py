# pylint: disable=true
import os
import json
from datetime import datetime
from json.decoder import JSONDecodeError


def read_json_file(file):
    '''
    Create a JSON File if not exit and return the data from JSON File.

            Parameters:
                    file (str): File Name
            Returns:
                    JSON Data (Dict): Returns the data of JSON file
    '''
    try:
        with open(file, 'r') as readfile:
            return json.load(readfile)

    except JSONDecodeError:
        write_empty_data = open(file, 'w')
        json.dump({}, write_empty_data)
        write_empty_data.close()


def add_task(file, task_input):
    '''
    Add Respective User Input Task in JSON File.

            Parameters:
                    JSON_File  (str): File Name
                    task_input (str): data to input in task List
            Returns:
                    JSON Data (Massage): show completion massage of added task
    '''
    data = read_json_file(file)

    if task_input not in data.keys():
        data[task_input] = str(datetime.now())[:16]
       
        print("\n"+("-"*50))
        print(f"Successfully added '{task_input}' to list")
        print("-"*50)
    else:
        print("\n"+("-"*50))
        print("Task already in List enter your next task")
        print("-"*50)

    with open(file, 'w') as writedata:
        json.dump(data, writedata)


def view_task(json_file):
    '''
    View the all Task List from JSON File

            Parameters:
                    JSON_File  (str): File Name
            Returns:
                    Massage : Show all the data of JSON file
    '''

    task_list = read_json_file(json_file)

    item_no = 0
    if len(task_list) > 0:
        for key, value in task_list.items():
            item_no += 1
            print("-"*50)
            print(f"{item_no} -- {key} -- Created on -- {value}")
            print("-"*50)
    else:
        print("\n"+("-"*50))
        print("No Pending Task is Left")
        print("-"*50)
        


def done_task(json_file, task_number):
    '''
    Remove the completed task from JSON file

            Parameters:
                    JSON_File   (str): File Name
                    task_number (int): respective task number
            Returns:
                    Massage : Display the respective Done Massage
    '''

    task_list = read_json_file(json_file)
    
    if task_number in range(1, len(task_list)+1):
        task_number -= 1

        for index, key in enumerate(task_list.keys()):
            if task_number == index:
                print("\n"+("-"*50))
                print(f"Successfully Completed the '{key}' Task")
                print("-"*50)
                del task_list[key]
                break
    else:
        print("\n"+("-"*50))
        print("No Data is Found in Task List Please Enter the valid Number")           
        print("-"*50)

    with open(json_file, 'w') as writefile:
        json.dump(task_list, writefile)


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

    if not os.path.isfile('todo.json'):
        createfile = open('todo.json', 'w').close()

    JSON_TO_DO_FILE = read_json_file('todo.json')

    while True:

        JSON_TO_DO_FILE = 'todo.json'


        print("\n\t------------------------")
        print("\tEnter 1 to Add Item : ")
        print("\t------------------------")
        print("\tEnter 2 to Done Item : ")
        print("\t------------------------")
        print("\tEnter 3 to View Item : ")
        print("\t------------------------")
        print("\tEnter 4 to Exit : ")
        print("\t------------------------")

        USER_INPUT = get_valid_integer("\nEnter Your choice : ")

        if USER_INPUT == 1:
            try:
                task_input = input("\nEnter the task to do : ").title()
                add_task(JSON_TO_DO_FILE, task_input)
            except (TypeError, ValueError, EOFError):
                print('Please enter the valid input')
        elif USER_INPUT == 2:
            view_task(JSON_TO_DO_FILE)
            complete_task_input = get_valid_integer("Enter the Respective task number for completion : ")
            done_task(JSON_TO_DO_FILE, complete_task_input)

        elif USER_INPUT == 3:
            view_task(JSON_TO_DO_FILE)

        elif USER_INPUT == 4:
            print("Thanks For using TODO Application Please come again ..")
            break

        else:
            print("\nYou have Enter the wrong input, Please enter again")
