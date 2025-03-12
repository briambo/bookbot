from stats import get_num_words, get_num_char

def main ():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    num_char = get_num_char(book_text)
    print(f"{num_words} words found in the document")
    print(num_char)

def get_book_text (filepath):
    with open(filepath) as f:
        return f.read()
        

main()    