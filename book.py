import utils


class Book:
    """
    A class representing a book with properties for title, author,
    publication year, and genre.

    Attributes:
        title (str): The title of the book, automatically capitalized.
        author (str): The author of the book.
        publication_year (int): The year the book was published.
        genre (str): The genre of the book.
    """

    def __init__(self, title, author, publication_year, genre):

        """
        Initializes a new instance of the Book class.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            publication_year (int): The year the book was published.
            genre (str): The genre of the book.
        """
        self.title = title.title()
        self.author = author
        self.publication_year = publication_year
        self.genre = genre

    def __str__(self):
        """
                String representation of the Book instance.

                Returns:
                    str: The title of the book in bold, followed by the author
                    , publication year, and genre.
                """
        return (
            f"{utils.bold_text(self.title)} by {self.author}, "
            f"{self.publication_year}, {self.genre}")

    def modify_book(self, modification, value):
        """
        Modifies an attribute of the book.

        Args:
            modification (str): The attribute of the book to modify
            ('title', 'author', 'publication_year', 'genre').
            value (str): The new value for the attribute.

        Returns:
            None: Prints out a success message or an error if the modification
            is not allowed.
        """
        if modification not in {"title", "author", "publication_year",
                                "genre"}:
            print('Modify book error')

        if modification == 'title':
            self.title = value
        elif modification == 'author':
            self.author = value
        elif modification == 'publication_year':
            self.publication_year = value
        elif modification == 'genre':
            self.genre = value
        print('Modified book successfully')
        print(self)
