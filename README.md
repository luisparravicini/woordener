
The scripts in this repo parse the [Wiktionary](https://en.wiktionary.org/) xml dump and extracts the Dutch section of each page (if it contains one).

They were tested with the [20190820 dump](https://dumps.wikimedia.org/enwiktionary/20190820/), the downloaded dump is [enwiktionary-20190820-pages-articles.xml.bz2](https://dumps.wikimedia.org/enwiktionary/20190820/enwiktionary-20190820-pages-articles.xml.bz2).

`bin/extract.py` is used for this extraction, it needs two arguments, the first is the path of the xml dump, the second is where it will output the extracted titles and dutch sections.

It needs Python 3.7+.

---

**READ THIS**

As I started to see how to translate the wikipedia templates of each entry I realized the scope is way bigger of what I expected for this project, so this repo will remain as is, no more updates.

`words-all.txt.gz` is the extract list of words from the dump one entry in each line. Each line is a json.dump of each entry.

Haven't tried it but [wiktextract](https://github.com/tatuylonen/wiktextract) seems to do what I wanted to do initially.
