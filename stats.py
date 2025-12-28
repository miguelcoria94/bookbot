def count_words(text):
    count = len(text.split())
    return f"Found {count} total words"

def count_letters(text):
    words = text.split()

    letter_counts = {}

    for word in words:
        for letter in word:
            letter = letter.lower()
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1

    return letter_counts

def sort_on(items):
    return items["num"]

def sorted_list(dict):
    res = []
    for item in dict:
        res.append({"char": item, "num": dict[item]})

    res.sort(reverse=True, key=sort_on)

    return res