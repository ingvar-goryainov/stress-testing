#!/usr/bin/env python3
import csv
import sys
import random
import string

rng = random.Random(0)

csv_writer = csv.writer(sys.stdout)
csv_writer.writerow(["id", "value"])

for i in range(1_000_000):
    short_random_string = "".join(
        rng.choice(string.ascii_letters) for _ in range(20))
    csv_writer.writerow([i, short_random_string])