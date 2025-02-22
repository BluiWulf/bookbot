import sys

from stats import *

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_counts = count_char(text.lower())
    sorted_counts = sort_entries(char_counts)
    print_report(book_path, word_count, sorted_counts)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, word_count, sorted_counts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for counter in sorted_counts:
        if counter["char"].isalpha():
            print(f"{counter["char"]}: {counter["count"]}")
    print("============= END ===============")

main()
