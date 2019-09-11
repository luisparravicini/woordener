import unittest
from pathlib import Path
import woordener


class TestParsePage(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.base_path = Path(__file__).parent.joinpath('data', 'page')

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
        article = woordener.extract_section(self.load_article(path))

        path = Path(self.base_path).joinpath(fname + '-expected.txt')
        expected = None
        if path.exists():
            expected = self.load_article(path)

        return (article, expected)

    def load_article(self, path):
        return Path(path).read_text()
