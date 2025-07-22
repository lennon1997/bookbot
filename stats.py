def count_words(text):
    words = text.split()
    return len(words)

def char_appears(text):
    letter_count = 0
    letters = {}
    lower_case = text.lower()
    for i in lower_case:
        if i not in letters:
            letters[i] = 1
        else:
            letters[i] += 1     
    return letters

def sort_count(char_counts):
    dict_list = []
    for key, value in char_counts.items():
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = value
        dict_list.append(new_dict)
    dict_list.sort(reverse=True, key=sort)
    return dict_list
         
def sort(item):
    return item["num"]

