import databaseconnection as db
import User_interface as ui

def main():
    connection = db.connect_to_database()
    cursor = db.create_cursor(connection)

    while True:
        ui.display_main_menu()
        choice = ui.main_menu_input()

        if choice == '1':
            ui.display_book_menu()
            book_choice = ui.book_menu_input()
            if book_choice == '1':
                db.add_new_book(cursor)
            # Implement other book operations similarly
        elif choice == '2':
            ui.display_user_menu()
            user_choice = ui.user_menu_input()
            # Implement user operations based on user_choice
        elif choice == '3':
            ui.display_author_menu()
            author_choice = ui.author_menu_input()
            # Implement author operations based on author_choice
        elif choice == '4':
            ui.display_genre_menu()
            genre_choice = ui.genre_menu_input()
            # Implement genre operations based on genre_choice
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

    db.close_cursor(cursor)
    db.close_connection(connection)

if __name__ == "__main__":
    main()
