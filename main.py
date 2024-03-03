def main():
    text = get_book()
    num_words= counts(text)
    letters = num_letter(text)
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print("")
    new_l(letters)
    print("")
    print("--- End report ---")



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
    for i in letters:
        return letters[i]
        
def new_l(letters):
    l_sort= []
    for i in letters:
        if i.isalpha():
           new_dict = {i:letters[i]}
           l_sort.append(new_dict)
    l_sort.sort(reverse=True, key=sort_on)
    for item in l_sort:
        for key in item:
            print (f"The {item} character was found {item[key]} times")

main()