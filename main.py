#!/usr/bin/env python3

from stats import get_num_words
from stats import get_num_characters
from stats import sort_and_print
import sys

def get_book_text (filepath):
    with open(filepath) as f:
        file_contents = f.read()
    #print(file_contents)
    print(filepath)

def main ():
    
    if len(sys.argv) < 2 or sys.argv[0] != "main.py":
        sys.exit("Usage: python3 main.py <path_to_book>")
    filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print(f"----------- Word Count ----------")  
    get_num_words(filepath)
    print(f"--------- Character Count -------")
#    get_num_characters(filepath)
    sort_and_print(filepath)
    print(f"============= END ===============")
    

if __name__ == "__main__":
    main()
