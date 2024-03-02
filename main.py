def main():
    text = get_book()
    num_words= counts(text)
    letters = num_letter(text)
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")



def get_book():
    with open("github.com/arturogood17/bookbot//books/frankenstein.txt") as f:
        return f.read()

    
def counts (text):
    string= text.split()
    return len(string)

def num_letter(text):
    dicc_letters= {}
    for letter in (text):
        letter_low= letter.lower()
        if letter_low in dicc_letters:
            dicc_letters[letter_low]+= 1
        else:
            dicc_letters[letter_low]= 1
    return dicc_letters

def sort_on(letters):

    


main()