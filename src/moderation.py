# /usr/bin/env python
from clint.textui import prompt
import csv
from utils.db import db
import time
from datetime import datetime

# TODO make prompt
moderator = "pieter"
moderator_id = "f124b7cf-324f-45d9-9352-24181116e7a4"

# get entries of unmoderated comments
def get_entries():
    unparsed_csv = open("comments.csv","r") 

    # parse the csv
    csvreader = csv.reader(unparsed_csv, delimiter=',',lineterminator="")

    # we want a simple array for our comments
    array = []
    for index,row in enumerate(csvreader):
        # we dont want to add the csv headers to our array so we dont add it, while we are at it we format it to an object for easier handeling
        formatted_comment = {
            "name": row[0],
            "station": row[1],
            "time": row[2],
            "message": row[3]
        }

        array.append(formatted_comment)

    return array


# the menu that allowes the use to remove or approve and shows the comment 
def moderation_menu(comment):
    print(comment)
    print(f"{comment['name']} said: {comment['message']} on {comment['time']} on station: {comment['station']}")
    inst_options = [{'selector':'1','prompt':'verwijderen','return': "trashed"},
                    {'selector':'2','prompt':'doorlaten','return': "published"}]

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
    	"name", "station", "time", "message","status","last_edit_time","last_edit_by","id")
	    VALUES ('{comment['name']}', '{comment['station']}', {comment['time']}, '{comment['message']}','{comment['status']}','{comment['last_edit_time']}', '{comment['last_edit_by']}',uuid_generate_v4());
        """)
    
if __name__ == '__main__':
    mod_queue = get_entries()

    # for item in mod_queue:
    accepted_comments = []
    for item,comment in enumerate(mod_queue):
        mod_queue[item]["status"] = moderation_menu(comment)
        mod_queue[item]["last_edit_time"] = datetime.fromtimestamp(time.time())
        mod_queue[item]["last_edit_by"] = moderator_id 


    accepted_comments.append(comment)
    
    insert_comments_to_database(accepted_comments)
    # clean_comments_csv()
