from stats import count_words 
from stats import char_appears
from stats import sort_count
import sys


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    try:
        output = get_book_text(sys.argv[1])
    except Exception:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 

    word_count = count_words(output)
    #pair_list = sort_count(char_appears(output))
    #print (f"{word_count} words found in the document")
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print (f"Found {word_count} total words")
    #print (char_appears(output))
    print("--------- Character Count -------")
    for char_dict in sort_count(char_appears(output)):
        character = char_dict["char"]
        count = char_dict["num"]
        if character.isalpha() == True:
            print (f"{character}: {count}")
    print("============= END ===============")
main()
