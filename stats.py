def word_count(text):
    return len(text.split())

def character_count(text):
    count_dict = {}
    for chara in text.lower(): 
        if chara not in count_dict:
            count_dict[chara] = 1
        else:
            count_dict[chara] += 1
    return count_dict

def sort_on(dict):
    return dict["num"]

def sorted_chara_count(unsorted_dict):
    new_ls = []
    for key,value in unsorted_dict.items():
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = value
        new_ls.append(new_dict)
    new_ls.sort(reverse=True, key=sort_on)
    return new_ls
