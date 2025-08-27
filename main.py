import sys
from stats import word_count, char_count, sort_report 
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    filepath = sys.argv[1]
    outputtext = get_book_text(filepath)
    wc = word_count(outputtext)
    cc = char_count(outputtext)
    report = ""
    report = sort_report(cc)
    bookdirectory = filepath

    print(f"""============ BOOKBOT ============
Analyzing book found at {bookdirectory}...
----------- Word Count ----------
Found {wc} total words
--------- Character Count -------
{report}
============= END ===============""")
main()
