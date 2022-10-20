import sqlite3
from src.repository.book_repo import BookRepository


class BookRepositoryDatabase(BookRepository):
    def __init__(self, books_text_file):
        super(BookRepositoryDatabase, self).__init__()
        self.__file_name = books_text_file
        self.__load_data()

    def __load_data(self):
        self.connection = sqlite3.connect(self.__file_name)
        self.cursor = self.connection.cursor()
        self.query = """
        CREATE TABLE IF NOT EXISTS books (
          id INTEGER PRIMARY KEY,
          author TEXT,
          title TEXT
        );
        """
        self.cursor.execute(self.query)
        self.connection.commit()
        self.cursor.execute("""SELECT * FROM books;""")
        rows = self.cursor.fetchall()
        for book in rows:
            super().add_book(book[0], book[1], book[2])

    def add_book(self, book_id, author, title):
        super(BookRepositoryDatabase, self).add_book(book_id, author, title)
        self.cursor.execute("""INSERT INTO books VALUES (?, ?, ?);""", (book_id, author, title))
        self.connection.commit()

    def remove_book(self, book_id):
        super(BookRepositoryDatabase, self).remove_book(book_id)
        self.cursor.execute("""DELETE FROM books WHERE id=?;""", (book_id,))
        self.connection.commit()

    def update_book(self, book_id, new_book):
        super(BookRepositoryDatabase, self).update_book(book_id, new_book)

        self.cursor.execute("""UPDATE books SET id=?, author=?, title=? WHERE id=?;""",
                            (new_book.book_id, new_book.author, new_book.title, book_id))
        self.connection.commit()
