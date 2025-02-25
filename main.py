from stats import *

def main():
	book_path = "books/frankenstein.txt"
	text = find_book(book_path)
	word_count = find_word_count(text)
	characters_report = find_character_count(text)
	sorted_report = report_sort(characters_report)

	print(f"--- Begin report of {book_path} ---")
	print(f"{word_count} words found in the document")
	print("")
	print(sorted_report)
	print("--- End report ---")

def find_book(book):
# find, open, and read text of book document
	with open(book) as f:
		return f.read()

main()
