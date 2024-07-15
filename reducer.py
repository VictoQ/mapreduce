import sys

current_category = None
current_sum = 0
current_count = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    key, value = data
    value = float(value)

    if current_category == key:
        current_sum += value
        current_count += 1
    else:
        if current_category:
            average = current_sum / current_count
            sys.stdout.write("{0}\t{1}\n".format(current_category, average))
        current_category = key
        current_sum = value
        current_count = 1

if current_category:
    average = current_sum / current_count
    sys.stdout.write("{0}\t{1}\n".format(current_category, average))