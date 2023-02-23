import sqlite3

# this code is used to connect DB 

conn = sqlite3.connect('bookstore.db')
cursor = conn.cursor()

# this code is used to create book list or table
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
  id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  author TEXT NOT NULL,
  price REAL NOT NULL
)
''')
conn.commit()

# this code is used to add a new book
def add_book(title, author, price):
    cursor.execute('''
    INSERT INTO books (title, author, price)
    VALUES (?,?,?)
    ''', (title, author, price))
    conn.commit()

# this is book list abd you can add more book list
#add_book("book name" , "author" "price")

add_book("The Great Gatsby", "F. Scott Fitzgerald", 5000)
add_book("Pride and Prejudice", "Jane Austen", 4000)
add_book("The Diary of a Young Girl" , "Anne Frank" , 3000)
add_book("To Kill a Mockingbird" , "Harper Lee" , 2000)
add_book("1984" , "George Orwell" ,1000)
conn.close()

########################--------------this is the process of connect with database----------------------###################

# In this example, a SQLite database named bookstore.db is created (or opened if it already exists). A books table is 
# created within the database to store information about each book, including its title, author, and price. The add_book 
# function can be used to add new books to the database.
