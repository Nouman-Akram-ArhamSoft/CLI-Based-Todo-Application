# CLI-Based-Todo-Application
Manage your Daily task and maintain your record in specific file


## Todo-Application Basic Task

- Main Todo Class

Attributes

- File (Take the name of file)

Methods

- add_item(input_item)  -> take the input from user and add it in todo file
- done_item()           -> Remove the Done task from todo file
- view_item()           -> View all the todo task
- open_file()           -> use to create or open the file
- get_valid_integer()   -> use to get the valid integer from user

Library Used

- os library -> use to get the path and file directory
- time library -> use to take sleep function so when user view item it sleep their for 1 second

