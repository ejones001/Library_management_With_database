import mysql.connector
import re



def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="root",
            user="localhost",
            password="That08er",
            database="mycodingtempledata"
        )
        print("Connected to the database!")
        return connection
    except mysql.connector.Error as err:
        print("Error:", err)

def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("Connection closed.")

def create_cursor(connection):
    try:
        cursor = connection.cursor()
        return cursor
    except mysql.connector.Error as err:
        print("Error:", err)

def close_cursor(cursor):
    cursor.close()

def add_new_book(cursor):
    title = input("Enter the title of the book: ")
    author_id = input("Enter the ID of the author: ")
    genre_id = input("Enter the ID of the genre: ")
    isbn = input("Enter the ISBN of the book (XXX-XXXXXXXXXX): ")
    while not validate_isbn(isbn):
        print("Invalid ISBN format. Please enter again.")
        isbn = input("Enter the ISBN of the book (XXX-XXXXXXXXXX): ")
    publication_date = input("Enter the publication date (YYYY-MM-DD): ")
    while not validate_date(publication_date):
        print("Invalid date format. Please enter again.")
        publication_date = input("Enter the publication date (YYYY-MM-DD): ")

    try:
        sql = "INSERT INTO books (title, author_id, genre_id, isbn, publication_date) VALUES (%s, %s, %s, %s, %s)"
        values = (title, author_id, genre_id, isbn, publication_date)
        cursor.execute(sql, values)
        print("Book added successfully!")
    except mysql.connector.Error as err:
        breakpoint

def validate_isbn(isbn):
    return bool(re.match(r'^\d{3}-\d{10}$', isbn))

def validate_date(date_str):
    return bool(re.match(r'^\d{4}-\d{2}-\d{2}$', date_str))
