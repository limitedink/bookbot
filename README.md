# BookBot

A command-line Python tool that analyzes text files and generates statistical reports on word and character frequency.

## Overview

BookBot is a text analysis utility that reads any text file and provides detailed statistics including:
- Total word count
- Character frequency analysis (alphabetic characters only)
- Sorted character distribution report

This project was built as part of the [Boot.dev](https://www.boot.dev) Python curriculum.

## Features

- 📊 Word counting with accurate tokenization
- 🔤 Character frequency analysis (case-insensitive)
- 📈 Sorted character distribution from most to least frequent
- 📝 Clean, formatted report output
- ⚡ Fast processing for large text files

## Installation

1. Clone the repository:
```bash
git clone https://github.com/bootdev/bookbot.git
cd bookbot
```

2. Ensure you have Python 3.6+ installed:
```bash
python3 --version
```

## Usage

Run the script with a path to any text file:

```bash
python3 main.py <path_to_book>
```

### Example

```bash
python3 main.py books/frankenstein.txt
```

### Sample Output

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 77986 total words
--------- Character Count -------
e: 46043
t: 30365
a: 26743
o: 25225
i: 24613
n: 24367
...
============= END ===============
```

## Project Structure

```
bookbot/
├── main.py          # Entry point and report generation
├── stats.py         # Statistical analysis functions
├── .gitignore       # Git ignore rules
└── README.md        # This file
```

## How It Works

1. **Text Reading**: The program reads the entire text file into memory
2. **Word Counting**: Splits text on whitespace and counts tokens
3. **Character Analysis**: 
   - Converts all text to lowercase for case-insensitive analysis
   - Counts only alphabetic characters (a-z)
   - Ignores numbers, punctuation, and special characters
4. **Sorting**: Orders characters by frequency (descending)
5. **Report Generation**: Formats and displays the results

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

## Contributing

This is a learning project from Boot.dev, but suggestions and improvements are welcome!

## License

This project is open source and available for educational purposes.

## Acknowledgments

- Built as part of the [Boot.dev](https://www.boot.dev) Python course
- Thanks to the Boot.dev community for support and guidance
