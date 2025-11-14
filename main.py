import os
from functions import *

def main():
    abs_path = os.path.dirname(__file__)
    relative_path = "books/frankenstein.txt"
    book_path = os.path.join(abs_path, relative_path) 
    book = get_book_text(book_path)

    print(book)


if __name__ == "__main__":
    main()