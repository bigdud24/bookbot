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

def find_word_count(book):
# finds how many words are in the book document
	words = book.split()
	return len(words)

def find_character_count(text):
# finds how many of each character are in the book document
	lowercase_book = text.lower()
	characters = {}
	for character in lowercase_book:
		if character in characters:
			characters[character] += 1
		else:
			characters[character] = 1
	return characters

def report_sort(text):
# sorts the list of all occurrences of all alphabetic characters in the book document

	# dict of characters into list of dicts of characters
	character_list = []
	for char, count in text.items():
		if char.isalpha():
			character_list.append({'char': char, 'num': count})

	# actually sorting of the list
	def sorter(dict):
		return dict["num"]
	character_list.sort(reverse=True, key=sorter)

	# making it neat
	report = []
	for character in character_list:
		report.append(f"The '{character['char']}' character was found {character['num']} times")
	return '\n'.join(report)


main()
