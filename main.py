import sys
from stats import get_num_words, letter_counts

def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        return f.read()

def sort_on(items):
    return items["num"]

def print_report(letter_count: list, words: int):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")

    letter_count.sort(reverse=True,key=sort_on)

    for kvp in letter_count:
        if kvp["char"].isalpha():
            print(f"{kvp['char']}: {kvp['num']}")
            
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    bookPath = sys.argv[1]
    frankensteinText = get_book_text(bookPath)
    print_report(letter_counts(frankensteinText), len(get_num_words(frankensteinText)))
    
main()