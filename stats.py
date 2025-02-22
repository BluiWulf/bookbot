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

def sort_on(dict):
    return dict["count"]

def sort_entries(char_counts):
    sorted_list = []
    for char in char_counts:
        sorted_list.append({"char": char, "count": char_counts[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    