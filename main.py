from __future__ import print_function

import os
from googleapiclient.discovery import build

GOOGLE_API_TOKEN = os.getenv("GOOGLE_API_TOKEN", None)


def main():
    print("TOKEN", GOOGLE_API_TOKEN)
    books_service = build("books", "v1", developerKey=GOOGLE_API_TOKEN)
    # print(books_service.bookshelves)
    print(dir(books_service.bookshelves))
    # print(books_service.mylibrary)
    print(dir(books_service.mylibrary))
    print(dir(books_service))


if __name__ == '__main__':
    main()