from stats import *
import sys

def main():
	if len(sys.argv) < 2:
		print("Usage: python main.py <path_to_book>")
		sys.exit(1)
	book_path = sys.argv[1]
	text = find_book(book_path)
	word_count = find_word_count(text)
	characters_report = find_character_count(text)
	sorted_report = report_sort(characters_report)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")
	print(sorted_report)
	print("============= END ===============")

def find_book(book):
# find, open, and read text of book document
	with open(book) as f:
		return f.read()

main()
