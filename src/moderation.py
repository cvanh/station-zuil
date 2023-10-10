# /usr/bin/env python
import sys
import os
import pandas as pd
from clint.textui import prompt

sys.path.insert(0, os.path.abspath('..'))

# pandas normal limit is 60 but we want to increment it
pd.options.display.max_rows = 9999

# get entries of unmoderated comments
def get_entries():
    unparsed_csv = pd.read_csv("../comments.csv",nrows=99999)
    print(unparsed_csv)
    return unparsed_csv.to_json()

# the menu that allowes the use to remove or approve 
def mod_menu():
    inst_options = [{'selector':'1','prompt':'remove','return':'remove'},
                    {'selector':'2','prompt':'approve','return':'approve'}]

    inst = prompt.options("Full or Partial Install", inst_options)

    return inst

if __name__ == '__main__':
    mod_queue = get_entries()
    print(mod_queue)

    for comment in mod_queue:
        print(comment)
        mod_menu()





