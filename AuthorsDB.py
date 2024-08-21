from DB import conn


class Author:
    def display_authors(self):   
            if conn is not None:
                try:
                    cursor=conn.cursor()
                    query = 'SELECT * FROM authors'
                    cursor.execute(query)
                    for row in cursor.fetchall():
                        print(row)
                except Exception as e:
                    print(f'Error: {e}')
                finally:
                    conn.close()
                    cursor.close()
            else:
                print("Error in connecting to the database. ")
            

    def view_author_details(self, id):   
            if conn is not None:
                try:
                    cursor=conn.cursor()
                    query = 'SELECT * FROM authors WHERE id = %s'
                    cursor.execute(query, (id, ))
                    for row in cursor.fetchall():
                        print(row)
                except Exception as e:
                    print(f'Error: {e}')
                finally:
                    conn.close()
                    cursor.close()
            else:
                print("Error in connecting to the database. ")



    def add_authors(self, name, biography):
        try:
            cursor = conn.cursor()
            query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
            cursor.execute(query, (name, biography))
            conn.commit()
            print("New author has been added successfully.")
        except Exception as e:
            print(f"Error {e}")
        finally:
            cursor.close()


 