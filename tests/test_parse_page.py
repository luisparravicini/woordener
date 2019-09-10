import unittest
from pathlib import Path
import wikitextparser as wtp


def load_article(path):
    return Path(path).read_text()


def parse_article(path):
    data = load_article(path)
    doc = wtp.parse(data)
    sections = [x for x in doc.sections if x.title == 'Dutch']

    result = None
    if len(sections) > 0:
        result = sections[0].contents
    return result


class TestParsePage(unittest.TestCase):

    def setUp(self):
        # self.maxDiff = None
        self.base_path = Path(__file__).parent.joinpath('data')

    def test_only_dutch_section(self):
        article, expected = self.load_and_parse('only-dutch')
        self.assertEqual(article, expected)

    def test_several_sections(self):
        article, expected = self.load_and_parse('several-sections')
        self.assertEqual(article, expected)

    def test_no_dutch_section(self):
        article, expected = self.load_and_parse('no-dutch')
        self.assertEqual(article, expected)

    def load_and_parse(self, fname):
        path = Path(self.base_path).joinpath(fname + '.txt')
        article = parse_article(path)

        path = Path(self.base_path).joinpath(fname + '-expected.txt')
        expected = None
        if path.exists():
            expected = load_article(path)

        return (article, expected)


if __name__ == '__main__':
    unittest.main()
