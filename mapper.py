
import sys

valid_categories = {"Computers", "Cameras", "Video Games"}

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, item, category, sales, payment = data
        if category in valid_categories:
            sys.stdout.write("{0}\t{1}\n".format(category, sales))