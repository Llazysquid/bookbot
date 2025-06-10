import sys

from stats import get_character_count, get_word_count, list_characters

def main():
    if len(sys.argv) >= 2:
        character_count_proper = list_characters(get_character_count(sys.argv[1]))
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        print(f'Found {get_word_count(sys.argv[1])} total words')
        print("--------- Character Count -------")
        for i in character_count_proper:
            if i["char"].isalpha():
                print(f'{i["char"]}: {i["num"]}')
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()