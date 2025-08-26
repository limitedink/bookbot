from stats import word_count
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    outputtext = get_book_text("./books/frankenstein.txt")
    output = word_count(outputtext)
    print(f"{output} words found in the document")

main()
