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

def sort_on(d):
    return d["num"]
  
def sort_char_count(char_count):
    sorted_counts = []
    for ch in char_count:
        sorted_counts.append({"char": ch, "num": char_count[ch]})
    sorted_counts.sort(reverse=True, key=sort_on)

    return sorted_counts