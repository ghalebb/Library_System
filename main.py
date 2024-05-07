import argparse
import utils
from library import Library
from tabulate import tabulate


class LibraryApp:
    def __init__(self):
        self.library = Library()
        self.library.load_from_file('library.json')

    def run(self):
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
        self.library.add_book(title, author, publication_year, genre)
        self.library.save_to_file('library.json')

    def remove(self, title):
        print(self.library.remove_book(title))
        self.library.save_to_file('library.json')

    def display(self):
        self.display_books()

    def modify(self, title, modification, value):
        self.library.modify_book(title, modification, value)
        self.library.save_to_file('library.json')

    def save(self):
        self.library.save_to_file('library.json')
        print("Library saved.")

    def filter(self, filter_type, value):
        books = self.library.filter_books(filter_type, value)
        if books is not None:
            self.display_books(books)

    def find(self, title):
        print(self.library.find_book(title))

    def display_books(self, books_to_display=None):
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
