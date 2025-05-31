from stats import word_count, character_count

def get_book_content(relative_path):
    with open(relative_path) as book:
        text_content = book.read()
    return text_content

def main():
    total_words = word_count(get_book_content("books/frankenstein.txt"))
    print(f"{total_words} words found in the document")
    each_chara_count_dict = character_count(get_book_content("books/frankenstein.txt"))
    print(each_chara_count_dict)

main()
