import json
from book import Book

BOOK_NOT_FOUND_MESSAGE = 'Book not found'


class Library:
    """
    A class representing a library, which manages a collection of books.

    Attributes:
        books (dict): A dictionary to store books with their titles as keys.
    """

    def __init__(self):
        """
        Initializes a new Library instance with an empty dictionary of books.
        """
        self.books = dict()

    def add_book(self, title, author, publication_year, genre):
        """
        Adds a new book to the library.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            publication_year (int): The year the book was published.
            genre (str): The genre of the book.

        Returns:
            str: A message indicating whether the book was added or already
            exists.
        """
        title = title.title()
        if title not in self.books:
            self.books[title] = Book(title, author,
                                     publication_year, genre)
            print(f'Book {title} added.')
        else:
            print(f'Book {title} already exists.')

    def remove_book(self, title):
        """
        Removes a book from the library.

        Args:
            title (str): The title of the book to remove.

        Returns:
            str: A message indicating whether the book was removed or not found.
        """
        title = title.title()
        if title in self.books:
            del self.books[title]
            return 'Book removed'
        else:
            return BOOK_NOT_FOUND_MESSAGE

    def find_book(self, title):
        """
        Finds a book in the library by title.

        Args:
            title (str): The title of the book to find.

        Returns:
            Book: The book object if found, else a not found message.
        """
        return self.books.get(title.title(), BOOK_NOT_FOUND_MESSAGE)

    def display_books(self, books_to_display=None):
        """
        Displays a list of books in the library.

        Args:
            books_to_display (list, optional): A list of books to display. Defaults to displaying all books.

        Returns:
            list: A list of books.
        """
        if books_to_display is None:
            books_to_display = self.books.values()
        if len(books_to_display) == 0:
            return []
        return books_to_display

    def filter_books(self, filter_by=None, value=None):
        """
        Filters books by a specified attribute and value.

        Args:
            filter_by (str): The attribute to filter by ('author' or 'genre').
            value (str): The value of the attribute to match.

        Returns:
            list: A list of books that match the filter criteria.
        """
        if filter_by and value:
            return [book for book in self.books.values() if
                    getattr(book, filter_by) == value]
        print('author or genre not found')
        return

    def modify_book(self, title, modification, value=None):
        """
        Modifies an attribute of a book in the library.

        Args:
            title (str): The title of the book to modify.
            modification (str): The attribute of the book to modify.
            value (str, optional): The new value for the attribute.
        """
        if modification == 'publication_year':
            try:
                value = int(value)
            except ValueError:
                print(
                    f"Error: '{value}' is not a valid integer for "
                    f"publication year.")
                return
        title = title.title()
        if title in self.books:
            self.books[title].modify_book(modification, value)
        else:
            print(BOOK_NOT_FOUND_MESSAGE)

    def save_to_file(self, file_path):
        """
        Saves the current list of books to a file.

        Args:
            file_path (str): The path to the file where the library will be saved.
        """
        with open(file_path, 'w') as file:
            json.dump([book.__dict__ for book in self.books.values()], file)

    def load_from_file(self, file_path):
        """
        Loads a list of books from a file.

        Args:
            file_path (str): The path to the file to load the books from.
        """
        try:
            with open(file_path, 'r') as file:
                # Attempt to load JSON data
                try:
                    data_file = json.load(file)
                except json.JSONDecodeError:
                    # Handle empty or invalid JSON
                    data_file = []

                # If data_file is not empty, initialize books dictionary
                if data_file:
                    self.books = {book_data['title'].title(): Book(**book_data)
                                  for
                                  book_data in data_file}
                else:
                    # If the data is empty, just initialize an empty dictionary
                    self.books = {}
                    print(
                        "Notice: Starting with an empty library.")
        except FileNotFoundError:
            # Handle the file not being found
            self.books = {}
            print(
                f"Notice: {file_path} not found. Starting with an empty "
                f"library.")
