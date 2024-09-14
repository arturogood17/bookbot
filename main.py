def main():
    book_path = "books/frankenstein.txt"
    texto= get_book_path(book_path) #me da el texto
    words = count_words(texto) #me da las palabras. int.
    dict_letter_unordered = count_char(texto) #me da el dict sin ordenar
    list_ordered = list_ord(dict_letter_unordered) #Me da la lista ordenada
    print("--- Begin report of books/frankenstein.txt ---")
    print("")
    print(f"{words} words found in the document")
    for i in list_ordered:
        if i["char"].isalpha():
            print(f"The {i["char"]} character was found {i["num"]} times")
    print("--- End report ---")


def get_book_path(book_path):
    with open("books/frankenstein.txt") as file:
        return file.read()


def count_words(book):
    words= book.split()
    return len(words)
    
def count_char(text):
    text= text.lower()
    deco ={}
    for i in text:
        if i in deco:
            deco[i] += 1
        else:
            deco[i] = 1
    return deco

def list_ord(dict_unordered):
    sorted_list=[]
    for ch in dict_unordered:
        sorted_list.append({"char": ch, "num": dict_unordered[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list



def sort_on(dict):
    return dict["num"]


main()