# Updated Library Collection
# ==============================================================================================================
# 1. Title: Dracula                   | Author: Bram Stoker               | ISBN: 9780486411095   | Year: 1897   | Genre: Horror             | Status: Available
# 2. Title: Dune                      | Author: Frank Herbert             | ISBN: 9780441172719   | Year: 1965   | Genre: Science Fiction    | Status: Available
# 3. Title: Frankenstein              | Author: Mary Shelley              | ISBN: 9780486282114   | Year: 1818   | Genre: Gothic             | Status: Available
# 4. Title: Of Mice and Men           | Author: John Steinbeck            | ISBN: 9780140177398   | Year: 1937   | Genre: Classic            | Status: Available
# 5. Title: The Grapes of Wrath       | Author: John Steinbeck            | ISBN: 9780143039433   | Year: 1939   | Genre: Historical Fiction | Status: Available
# 6. Title: The Great Gatsby          | Author: F. Scott Fitzgerald       | ISBN: 9780743273565   | Year: 1925   | Genre: Classic            | Status: Available
# PS C:\Users\GregoryCTRMartinez\AppData\Local\Programs\Microsoft VS Code> ^C
# PS C:\Users\GregoryCTRMartinez\AppData\Local\Programs\Microsoft VS Code> & C:\Users\GregoryCTRMartinez\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/GregoryCTRMartinez/OneDrive - Knowledge Management, Inc/Tools/Scripts/Powershell/Gregory_Library_Book_System.py"
# Library Book Management System
# ==============================================================================================================

# Your Library Collection - Alphabetical Order
# ==============================================================================================================
# 1. Title: Dracula                   | Author: Bram Stoker               | ISBN: 9780486411095   | Year: 1897   | Genre: Horror             | Status: Available
# 2. Title: Dune                      | Author: Frank Herbert             | ISBN: 9780441172719   | Year: 1965   | Genre: Science Fiction    | Status: Available
# 3. Title: Frankenstein              | Author: Mary Shelley              | ISBN: 9780486282114   | Year: 1818   | Genre: Gothic             | Status: Available
# 4. Title: Of Mice and Men           | Author: John Steinbeck            | ISBN: 9780140177398   | Year: 1937   | Genre: Classic            | Status: Available
# 5. Title: The Grapes of Wrath       | Author: John Steinbeck            | ISBN: 9780143039433   | Year: 1939   | Genre: Historical Fiction | Status: Available
# 6. Title: The Great Gatsby          | Author: F. Scott Fitzgerald       | ISBN: 9780743273565   | Year: 1925   | Genre: Classic            | Status: Available

# Library Options
# 1. Check out a book
# 2. Return a book
# 3. Add a new book
# Enter your choice (1, 2, or 3): 3

# Add a New Book
# -------------------------
# Enter the book title: Ender's Game
# Enter the author: Orson Scott Card
# Enter the ISBN: 978-1250773012
# Enter the publication year: 1985
# Enter the genre: Science Fiction

# "Ender's Game" has been added to the library.

# New book saved to library_books.csv.

# Updated Library Collection
# ==============================================================================================================
# 1. Title: Dracula                   | Author: Bram Stoker               | ISBN: 9780486411095   | Year: 1897   | Genre: Horror             | Status: Available
# 2. Title: Dune                      | Author: Frank Herbert             | ISBN: 9780441172719   | Year: 1965   | Genre: Science Fiction    | Status: Available
# 3. Title: Ender's Game              | Author: Orson Scott Card          | ISBN: 978-1250773012  | Year: 1985   | Genre: Science Fiction    | Status: Available
# 4. Title: Frankenstein              | Author: Mary Shelley              | ISBN: 9780486282114   | Year: 1818   | Genre: Gothic             | Status: Available
# 5. Title: Of Mice and Men           | Author: John Steinbeck            | ISBN: 9780140177398   | Year: 1937   | Genre: Classic            | Status: Available
# 6. Title: The Grapes of Wrath       | Author: John Steinbeck            | ISBN: 9780143039433   | Year: 1939   | Genre: Historical Fiction | Status: Available
# 7. Title: The Great Gatsby          | Author: F. Scott Fitzgerald       | ISBN: 9780743273565   | Year: 1925   | Genre: Classic            | Status: Available

# Check out procedure test
# Library Options
# 1. Check out a book
# 2. Return a book
# 3. Add a new book
# Enter your choice (1, 2, or 3): 1

# Available Books
# -------------------------
# 1. Dracula
# 2. Dune
# 3. Ender's Game
# 4. Frankenstein
# 5. Of Mice and Men
# 6. The Grapes of Wrath
# 7. The Great Gatsby

# Enter the number of the book you want to check out: 7
# Enter your name: Martinez Gregory
# "The Great Gatsby" has been checked out to Martinez Gregory.

# Book status saved to library_books.csv.
# PS C:\Users\GregoryCTRMartinez\AppData\Local\Programs\Microsoft VS Code> & C:\Users\GregoryCTRMartinez\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/GregoryCTRMartinez/OneDrive - Knowledge Management, Inc/Tools/Scripts/Powershell/Gregory_Library_Book_System.py"
# Library Book Management System
# ==============================================================================================================

# Your Library Collection - Alphabetical Order
# ==============================================================================================================
# 1. Title: Dracula                   | Author: Bram Stoker               | ISBN: 9780486411095   | Year: 1897   | Genre: Horror             | Status: Available
# 2. Title: Dune                      | Author: Frank Herbert             | ISBN: 9780441172719   | Year: 1965   | Genre: Science Fiction    | Status: Available
# 3. Title: Ender's Game              | Author: Orson Scott Card          | ISBN: 978-1250773012  | Year: 1985   | Genre: Science Fiction    | Status: Available
# 4. Title: Frankenstein              | Author: Mary Shelley              | ISBN: 9780486282114   | Year: 1818   | Genre: Gothic             | Status: Available
# 5. Title: Of Mice and Men           | Author: John Steinbeck            | ISBN: 9780140177398   | Year: 1937   | Genre: Classic            | Status: Available
# 6. Title: The Grapes of Wrath       | Author: John Steinbeck            | ISBN: 9780143039433   | Year: 1939   | Genre: Historical Fiction | Status: Available
# 7. Title: The Great Gatsby          | Author: F. Scott Fitzgerald       | ISBN: 9780743273565   | Year: 1925   | Genre: Classic            | Status: Checked Out to Martinez Gregory

# Checkout checked out book test
# Available Books
# -------------------------
# 1. Dracula
# 2. Dune
# 3. Ender's Game
# 4. Frankenstein
# 5. Of Mice and Men
# 6. The Grapes of Wrath

# Enter the number of the book you want to check out: 7
# "The Great Gatsby" is already checked out to Martinez Gregory.

# This is my Python library code. I attempted the basic level coding assignment.
import csv

# This section defines the book class which includes the title, author, isbn, year and genre
class Book:
    def __init__(self, title, author, isbn, year, genre,
                 status="Available", patron_name=""):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.genre = genre
        self.checked_out = status == "Checked Out"
        self.patron_name = patron_name

# Defines the checkout procedure and creates the patron_name that allows the program to associate user actions with the books in the library
    def check_out(self, patron_name):
        if not self.checked_out:
            self.checked_out = True
            self.patron_name = patron_name
            print(f'"{self.title}" has been checked out to {patron_name}.')
        else:
            print(
                f'"{self.title}" is already checked out '
                f'to {self.patron_name}.'
            )

# Return book function
    def return_book(self):
        if self.checked_out:
            print(
                f'"{self.title}" has been returned '
                f'by {self.patron_name}.'
            )
            self.checked_out = False
            self.patron_name = ""
        else:
            print(f'"{self.title}" was not checked out.')

# Reports book availability status
    def report_status(self):
        if self.checked_out:
            status = f"Checked Out to {self.patron_name}"
        else:
            status = "Available"

        print("\nBook Information")
        print("-------------------------")
        print(f"Title:       {self.title}")
        print(f"Author:      {self.author}")
        print(f"ISBN:        {self.isbn}")
        print(f"Year:        {self.year}")
        print(f"Genre:       {self.genre}")
        print(f"Status:      {status}")

    def __str__(self):
        status = (
            f"Checked Out to {self.patron_name}"
            if self.checked_out
            else "Available"
        )

        return (
            f"Title: {self.title:<25} | "
            f"Author: {self.author:<25} | "
            f"ISBN: {self.isbn:<15} | "
            f"Year: {self.year:<6} | "
            f"Genre: {self.genre:<18} | "
            f"Status: {status}"
        )


# -------------------------------------------------
# File path of book library file
# -------------------------------------------------

filename = r"C:\Users\GregoryCTRMartinez\OneDrive - Knowledge Management, Inc\Tools\Scripts\Powershell\library_books.csv"


# -------------------------------------------------
# Load books from CSV
# -------------------------------------------------

def load_books(filename):
    books = []

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            book = Book(
                row["title"],
                row["author"],
                row["isbn"],
                int(row["year"]),
                row["genre"],
                row["status"],
                row["patron_name"]
            )

            books.append(book)

    return books


# -------------------------------------------------
# Save books to CSV
# -------------------------------------------------

def save_books(filename, books):
    with open(filename, "w", newline="", encoding="utf-8") as file:

        fieldnames = [
            "title",
            "author",
            "isbn",
            "year",
            "genre",
            "status",
            "patron_name"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for book in books:

            if book.checked_out:
                status = "Checked Out"
                patron_name = book.patron_name
            else:
                status = "Available"
                patron_name = ""

            writer.writerow({
                "title": book.title,
                "author": book.author,
                "isbn": book.isbn,
                "year": book.year,
                "genre": book.genre,
                "status": status,
                "patron_name": patron_name
            })


# -------------------------------------------------
# Sort books alphabetically by title
# -------------------------------------------------

def sort_books(books):
    return sorted(books, key=lambda book: book.title.lower())


# -------------------------------------------------
# Add a new book
# -------------------------------------------------

def add_book(books):
    print("\nAdd a New Book")
    print("-------------------------")

    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    isbn = input("Enter the ISBN: ")

    while True:
        try:
            year = int(input("Enter the publication year: "))
            break
        except ValueError:
            print("Please enter a valid year.")

    genre = input("Enter the genre: ")

    new_book = Book(
        title,
        author,
        isbn,
        year,
        genre
    )

    books.append(new_book)

    print(f'\n"{title}" has been added to the library.')

    return new_book


# -------------------------------------------------
# Main program
# -------------------------------------------------

print("Library Book Management System")
print("=" * 110)

# Load books from CSV
books = load_books(filename)


# -------------------------------------------------
# Display current collection
# -------------------------------------------------

print("\nYour Library Collection - Alphabetical Order")
print("=" * 110)

sorted_books = sort_books(books)

for number, book in enumerate(sorted_books, start=1):
    print(f"{number}. {book}")


# -------------------------------------------------
# Patron menu
# -------------------------------------------------

print("\nLibrary Options")
print("1. Check out a book")
print("2. Return a book")
print("3. Add a new book")

choice = input("Enter your choice (1, 2, or 3): ")


# -------------------------------------------------
# Check out a book
# -------------------------------------------------

if choice == "1":

    print("\nAvailable Books")
    print("-------------------------")

    sorted_books = sort_books(books)

    for number, book in enumerate(sorted_books, start=1):
        if not book.checked_out:
            print(f"{number}. {book.title}")

    book_choice = int(
        input("\nEnter the number of the book you want to check out: ")
    )

    if 1 <= book_choice <= len(sorted_books):

        selected_book = sorted_books[book_choice - 1]

        if not selected_book.checked_out:

            patron_name = input("Enter your name: ")

            selected_book.check_out(patron_name)

            save_books(filename, books)

            print("\nBook status saved to library_books.csv.")

        else:

            print(
                f'"{selected_book.title}" is already checked out '
                f'to {selected_book.patron_name}.'
            )

    else:
        print("Invalid book selection.")


# -------------------------------------------------
# Return a book
# -------------------------------------------------

elif choice == "2":

    print("\nChecked Out Books")
    print("-------------------------")

    sorted_books = sort_books(books)

    found_book = False

    for number, book in enumerate(sorted_books, start=1):

        if book.checked_out:
            print(
                f"{number}. {book.title} - "
                f"{book.patron_name}"
            )

            found_book = True

    if found_book:

        book_choice = int(
            input("\nEnter the number of the book you want to return: ")
        )

        if 1 <= book_choice <= len(sorted_books):

            selected_book = sorted_books[book_choice - 1]

            if selected_book.checked_out:

                selected_book.return_book()

                save_books(filename, books)

                print("\nBook status saved to library_books.csv.")

            else:

                print(
                    f'"{selected_book.title}" '
                    f"is not currently checked out."
                )

        else:
            print("Invalid book selection.")

    else:
        print("There are currently no checked-out books.")


# -------------------------------------------------
# Add a new book
# -------------------------------------------------

elif choice == "3":

    new_book = add_book(books)

    # Save the new book to the CSV file
    save_books(filename, books)

    print("\nNew book saved to library_books.csv.")

    print("\nUpdated Library Collection")
    print("=" * 110)

    sorted_books = sort_books(books)

    for number, book in enumerate(sorted_books, start=1):
        print(f"{number}. {book}")


else:
    print("Invalid choice. Please select 1, 2, or 3.")