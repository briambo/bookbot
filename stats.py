def get_num_words (text):
    return len(text.split())

def get_num_char (text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars  
  
def sort_char_count(char_count):
    sorted_counts = [
        {"character": char, "count":count}
        for char, count in char_count.items() if char.isalpha()
    ]
    sorted_counts.sort(key=lambda x: x["count"], reverse=True)
    return sorted_counts