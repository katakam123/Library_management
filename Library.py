FILE_NAME = "library.txt"
# -------------------------------
# Function to add a book
# -------------------------------
def add_book():
    print("\n--- Add Book ---")

    book_id = input("Enter Book ID: ").strip()
    title = input("Enter Book Title: ").strip()
    author = input("Enter Author Name: ").strip()

    if book_id == "" or title == "" or author == "":
        print("Error: All fields are required.")
        return

    # Check whether Book ID already exists
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split("|")

                if data[0] == book_id:
                    print("Error: Book ID already exists.")
                    return
    except FileNotFoundError:
        pass

    # Add book to file
    with open(FILE_NAME, "a") as file:
        file.write(f"{book_id}|{title}|{author}|Available\n")

    print("Book added successfully!")

# -------------------------------
# Function to view all books
# -------------------------------
def view_books():
    print("\n--- All Books ---")

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

            if not lines:
                print("No books found.")
                return

            print("-" * 75)
            print(f"{'ID':<10}{'Title':<25}{'Author':<20}{'Status':<15}")
            print("-" * 75)

            for line in lines:
                data = line.strip().split("|")

                if len(data) == 4:
                    print(f"{data[0]:<10}{data[1]:<25}{data[2]:<20}{data[3]:<15}")

            print("-" * 75)

    except FileNotFoundError:
        print("No library file found.")
        print("Please add a book first.")


# -------------------------------
# Function to search for a book
# -------------------------------
def search_book():
    print("\n--- Search Book ---")

    search = input("Enter Book ID or Title: ").strip().lower()

    if search == "":
        print("Error: Search value cannot be empty.")
        return

    found = False

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split("|")

                if len(data) == 4:
                    book_id, title, author, status = data

                    if search == book_id.lower() or search in title.lower():
                        print("\nBook Found")
                        print("Book ID :", book_id)
                        print("Title   :", title)
                        print("Author  :", author)
                        print("Status  :", status)
                        found = True

        if not found:
            print("Book not found.")

    except FileNotFoundError:
        print("No books available.")


# -------------------------------
# Function to issue a book
# -------------------------------
def issue_book():
    print("\n--- Issue Book ---")

    book_id = input("Enter Book ID to issue: ").strip()

    if book_id == "":
        print("Error: Book ID cannot be empty.")
        return

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        found = False
        updated_lines = []

        for line in lines:
            data = line.strip().split("|")

            if len(data) == 4 and data[0] == book_id:
                found = True

                if data[3] == "Issued":
                    print("Book is already issued.")
                    return

                data[3] = "Issued"

                updated_lines.append("|".join(data) + "\n")
            else:
                updated_lines.append(line)

        if not found:
            print("Book not found.")
            return

        with open(FILE_NAME, "w") as file:
            file.writelines(updated_lines)

        print("Book issued successfully!")

    except FileNotFoundError:
        print("No books available.")


# -------------------------------
# Function to return a book
# -------------------------------
def return_book():
    print("\n--- Return Book ---")

    book_id = input("Enter Book ID to return: ").strip()

    if book_id == "":
        print("Error: Book ID cannot be empty.")
        return

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        found = False
        updated_lines = []

        for line in lines:
            data = line.strip().split("|")

            if len(data) == 4 and data[0] == book_id:
                found = True

                if data[3] == "Available":
                    print("Book is already available.")
                    return

                data[3] = "Available"

                updated_lines.append("|".join(data) + "\n")
            else:
                updated_lines.append(line)

        if not found:
            print("Book not found.")
            return

        with open(FILE_NAME, "w") as file:
            file.writelines(updated_lines)

        print("Book returned successfully!")

    except FileNotFoundError:
        print("No books available.")


# -------------------------------
# Function to delete a book
# -------------------------------
def delete_book():
    print("\n--- Delete Book ---")

    book_id = input("Enter Book ID to delete: ").strip()

    if book_id == "":
        print("Error: Book ID cannot be empty.")
        return

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        found = False
        updated_lines = []

        for line in lines:
            data = line.strip().split("|")

            if len(data) == 4 and data[0] == book_id:
                found = True

                if data[3] == "Issued":
                    print("Cannot delete an issued book.")
                    return

                continue

            updated_lines.append(line)

        if not found:
            print("Book not found.")
            return

        with open(FILE_NAME, "w") as file:
            file.writelines(updated_lines)

        print("Book deleted successfully!")

    except FileNotFoundError:
        print("No books available.")


# -------------------------------
# Main Menu
# -------------------------------
def main():
    while True:
        print("\n===================================")
        print("     LIBRARY MANAGEMENT SYSTEM")
        print("===================================")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. Exit")
        print("===================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            search_book()

        elif choice == "4":
            issue_book()

        elif choice == "5":
            return_book()

        elif choice == "6":
            delete_book()

        elif choice == "7":
            print("Thank you for using Library Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()