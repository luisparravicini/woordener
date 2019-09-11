#!/usr/bin/env python3

import sys
import os
from pathlib import Path
import json
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import woordener  # noqa: E402


out_file = None
index = 0
printed = 0
frames = ['.', '·', '•', 'o', 'O']

def collector(title, section):
    global out_file, index, printed, frames

    out_file.write(json.dumps((title, section)))
    out_file.write("\n")

    print(f'{frames[index]}\x08', end='', flush=True)
    printed += 1
    if printed > 10:
        printed = 0
        index += 1
        if index >= len(frames):
            index = 0
            print('.', end='')


if len(sys.argv) < 3:
    print(f'usage: {sys.argv[0]} <wiktionary_pages_dump.xml> <output_path>')
    os.sys.exit(1)

in_path = Path(sys.argv[1])
out_path = sys.argv[2]
with open(out_path, 'w') as file:
    # HACK: find a better way
    out_file = file

    woordener.extract(in_path, collector)
