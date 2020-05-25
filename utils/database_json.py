import json

def book_add(user_nb_title, user_nb_author, user_nb_read):
    new_book = {'Title': (user_nb_title), 'Author': (user_nb_author), 'Read': (user_nb_read)}
    with open("utils/books_database.json", "r") as add_new_book:
        Books = json.load(add_new_book)
        temp = Books['Books']
        temp.append(new_book)
    with open("utils/books_database.json", "w") as add_new_book:
        json.dump(Books, add_new_book, indent=4)

book_add("LOTR1", 'Tolkien2', True)

def book_read(user_rb_title):
    with open("utils/Books_json.txt", "w+") as book_set_read:
        for n in book_set_read:
            if n["Title"] == user_rb_title:
                n["Read"] = True

def book_delete():
    user_rb_title = (input("Enter title of the book you'd like to remove: "))
    with open("utils/Books_json.txt", "w+") as book_remove:
        for n in book_remove:
            if n["Title"] == user_rb_title:
                book_remove.remove(n)



"""


def book_add(user_nb_title, user_nb_author, user_nb_read):
    new_book = ({'Title': (user_nb_title), 'Author': (user_nb_author), 'Read': (user_nb_read)})
    with open("utils/Books_json.txt", "r") as add_new_book:
        Books = json.load(add_new_book)
        temp = Books['Books']
        temp.append(new_book)
    with open("utils/Books_json.txt", "w") as add_new_book:
        json.dump(Books, add_new_book, indent=4)


{
    "Books": [
        {
            "Title": "Krew Elfow", 
            "Author": "Sapkowski", 
            "Read": "False"
        }
    ]
}

"""