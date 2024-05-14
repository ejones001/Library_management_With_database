# Input Validation Functions
import re


def validate_isbn(isbn):
    return bool(re.match(r'^\d{3}-\d{10}$', isbn))

def validate_date(date_str):
    return bool(re.match(r'^\d{4}-\d{2}-\d{2}$', date_str))

# Menu Display Functions
def display_main_menu():
    print("Main Menu:")
    print("1. Book Operations")
    print("2. User Operations")
    print("3. Author Operations")
    print("4. Genre Operations")
    print("5. Quit")

def display_book_menu():
    print("Book Operations:")
    print("1. Add a new book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")
    print("6. Back to Main Menu")

def display_user_menu():
    print("User Operations:")
    print("1. Add a new user")
    print("2. View user details")
    print("3. Display all users")
    print("4. Back to Main Menu")

def display_author_menu():
    print("Author Operations:")
    print("1. Add a new author")
    print("2. View author details")
    print("3. Display all authors")
    print("4. Back to Main Menu")

def display_genre_menu():
    print("Genre Operations:")
    print("1. Add a new genre")
    print("2. View genre details")
    print("3. Display all genres")
    print("4. Back to Main Menu")

# Input Handling Functions
def main_menu_input():
    choice = input("Enter your choice: ")
    return choice

def book_menu_input():
    choice = input("Enter your choice: ")
    return choice

def user_menu_input():
    choice = input("Enter your choice: ")
    return choice

def author_menu_input():
    choice = input("Enter your choice: ")
    return choice

def genre_menu_input():
    choice = input("Enter your choice: ")
    return choice





# Utility Function
def format_date(date):
    return date.strftime('%Y-%m-%d')
