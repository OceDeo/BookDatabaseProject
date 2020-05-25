
from utils import database_json, database_csv, database

USER_CHOICE = """
- "a" to add a new book
- "l" to list all books
- "r" to mark a book as read
- "d" to delete a book
- "q" to go back / quit
Enter: """

user_input_selection = """Which database type you'd like to use?:
- 1 - Temporary
- 2 - CSV
- 3 - JSON
- q - to quit
Enter: """

database_type = False

def menu():
    user_input = input(USER_CHOICE)
    while user_input != "q":
        if user_input == "a":
            user_nb_title = input("Title: ")
            user_nb_author = input("Author: ")
            user_nb_read = input("Did you read the book already?(y/n): ") == "y"
            database_type.book_add(user_nb_title, user_nb_author, user_nb_read)
        elif user_input == "r":
            user_rb_title = input("Book title to mark as read: ")
            database_type.book_read(user_rb_title)
        elif user_input == "d":
            user_delete_title = input("Enter title to delete: ")
            database_type.book_delete(user_delete_title)
        elif user_input == "l":
            database_type.book_list()
        else:
            print("Unexpected input, please try again.")
        user_input = input(USER_CHOICE)

user_input_sel = input(user_input_selection)

while user_input_sel != "q":
    if user_input_sel == "3":
        database_type = database_json
        menu()
    elif user_input_sel == "2":
        database_type = database_csv
        menu()
    elif user_input_sel == "1":
        database_type = database
        menu()
    else:
        print("Unexpected input, please try again.")
    user_input_sel = input(user_input_selection)

