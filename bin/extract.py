#!/usr/bin/env python3

import sys
import os
from pathlib import Path
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import woordener  # noqa: E402


out_file = None


def collector(title, section):
    global out_file

    out_file.write(json.dumps((title, section)))
    out_file.write("\n")

    print('.', end='', flush=True)


if len(sys.argv) < 3:
    print(f'usage: {sys.argv[0]} <wiktionary_pages_dump.xml> <output_path>')
    os.sys.exit(1)

in_path = Path(sys.argv[1])
out_path = sys.argv[2]
with open(out_path, 'w') as file:
    # HACK: find a better way
    out_file = file

    woordener.extract(in_path, collector)
