def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_counts = count_char(text.lower())
    print_report(book_path, word_count, char_counts)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_char(text):
    char_counts = {}
    for char in text:
        if not char in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] = char_counts[char] + 1
    return char_counts

def print_report(book_path, word_count, char_counts):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    for char in char_counts:
        if char.isalpha():
            print(f"The '{char}' character was found {char_counts[char]} times")
    print("\n--- End report ---")

main()
