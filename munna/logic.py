from data import all_dict_num
from rich import print
import os

def fill_dict(u_input):
    dict_numeric = []
    cnt = len(u_input)

    # filling this with appropriate dictionaries from all_dict_num
    for i in range(cnt):
        dict_numeric.append(all_dict_num.get(i))

    return dict_numeric

def generate_word(u_input , clean_output=0):
    if(len(u_input)<=6):
        dict_numeric = fill_dict(u_input)
        result = ""
        count = 0
        for d in reversed(dict_numeric):
            word = d.get(int(u_input[count]))
            if word:
                result = result +' '+ word
            count = count+1
        if clean_output:
            os.system('clear')
        return result.strip()
    else:
        if clean_output:
            os.system('clear')
        print("[white on red]\nWord limit reached bro!!!! Increment in the data.py for more words.\n")
