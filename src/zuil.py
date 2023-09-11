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

with open(f'{os.path.dirname(__file__)}/../comments.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(csv_headers)

    # write the data
    writer.writerow(data)
