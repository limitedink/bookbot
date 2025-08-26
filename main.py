def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
    words = []
    wc = 0
    words = text.split()
    for word in words:
        wc += 1
    return wc

def main():
    outputtext = get_book_text("./books/frankenstein.txt")
    output = word_count(outputtext)
    print(f"{output} words found in the document")

main()
