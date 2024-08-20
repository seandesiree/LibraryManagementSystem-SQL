from DB import conn


class Genre:
    def add_genre(self, name, description):
        try:
            cursor = conn.cursor()
            query = "INSERT INTO genre (name, description) VALUES (%s, %s)"
            cursor.execute(query, (name, description))
            conn.commit()
            print("New genre has been added successfully.")
        except Exception as e:
            print(f"Error {e}")
        finally:
            cursor.close()


    def display_genres(self, genre):
        if conn is not None:
            try:
                cursor=conn.cursor()
                query = 'SELECT * FROM genres'
                cursor.execute(query, (genre))
                for row in cursor.fetchall():
                    print(row)
            except Exception as e:
                print(f'Error: {e}')
            finally:
                conn.close()
                cursor.close()
        else:
            print("Error in connecting to the database. ")