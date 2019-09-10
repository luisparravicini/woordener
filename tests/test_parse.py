import unittest
import os
from pathlib import Path


def load_article(path):
    return Path(path).read_text()


def parse_article(path):
    data = load_article(path)
    return data


class TestParsePage(unittest.TestCase):

    def setUp(self):
        self.base_path = Path(__file__).parent.joinpath('data')

    def test_only_nl_section(self):
        article, expected = self.load_and_parse('only-nl')
        self.assertEqual(article, expected)

    def test_several_sections(self):
        article, expected = self.load_and_parse('several-sections')
        self.assertEqual(article, expected)

    def load_and_parse(self, fname):
        path = Path(self.base_path).joinpath(fname + '.txt')
        article = parse_article(path)

        path = Path(self.base_path).joinpath(fname + '-expected.txt')
        expected = load_article(path)

        return (article, expected)


if __name__ == '__main__':
    unittest.main()
