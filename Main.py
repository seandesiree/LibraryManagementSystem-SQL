
import AuthorsDB, BooksDB, GenreDB, UserDB
from datetime import datetime

def book_operations():
    print("\nBook Operations:\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books")
    option = int(input("Please pick an option to continue: "))
    if option == 1:
        title = input('What is the title of the book being added? ').title()
        author = input('Enter auhtors name ').title()
        biography= input('Enter a biography for this author: ')
        author_id = AuthorsDB.add_authors(author, biography) 
        genre = input('Enter the genre name: ').title()
        description= input('Enter a description of the genre: ')
        genre_id = GenreDB.add_genre(genre, description)
        isbn=int(input('Please insert the book ISBN: '))       
        publication_date = input('Please enter the publication date in format (YYYY-MM-DD): ')
        BooksDB.add_book(title, author_id, genre_id, isbn, publication_date)
    elif option == 2:
        user= input('Please enter library_id: ')
        book= input('Please enter the book title you would like to borrow: ').title()
        borrowed_date = datetime.today().strftime('%Y-%m-%d')
        BooksDB.borrowed_books(user, book, borrowed_date)   
    elif option == 3:
        library_id= input('Please enter your library_id: ')
        book= input('Please enter the title of the book you are returning: ').title()
        return_date= datetime.today().strftime('%Y-%m-%d')
        BooksDB.return_book(library_id, book, return_date)
    elif option == 4:
        book= input('Please enter the title of the book you are searching for: ').title()
        BooksDB.search_book(book)
    elif option == 5:
        BooksDB.display_books()
    else:
            raise ValueError("Invalid option. (1-5)")         

def author_operations():
    try:
        print("\nAuthor Operations\n1. Add a new author\n2. View author details\n3. Display all authors\n")
        option = int(input("Please pick an option to continue: "))
        if option == 1:
            name = input('What is the name of the author?').title()
            bio= input("Please provide a biography of the author.")
            AuthorsDB.add_authors(name, bio)
        elif option == 2:
            name= input("Which author are you looking for? ").title()
            AuthorsDB.search_author(name)
        elif option == 3:
            AuthorsDB.display_authors()
        else:
            raise ValueError("Invalid option. (1-3)") 

    except Exception as e:
        print(f'Error: {e}')


def user_operations():
    try:
        print("\nUser Operations\n1. Add a new user\n2. View user details\n3. Display all users\n")
        option = int(input("Please pick an option to continue: "))
        if option == 1:
            name = input('Please enter users name: ').title()
            library_id= input('Please enter new library id: ')
            UserDB.add_user(name, library_id)
        elif option == 2:
            library_id = input('Please enter library id: ')
            UserDB.search_user(library_id)
        elif option == 3:
            UserDB.display_users()
        else:
            raise ValueError("Invalid option. (1-3)")
    except Exception as e:
        print(f'Error: {e}')
    



def genre_operations():
      try:
        print("\nGenre Operations\n1. Add a new genre\n2. View genre details\n3. Display all genres\n")
        option = int(input("Please pick an option to continue: "))
        if option == 1:
            name= input('Please enter the Genre name: ').title()
            description= input('Please enter a description of this genre: ')
            GenreDB.add_genre(name, description)
        elif option == 2:
            name= input('Which genre are you looking for? ').title()
            GenreDB.search_genre(name)
        elif option == 3:
            GenreDB.display_genres()
        else:
            raise ValueError("Invalid option. (1-3)")
      except Exception as e:
          print(f'Error: {e}')
