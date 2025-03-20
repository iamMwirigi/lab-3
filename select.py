import mysql.connector

def query_table():
    """Fetches and displays all records from the movies table."""
    try:
        # Connect to MySQL Server
        conn = mysql.connector.connect(
            host="localhost",
            database="movies",
            user="root",
            password=" " # Add Password
        )
        cursor = conn.cursor()

        # Execute the SELECT query
        cursor.execute("SELECT * FROM movie")

        # Fetch all rows
        records = cursor.fetchall()

        # Print the records
        print("movies in the database:")
        for row in records:
            print(row)

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    query_table()
