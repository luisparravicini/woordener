#!/usr/bin/env python3

import sys
import os
from pathlib import Path
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import woordener  # noqa: E402


out_file = None
index = 0
printed = 0
frames = ['.', '·', '•', 'o', 'O']
# used for profiling
profiling = False
iteration_count = 0


# used for profiling
def check_iterations():
    global iteration_count
    iteration_count += 1
    if iteration_count > 1000:
        os.sys.exit(1)


def update_spinner():
    global index, printed, frames

    if printed == 0:
        print(f'{frames[index]}\x08', end='', flush=True)
    printed += 1
    if printed > 10:
        printed = 0
        index += 1
        if index >= len(frames):
            index = 0
            # HACK: the output was stuck at the end of the
            # first line, the two dots make it go down to
            # another line
            print('..', end='', flush=True)


def collector(title, section):
    global profiling
    if profiling:
        check_iterations()

    global out_file

    out_file.write(json.dumps((title, section)))
    out_file.write("\n")

    update_spinner()


if len(sys.argv) < 3:
    print(f'usage: {sys.argv[0]} <wiktionary_pages.xml> <output_path> [-p]')
    os.sys.exit(1)

in_path = Path(sys.argv[1])
out_path = sys.argv[2]
profiling = (len(sys.argv) > 3 and sys.argv[3] == '-p')
if profiling:
    print("profiling")
with open(out_path, 'w') as file:
    # HACK: find a better way
    out_file = file

    woordener.extract(in_path, collector)
