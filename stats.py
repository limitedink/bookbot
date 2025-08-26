def word_count(text):
    words = []
    wc = 0
    words = text.split()
    for word in words:
        wc += 1
    return wc

def char_count(text):
    char_counts = {}
    text = text.lower()
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts
      
