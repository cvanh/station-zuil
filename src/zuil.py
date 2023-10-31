# /usr/bin/env python
# not my proudest work, but functional programmin ftw

import csv
import time
import random
import re
import os

csv_headers = ["name", "station", "time", "message"]

# the list of random stations that are used
stations = ["den haag", "amsterdam", "leiden"]

# collect data from user
message = input("message?:")

if len(message) > 140:
    print("your message must be shorter than 140 chars")
    exit(1)

name = input("name?:")

# generate value's we need
time = int(time.time())
station = random.choice(stations)


# write to file
data = [name, station, time, re.escape(message)]

with open(f'{os.path.dirname(__file__)}/../comments.csv', 'a') as f:
    writer = csv.writer(f,lineterminator="\n",dialect="unix")

    # write data to a new line in the csv
    writer.writerow(data)
