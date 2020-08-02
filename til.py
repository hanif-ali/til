#!/usr/bin/python

import sys
import re

README_FILE = "README.md"

def get_new_count(file_content):
    til_re = re.compile(r"- \[.*\]\(.*\)")
    lines = file_content.split("\n")
    til_lines = list(filter(lambda x: til_re.match(x), lines))
    return len(til_lines)

def get_content_with_changed_count(file_content, new_count):
    count_re = re.compile(r"(_\d+)(\sTILs and counting..._)")
    replacement_string = fr"_{new_count}\2"
    return count_re.sub(replacement_string, file_content)

if __name__ == "__main__":
    with open(README_FILE) as r_file:
        file_content = r_file.read()

    command = sys.argv[1]
    
    if command == "updatecount":
        new_count = get_new_count(file_content)
        with open(README_FILE, "w") as r_file:
            new_content = get_content_with_changed_count(file_content, new_count)
            r_file.write(new_content)
        print(f"[TIL COUNT UPDATED] -> {new_count}")
