import string
import operator

def get_num_words (filepath):
    num_words = 0
    with open(filepath) as f:
        content = f.read()
        words = content.split()
        for i in words:
            num_words += 1
    print(f"Found {num_words} total words")

def get_num_characters (filepath):
    num_characters = 0
    characters = list(string.ascii_lowercase) + list(string.punctuation) + list(string.digits[1:])
    character_counts = {}
    with open(filepath) as f:
        content = f.read()
        content = content.lower()
        for i in characters:
            char_count = 0
            for char in content:
                if i == char:
                    char_count += 1
            character_counts[i] = char_count

    #    print(num_characters)
        return character_counts

def sort_and_print (filepath):
    list_characters = []
    some_var = get_num_characters(filepath)
    sorted_some_var = dict(sorted(some_var.items(), key=lambda item: item[1], reverse=True))
    another_sorted_list = dict(sorted(some_var.items()))
    for i in sorted_some_var:
        thing = sorted_some_var[i]
        if i.isalpha():
            print(f"{i}: {thing}")

    
    
