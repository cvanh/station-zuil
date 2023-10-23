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
name = input("name?:")

# generate value's we need
time = time.time()
station = random.choice(stations)


# write to file
data = [name, station, time, re.escape(message)]

with open(f'{os.path.dirname(__file__)}/../comments.csv', 'a') as f:
    writer = csv.writer(f,lineterminator="\n")

    # write the header
    # TODO make it so when the file doenst exist it creates the file and sets the headers
    # writer.writerow(csv_headers)

    # write the data
    writer.writerow(data)
