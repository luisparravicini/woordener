
The scripts in this repo parse the (https://en.wiktionary.org/)[Wiktionary] xml dump and extracts the Dutch section of each page (if it contains one).

They were tested with the (https://dumps.wikimedia.org/enwiktionary/20190820/)[20190820 dump], the downloaded dump is (https://dumps.wikimedia.org/enwiktionary/20190820/enwiktionary-20190820-pages-articles.xml.bz2)[enwiktionary-20190820-pages-articles.xml.bz2].

`bin/extract.py` is used for this extraction, it needs two arguments, the first is the path of the xml dump, the second is where it will output the extracted titles and dutch sections.

It needs Python 3.7+.
