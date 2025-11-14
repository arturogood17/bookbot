import os
from stats import *

def main():
    abs_path = os.path.dirname(__file__)
    relative_path = "books/frankenstein.txt"
    book_path = os.path.join(abs_path, relative_path) 
    book = get_book_text(book_path)

    words = count_words(book)
    print(f"Found {words} total words")
    print()
    chars = count_char(book)
    for k, v in chars.items():
        print(f"'{k}': {v}")
    print()

if __name__ == "__main__":
    main()