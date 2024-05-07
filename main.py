import argparse
import utils
from library import Library
from tabulate import tabulate


class LibraryApp:
    """
    A command-line application for managing a library of books.

    This application supports adding, removing, modifying, displaying,
    and filtering books stored in a JSON file.
    """

    def __init__(self):
        """
        Initializes the LibraryApp by loading the books from a JSON file.
        """
        self.library = Library()
        self.library.load_from_file('library.json')

    def run(self):
        """
        Runs the command-line interface for the LibraryApp.
        :return:
        """
        parser = argparse.ArgumentParser(
            description="Library Management System")
        subparsers = parser.add_subparsers(dest='command')

        # Add book command
        add_parser = subparsers.add_parser('add', help='Add a new book')
        add_parser.add_argument('title', type=str, help='Title of the book')
        add_parser.add_argument('author', type=str, help='Author of the book')
        add_parser.add_argument('publication_year', type=int,
                                help='Publication year of the book')
        add_parser.add_argument('genre', type=str, help='Genre of the book')

        # Remove book command
        remove_parser = subparsers.add_parser('remove', help='Remove a book')
        remove_parser.add_argument('title', type=str,
                                   help='Title of the book to remove')

        # Modify book command
        modify_parser = subparsers.add_parser('modify', help='Modify a book')
        modify_parser.add_argument('title', type=str,
                                   help='Title of the book to modify')
        modify_parser.add_argument('modification', choices=['title', 'author',
                                                            'publication_year',
                                                            'genre'],
                                   help='Field to modify')
        modify_parser.add_argument('value', type=str,
                                   help='New value for the field')

        # Display books command
        subparsers.add_parser('display',
                              help='Display all books')

        # Save library command
        subparsers.add_parser('save',
                              help='Save library to file')

        # Filter books command
        filter_parser = subparsers.add_parser('filter',
                                              help='Filter books by genre or '
                                                   'author')
        filter_parser.add_argument('filter_type', choices=['genre', 'author'],
                                   help='Filter by genre or author')
        filter_parser.add_argument('value', type=str,
                                   help='Value to filter by')

        # Find book command
        find_parser = subparsers.add_parser('find', help='Find a book')
        find_parser.add_argument('title', type=str,
                                 help='Title of the book to find')

        args = parser.parse_args()
        if args.command:
            command_function = getattr(self, args.command)
            arg_dict = vars(args)
            arg_dict.pop('command')  # Remove 'command' key from the arguments
            command_function(**arg_dict)
        else:
            parser.print_help()

    def add(self, title, author, publication_year, genre):
        """
        Adds a new book to the library.

        Args:
            title (str): Title of the book.
            author (str): Author of the book.
            publication_year (int): Year the book was published.
            genre (str): Genre of the book.
        """
        self.library.add_book(title, author, publication_year, genre)
        self.library.save_to_file('library.json')

    def remove(self, title):
        """
        Removes a book from the library.

        Args:
            title (str): Title of the book to remove.
        """
        print(self.library.remove_book(title))
        self.library.save_to_file('library.json')

    def display(self):
        """
        Displays all books in the library.
        """
        self.display_books()

    def modify(self, title, modification, value):
        """
        Modifies an attribute of a book.

        Args:
            title (str): Title of the book to modify.
            modification (str): Attribute of the book to modify.
            value (str): New value for the attribute.
        """
        self.library.modify_book(title, modification, value)
        self.library.save_to_file('library.json')

    def save(self):
        """
        Saves the current state of the library to the JSON file.
        """
        self.library.save_to_file('library.json')
        print("Library saved.")

    def filter(self, filter_type, value):
        """
        Filters books by specified attribute.

        Args:
            filter_type (str): Attribute to filter by ('genre' or 'author').
            value (str): Value of the attribute to filter by.
        """
        books = self.library.filter_books(filter_type, value)
        if books is not None:
            self.display_books(books)

    def find(self, title):
        """
        Finds a book by title.

        Args:
            title (str): Title of the book to find.
        """
        print(self.library.find_book(title))

    def display_books(self, books_to_display=None):
        """
        Displays books in a formatted table.

        Args: books_to_display (list, optional): A list of books to display.
        Defaults to displaying all books.
        """
        books = self.library.display_books(books_to_display)
        if len(books) == 0:
            print("No Books to Display")
            return
        book_table = [
            [utils.bold_text(book.title), book.author, book.publication_year,
             book.genre] for
            book in books]
        headers = ["Title", "Author", "Publication Year", "Genre"]
        print(tabulate(book_table, headers, tablefmt="grid"))


if __name__ == '__main__':
    app = LibraryApp()
    app.run()
