import pandas as pd
import os
from os import walk


def get_generator(file_path):
    for item in open(file_path, "r"):
        yield item


files = []
for (dir_path, dir_names, file_names) in walk("C:\work\DA-1936\work_dir"):
    files.extend(file_names)

total = 0
for file in files:
    if file.find('.txt'):
        print(file)
        row_count = 0
        for row in get_generator(f"work_dir/{file}"):
            row_count += 1
        # remove 1 line for header
        total += (row_count - 1)
        print(f"row count: {(row_count - 1)}")
        print(f"total count: {total}")

print(total)
