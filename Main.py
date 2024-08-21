
from datetime import datetime
from AuthorsDB import Author
from BooksDB import Library
from GenreDB import Genre
from UserDB import User



def book_operations():
    author_OBJ = Author()
    # genre_OBJ = Genre()
    books_OBJ = Library()

    print("\nBook Operations:\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books")
    option = int(input("Please pick an option to continue: "))
    if option == 1:
        title = input('What is the title of the book being added? ').title()
        author = input('Enter auhtors name ').title()
        biography= input('Enter a biography for this author: ')
        author_id = author_OBJ.add_authors(author, biography) 
        isbn=int(input('Please insert the book ISBN: '))       
        publication_date = input('Please enter the publication date in format (YYYY-MM-DD): ')
        books_OBJ.add_book(title, author_id, isbn, publication_date, True)
    elif option == 2:
        user= input('Please enter user_id: ')
        book= input('Please enter the book id you would like to borrow: ').title()
        borrowed_date = datetime.today().strftime('%Y-%m-%d')
        return_date = input("Please enter the return date in format (YYYY-MM-DD): ")
        books_OBJ.borrow_book(user, book, borrowed_date, return_date)   
    elif option == 3:
        library_id= input('Please enter your library_id: ')
        book= input('Please enter the title of the book you are returning: ').title()
        return_date= datetime.today().strftime('%Y-%m-%d')
        books_OBJ.return_book(library_id, book, return_date)
    elif option == 4:
        book= input('Please enter the title of the book you are searching for: ').title()
        books_OBJ.search_book(book)
    elif option == 5:
        books_OBJ.display_books()
    else:
            raise ValueError("Invalid option. (1-5)")         

def author_operations():
    author_OBJ = Author()
    try:
        print("\nAuthor Operations\n1. Add a new author\n2. View author details\n3. Display all authors\n")
        option = int(input("Please pick an option to continue: "))
        if option == 1:
            name = input('What is the name of the author?').title()
            bio= input("Please provide a biography of the author.")
            author_OBJ.add_authors(name, bio)
        elif option == 2:
            author_id = input("What is the author id? ").title()
            author_OBJ.view_author_details(author_id)
        elif option == 3:
            author_OBJ.display_authors()
        else:
            raise ValueError("Invalid option. (1-3)") 

    except Exception as e:
        print(f'Error: {e}')


def user_operations():
    user_OBJ = User()
    try:
        print("\nUser Operations\n1. Add a new user\n2. View user details\n3. Display all users\n")
        option = int(input("Please pick an option to continue: "))
        if option == 1:
            name = input('Please enter users name: ').title()
            library_id= input('Please enter new library id: ')
            user_OBJ.add_user(name, library_id)
        elif option == 2:
            library_id = input('Please enter library id: ')
            user_OBJ.search_user(library_id)
        elif option == 3:
            user_OBJ.display_users()
        else:
            raise ValueError("Invalid option. (1-3)")
    except Exception as e:
        print(f'Error: {e}')
    



# def genre_operations():
#       genre_OBJ = Genre()
#       try:
#         print("\nGenre Operations\n1. Add a new genre\n2. View genre details\n3. Display all genres\n")
#         option = int(input("Please pick an option to continue: "))
#         if option == 1:
#             name= input('Please enter the Genre name: ').title()
#             description= input('Please enter a description of this genre: ')
#             genre_OBJ.add_genre(name, description)
#         elif option == 2:
#             name= input('Which genre are you looking for? ').title()
#             genre_OBJ.search_genre(name)
#         elif option == 3:
#             genre_OBJ.display_genres()
#         else:
#             raise ValueError("Invalid option. (1-3)")
#       except Exception as e:
#           print(f'Error: {e}')
