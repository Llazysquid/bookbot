def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def get_word_count(file_path):
    return len(get_book_text(file_path).split())

def get_character_count(file_path):
    character_dictionary = {}
    
    for character in get_book_text(file_path).lower():
        if character in character_dictionary:
            character_dictionary[character] += 1
        else:
            character_dictionary[character] = 1

    return character_dictionary

def list_characters(dict):
    list = []

    for character in dict:
        list.append({"char": character, "num":dict[character]})

    def sort_on(dictbob):
        return dictbob["num"]
    
    list.sort(reverse=True, key=sort_on)
    
    return list
    

