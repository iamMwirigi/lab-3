import mysql.connector
from mysql.connector import Error

def delete_book(book_id):
    """Delete a movie from the movies table by ID."""
    
    query = "DELETE FROM movie WHERE id = %s"
    data = (book_id, )

    try:
        # Connect to the database
        with mysql.connector.connect(
            host="localhost",
            database="movies",
            user="root",
            password=" " # Add your password
        ) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, data)

                # Get the number of affected rows
                affected_rows = cursor.rowcount

            # Commit the changes
            conn.commit()
            return affected_rows  # Return the number of affected rows

    except Error as error:
        print(f"Database error: {error}")
        return None  # Return None if an error occurs

if __name__ == '__main__':
    affected_rows = delete_book(2)
    if affected_rows is not None:
        print(f'Number of affected rows: {affected_rows}')
    else:
        print('Failed to delete the book.')
