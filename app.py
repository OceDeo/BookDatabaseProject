
from utils import database_json, database_csv, database, database_sql

USER_CHOICE = """
- a - Add a new book
- l - List all books
- r - Mark a book as read
- d - Delete a book
- b - Go back to database type selection
- q - EXIT
Enter: """

user_input_selection = """Which database type you'd like to use?:
- 1 - Temporary
- 2 - CSV
- 3 - JSON
- 4 - SQLite
- q - EXIT
Enter: """

database_type = False

def menu(database_type):
    user_input = input(USER_CHOICE)
    while user_input != "b":
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
        elif user_input == "q":
            exit()
        else:
            print("Unexpected input, please try again.")
        user_input = input(USER_CHOICE)



def database_sel():
    user_input_sel = input(user_input_selection)
    while user_input_sel != "q":
        if user_input_sel == "4":
            database_type = database_sql
            menu(database_type)
        elif user_input_sel == "3":
            database_type = database_json
            menu(database_type)
        elif user_input_sel == "2":
            database_type = database_csv
            menu(database_type)
        elif user_input_sel == "1":
            database_type = database
            menu(database_type)
        elif user_input_sel == "q":
            exit()
        else:
            print("Unexpected input, please try again.")
        user_input_sel = input(user_input_selection)

def main():
    database_sel()

if __name__ == "__main__":
    main()
