from stats import get_num_words, get_num_char, sort_char_count

def main ():
    print("============ BOOKBOT ============")
    print("Analyzing book found at frankenstein.txt...")
    print("----------- Word Count ----------")
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    
    print(f"Found {num_words} total words")
    
    print("--------- Character Count -------")
    num_char = get_num_char(book_text)
    sorted_chars = sort_char_count(num_char)
    for item in sorted_chars:
        print(f"{item['character']}: {item['count']}")

    print("============= END ===============")

def get_book_text (filepath):
    with open(filepath) as f:
        return f.read()
        

main()    