def word_count(text):
    words = []
    wc = 0
    words = text.split()
    for word in words:
        wc += 1
    return wc
