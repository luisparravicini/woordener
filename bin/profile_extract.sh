#!/bin/bash

python -m cProfile -s tottime ./bin/extract.py $1 words.txt -p
