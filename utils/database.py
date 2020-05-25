books = []

def book_add(user_nb_title, user_nb_author, user_nb_read):
    books.append({"Title": user_nb_title, "Author": user_nb_author, "Read": user_nb_read})

def book_read(user_rb_title):
        for n in books:
            if n["Title"] == user_rb_title:
                if n["Read"] == False:
                    n["Read"] = True
                    print(f"{user_rb_title} has be set as read")
                elif n["Read"] == True:
                    print(f"{user_rb_title} is already read")

def books_list():
    for n in books:
        if n["Read"] == True:
            check = "Book is finished."
        elif n["Read"] == False:
            check = "Book is not finished."
        else:
            return ''
        print(f"{n['Title']} by {n['Author']}. {check}")
    else:
        return ''

def book_delete(user_to_remove):
        for n in books:
            if n["Title"] == user_to_remove:
                books.remove(n)

