from stats import word_count, character_count,sorted_chara_count

def get_book_content(relative_path):
    with open(relative_path) as book:
        text_content = book.read()
    return text_content

def chara_print_format(sorted_list):
    for pair in sorted_list:
        if pair["char"].isalpha():
            char = pair["char"]
            num = pair["num"]
            print(f"{char}: {num}")

def main():
    total_words = word_count(get_book_content("books/frankenstein.txt"))
    print(f"Found {total_words} total words")
    each_chara_count_dict = character_count(get_book_content("books/frankenstein.txt"))

    chara_print_format(sorted_chara_count(each_chara_count_dict))
    

main()
