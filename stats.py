from typing import Dict

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(file_contents: str) -> int:
    return len(file_contents.split())

def get_character_appearance(file_contents:str) -> Dict[str,int]:
    counts: Dict[str,int] = {}
    
    for character in file_contents:
        character = character.lower()
        if character != ' ':
            if character in counts:
                counts[character] += 1
            else:
                counts[character] = 1
    return  counts

def sort_dict_by_count(character_appearances:Dict[str,int]) -> Dict[str,int]:
    
    character_appearances_sorted = sorted(character_appearances.items(), key=lambda item: item[1], reverse=True)
    character_appearances_sorted = [f"{key}: {value}" for key, value in character_appearances_sorted]
    return character_appearances_sorted