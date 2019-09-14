
The scripts in this repo parse the [Wiktionary](https://en.wiktionary.org/) xml dump and extracts the Dutch section of each page (if it contains one).

They were tested with the [20190820 dump](https://dumps.wikimedia.org/enwiktionary/20190820/), the downloaded dump is [enwiktionary-20190820-pages-articles.xml.bz2](https://dumps.wikimedia.org/enwiktionary/20190820/enwiktionary-20190820-pages-articles.xml.bz2).

`bin/extract.py` is used for this extraction, it needs two arguments, the first is the path of the xml dump, the second is where it will output the extracted titles and dutch sections.

It needs Python 3.7+.


As I started to see how to translate the wikipedia templates of each entry I realized the scope was way too much of what I expected, so this repo will remain as is, no more updates. Haven't tried it but [wiktextract](https://github.com/tatuylonen/wiktextract) seems to do what I wanted to do initially.
