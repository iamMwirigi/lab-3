import mysql.connector
from mysql.connector import Error

def update_movie(movie_id, new_name):
    """Update the movie title in the movie table."""
    
    query = """ UPDATE movie
                SET title = %s
                WHERE id = %s """
    
    data = (new_name, movie_id)

    try:
        # Connect to the database
        with mysql.connector.connect(
            host="localhost",
            database="movies",
            user="root",
            password=" " #Add password
        ) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, data)

                # Get the number of affected rows
                affected_rows = cursor.rowcount

            # Commit the changes
            conn.commit()
            return affected_rows 

    except Error as error:
        print(f"Database error: {error}")
        return None  # Return None if an error occurs

if __name__ == '__main__':
    affected_rows = update_movie(2,'Terminator')
    if affected_rows is not None:
        print(f'Number of affected rows: {affected_rows}')
    else:
        print('Failed to update the movie.')
