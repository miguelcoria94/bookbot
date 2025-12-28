import sys
from stats import count_words, count_letters, sorted_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) == 2:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        num_words = count_words(text)
        chars_dict = count_letters(text)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}")
        print("----------- Word Count ----------")
        print(num_words)
        print("--------- Character Count -------")
        for item in sorted_list(chars_dict):
            print(f"{item['char']}: {item['num']}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()