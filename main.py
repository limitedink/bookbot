from stats import word_count, char_count
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    outputtext = get_book_text("./books/frankenstein.txt")
    wc = word_count(outputtext)
    cc = char_count(outputtext)
    print(f"{wc} words found in the document")
    print(cc)

main()
