def get_book_text(filepath):
    with open(filepath, 'r') as f:
        return f.read()

def count_words(book):
    b = book.split()
    return len(b)
      