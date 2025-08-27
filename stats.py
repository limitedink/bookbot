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
        if not char.isalpha():
            continue
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_report(char_counts):
    report_list = list(char_counts.items())

    def sort_by_count(item):
        return item[1]

    report_list.sort(reverse = True, key=sort_by_count)
    return "\n".join(f"{char}: {count}" for char, count in report_list)



      
