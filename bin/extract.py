#!/usr/bin/env python3

import sys
import os
from pathlib import Path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import woordener


def collector(title, section):
    # print(title, section)
    print(title)


if len(sys.argv) < 2:
    print(f'usage: {sys.argv[0]} <wiktionary_pages_dump.xml>')
    os.sys.exit(1)

path = Path(sys.argv[1])
woordener.extract(path, collector)
