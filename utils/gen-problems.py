#!/usr/bin/env python3

import os
from hashlib import blake2s

CODES = {
    "E": "encoding",
    "F": "font",
    "I": "input",
    "P": "processing"
}

def hash_line(line):
    return blake2s(line.encode(), digest_size=2, key=b'', salt=b'', usedforsecurity=False).hexdigest()

def process_files(input_dir, output_file):
    with open(output_file, 'w') as outfile:
        for code, filename in CODES.items():
            file_path = os.path.join(input_dir, filename)
            if os.path.isfile(file_path):
                with open(file_path, 'r') as infile:
                    for line in infile:
                        hash = hash_line(line)
                        outfile.write(f"{code}-{hash}\t{line}")

if __name__ == "__main__":
    input_dir = "problems"
    output_file = "problems.tsv"
    process_files(input_dir, output_file)
