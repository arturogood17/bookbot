import os
from stats import *

def main():
    abs_path = os.path.dirname(__file__)
    relative_path = "books/frankenstein.txt"
    book_path = os.path.join(abs_path, relative_path) 
    book = get_book_text(book_path)
    words = count_words(book)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {relative_path}")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    chars = count_char(book)
    report =  []
    for k, v in chars.items():
        report.append({"char": k, "num": v})        
    
    report.sort(reverse= True, key=sort_on)
    
    for i in range(len(report)):
        key = report[i]["char"]
        if key.isalpha():
            c = report[i]["num"]
            print(f"{key}: {c}")
    print("============= END ===============")


if __name__ == "__main__":
    main()