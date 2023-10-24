# /usr/bin/env python
from clint.textui import prompt
import csv
from utils.db import db

# get entries of unmoderated comments
def get_entries():
    unparsed_csv = open("comments.csv","r") 

    # parse the csv
    csvreader = csv.reader(unparsed_csv, delimiter=',',lineterminator="")

    # we want a simple array for our comments
    array = []
    for index,row in enumerate(csvreader):
        # we dont want to add the csv headers to our array so we dont add it
        array.append(row)

    return array


# the menu that allowes the use to remove or approve and shows the comment 
def moderation_menu(comment):
    print(f"{comment[0]} said: {comment[3]} on {comment[2]} on station: {comment[1]}")
    inst_options = [{'selector':'1','prompt':'verwijderen','return': False},
                    {'selector':'2','prompt':'doorlaten','return': True}]

    inst = prompt.options("comment doorlaten of verwijderen?", inst_options)

    return inst

# whiteout the file by writing empty string
def clean_comments_csv():
    file = open("comments.csv","w") 
    file.write("")
    file.close()

def insert_comments_to_database(comments):
    conn = db()

    # we insert comment per comment 
    for comment in comments:
        conn.execute(
        f"""
        INSERT INTO comments(
    	"name", "station", "time", "message")
	    VALUES ('{comment[0]}', '{comment[1]}', {comment[2]}, '{comment[3]}');
        """)
    
if __name__ == '__main__':
    mod_queue = get_entries()

    # for item in mod_queue:
    accepted_comments = []
    for comment in mod_queue:
        is_comment_approved = moderation_menu(comment)

        if is_comment_approved: 
            accepted_comments.append(comment)
    
    insert_comments_to_database(accepted_comments)
    clean_comments_csv()
