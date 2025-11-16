def get_book_text(filepath):
    with open(filepath, 'r') as f:
        return f.read()

def count_words(book):
    b = book.split()
    return len(b)

def count_char(book):
    chars = {}
    for l in book:
        l = l.lower()
        if l in chars:
            chars[l] += 1
        else:
            chars[l] = 1
    return chars

def sort_on(book):
    return book["num"]