Books_list = "utils/books_csv.txt"


def book_add(user_nb_title, user_nb_author, user_nb_read):
    with open(Books_list, "a") as books:
        books.write(f'{user_nb_title},{user_nb_author},{user_nb_read}\n')


def book_read(user_rb_title):
    temp_list = []
    with open(Books_list, "r") as books_databaselist:
        for n in books_databaselist.readlines():
            title, author, status = n.split(",")
            if title == user_rb_title:
                if status.strip() == 'False':
                    status = 'True'
                    print(f"{user_rb_title} has be set as read") 
                elif status.strip() == 'True':
                    print(f"{user_rb_title} is already read")
            temp_list.append(f'{title},{author},{status.strip()}\n')
    with open(Books_list, "w") as books_databaselist:
        for n in temp_list:
            books_databaselist.writelines(n)


def book_list():
    with open(Books_list, "r") as books_databaselist:
        for n in books_databaselist.readlines():
            title, author, status = n.split(",")
            if status.strip() == 'False':
                status_1 = "Not yet finished."
            elif status.strip() == 'True':
                status_1 = "Book finished."
            else:
                return ''
            print(f'{title} by {author}. {status_1}')
        else:
            return ''


def book_delete(user_to_remove):
    temp_list = []
    with open(Books_list, "r") as books_databaselist:
        for n in books_databaselist.readlines():
            title, author, status = n.split(",")
            if title == user_to_remove:
                None
                print("Book has been removed from the list.")
            else:
                temp_list.append(f'{title},{author},{status.strip()}\n')
    with open(Books_list, "w") as books_databaselist:
        for n in temp_list:
            books_databaselist.writelines(n)
