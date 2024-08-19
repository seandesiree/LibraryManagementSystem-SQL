from DB import conn


class Library:
    def add_book(self, id, title, author_id, isbn, publication_date, availability):
        try:
            cursor = conn.cursor()
            query = "INSERT INTO books (id, title, author_id, isbn, publication_date, availability) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (id, title, author_id, isbn, publication_date, availability))
            conn.commit()
            print("New book has been added successfully.")
        except Exception as e:
            print(f"Error {e}")
        finally:
            cursor.close()
        

    def borrow_book(self, user_id, book_id, borrow_date, return_date):
        if conn is not None:
            try:
                cursor = conn.cursor()
                query = "INSERT INTO borrowed_books (user_id, book_id, borrow_date, return_date) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (user_id, book_id, borrow_date, return_date))
                conn.commit()
                print("The book has been borrowed successfully.")
            finally:
                cursor.close()
                conn.close()
        else:
            print("Error in connecting to the database. ")

    def return_book(self, book_id):
        if conn is not None:
            try:
                cursor = conn.cursor()
                query = "DELETE FROM borrowed_books WHERE book_id = %s"
                cursor.execute(query, (book_id,))
                conn.commit()
                print("The book has been borrowed successfully.")
            finally:
                cursor.close()
                conn.close()
        else:
            print("Error in connecting to the database. ")


    def search_book(self, title):
        if conn is not None:
            try:
                cursor=conn.cursor()
                query= 'SELECT * FROM books WHERE title = %s'
                cursor.execute(query, (title, ))
                book = cursor.fetchone()
                if book:
                    print(book)
                else: 
                    print('Book does not exist.')           
            except Exception as e:
                print(f'Error: {e}')
            finally:
                conn.close()
                cursor.close()
        else:
            print("Error in connecting to the database. ")


 



    
