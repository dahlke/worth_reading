from __future__ import print_function

import os
import json
from pynytimes import NYTAPI

NYT_TOKEN = os.getenv("NYT_TOKEN", None)

books_data = {}

def main():
    print("NYT Token", NYT_TOKEN)
    nyt = NYTAPI(NYT_TOKEN)

    authors = {}
    with open("books.json", "r") as f:
        authors = json.loads(f.read())

    for author in authors:
        books = authors[author]
        for book in books:
            reviews = nyt.book_reviews(title=book)
            print(author, book, reviews)


if __name__ == '__main__':
    main()


"""
book_dir = "/Users/neil/Downloads/books"
authors = os.listdir(book_dir)

for author in authors:
    author_dir = f"{book_dir}/{author}"
    if os.path.isdir(author_dir):
        raw_books = os.listdir(author_dir)
        books = []
        for raw_book in raw_books:
            split_book = raw_book.split(" ")
            print(split_book)
            book = " ".join(split_book[:-1])
            books.append(book)

        books_data[author] = books

with open("books.json", "w") as f:
    f.write(json.dumps(books_data, indent=4))
"""
