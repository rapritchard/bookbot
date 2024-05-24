def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    get_book_report(book_path, num_words, chars_dict)
        
def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
        
def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []
    for char, num in chars_dict.items():
        sorted_list.append({"char": char, "num": num})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list


def get_book_report(book_path, words, chars_dict):
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"Number of words: {words}\n")
    
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The {item["char"]} character appears {item["num"]} times")
    
    print(f"--- End report ---")

        
main()