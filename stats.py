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
