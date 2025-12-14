from stats import get_book_text,get_word_count,get_character_appearance,sort_dict_by_count
import sys

def main(file_path:list):
    if len(file_path) > 1:
        book_text = get_book_text(file_path[1])
        word_count = get_word_count(book_text)
        print(f'Found {word_count} total words')
        character_appearances = get_character_appearance(book_text)
        character_appearances = sort_dict_by_count(character_appearances)
        print(character_appearances)
    else:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

main(sys.argv)