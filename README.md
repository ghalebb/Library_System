
# Library Management System

The Library Management System is a command-line application that allows users to manage a library of books. It supports operations such as adding, removing, modifying, displaying, and filtering books stored in a JSON file. This application is designed to demonstrate the use of Python and command-line interface programming for managing data.

## Features

- Add new books to the library.
- Remove existing books.
- Modify details of existing books.
- Display all books in the library.
- Filter books by author or genre.
- Persistent storage of library data in a JSON file.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need Python installed on your system. The application is tested with Python 3.8 and above.

### Cloning the Repository

To clone the repository, run the following command in your terminal:

```bash
git clone https://github.com/ghalebb/Library_System.git
```
then
```bash
cd Library_System
```

### Setting Up a Virtual Environment

To create a virtual environment, run the following commands in the root directory of the project:

```bash
python -m venv .venv
```

This command creates a new directory `venv` where the virtual environment files are stored.

#### Activating the Virtual Environment

- On Windows, run:
  ```bash
  .\.venv\Scripts\activate
  ```

- On macOS and Linux, run:
  ```bash
  source .venv/bin/activate
  ```

### Installing Dependencies

Once the virtual environment is activated, install the required dependencies by running:

```bash
pip install -r requirements.txt
```

### Running the Application

To run the application, use the following command:

```bash
python main.py
```

This will start the command-line interface. Here are some specific commands you can use to interact with the application:

### Adding a Book
To add a book, provide the title, author, publication year, and genre as follows:

```bash
python main.py add "To Kill a Mockingbird" "Harper Lee" 1960 "Fiction"
```

### Removing a Book
To remove a book, provide the title of the book you want to remove:

```bash
python main.py remove "To Kill a Mockingbird"
```

### Modifying a Book
To modify an attribute of a book, specify the title, the attribute you want to change, and the new value:

```bash
python main.py modify "To Kill a Mockingbird" title "To Kill a Mockingbird Updated"
```

### Displaying All Books
To display all books in the library:

```bash
python main.py display
```

### Filtering Books
To filter books by a specific attribute such as genre or author:

```bash
python main.py filter genre "Fiction"
```

### Finding a Book
To find a book by title:

```bash
python main.py find "To Kill a Mockingbird"
```


## Contributing

Contributions are welcome. Please feel free to fork the repository and submit pull requests.

