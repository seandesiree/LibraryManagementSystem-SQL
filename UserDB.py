from DB import conn


class User:
    def add_user(self, name, library_id):
        try:
            cursor = conn.cursor()
            query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
            cursor.execute(query, (name, library_id))
            conn.commit()
            print("New user has been added successfully.")
        except Exception as e:
            print(f"Error {e}")
        finally:
            cursor.close()


    def display_users(self, user):   
        if conn is not None:
            try:
                cursor=conn.cursor()
                query = 'SELECT * FROM users'
                cursor.execute(query, (user))
                for row in cursor.fetchall():
                    print(row)
            except Exception as e:
                print(f'Error: {e}')
            finally:
                conn.close()
                cursor.close()
        else:
            print("Error in connecting to the database. ")