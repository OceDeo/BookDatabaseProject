
from utils import database_json

USER_CHOICE = """
- "a" to add a new book
- "l" to list all books
- "r" to mark a book as read
- "d" to delete a book
- "q" to quit
Enter: """

def menu():
    user_input = input(USER_CHOICE)
    while user_input != "q":
        if user_input == "a":
            user_nb_title = input("Title: ")
            user_nb_author = input("Author: ")
            user_nb_read = input("Did you read the book already?(y/n): ") == "y"
            database_json.book_add(user_nb_title, user_nb_author, user_nb_read)
        elif user_input == "r":
            user_rb_title = input("Book title to mark as read: ")
            database_json.book_read(user_rb_title)
        elif user_input == "d":
            user_delete_title = input("Enter title to delete: ")
            database_json.book_delete(user_delete_title)
        elif user_input == "l":
            print(database_json.books_list())
        user_input = input(USER_CHOICE)

menu()