import json

def book_add(user_nb_title, user_nb_author, user_nb_read):
    new_book = {'Title': (user_nb_title), 'Author': (user_nb_author), 'Read': (user_nb_read)}
    with open("utils/books_database.json", "r") as add_new_book:
        Books = json.load(add_new_book)
        temp = Books['Books']
        temp.append(new_book)
    with open("utils/books_database.json", "w") as add_new_book:
        json.dump(Books, add_new_book, indent=4)


def book_read(user_rb_title):
    with open("utils/books_database.json", "r") as book_set_read:
        Books = json.load(book_set_read)
        temp = Books['Books']
        for n in temp:
            if n["Title"] == user_rb_title:
                n["Read"] = True
                print(f"{user_rb_title} has be set as read") 
    with open("utils/books_database.json", "w") as book_set_read:
        json.dump(Books, book_set_read, indent=4)


def book_list():
    with open("utils/books_database.json", "r") as book_set_read:
        Books = json.load(book_set_read)
        dict = Books['Books']
        for n in dict:
            x = "Finished." if n["Read"] == True else "Not finished."
            print(f'{n["Title"]} by {n["Author"]}. {x}')


def book_delete(user_remove_title):
    with open("utils/books_database.json", "r") as book_set_read:
        Books = json.load(book_set_read)
        temp = Books['Books']
        for n in temp:
            if n["Title"] == user_remove_title:
                temp.remove(n)
                print("Book has been removed from the list.")
    with open("utils/books_database.json", "w") as book_set_read:
        json.dump(Books, book_set_read, indent=4)


