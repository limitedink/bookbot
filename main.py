from stats import word_count, char_count, sort_report 
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    outputtext = get_book_text("./books/frankenstein.txt")
    wc = word_count(outputtext)
    cc = char_count(outputtext)
    report = ""
    report = sort_report(cc)

    print(f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {wc} total words
--------- Character Count -------
{report}
============= END ===============""")
main()
