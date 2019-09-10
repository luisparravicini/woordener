import unittest
import yaml
import copy
from pathlib import Path
import woordener

class TestExtractor(unittest.TestCase):

    def setUp(self):
        self.base_path = Path(__file__).parent.joinpath('data', 'xml')

    def test_not_in_wikitext(self):
        with self.assertRaises(woordener.SectionFormatError):
            self.load_and_parse('extractor-not-wikitext')
            self.fail("exception expected")

    def test_none(self):
        pages, expected = self.load_and_parse('extractor-none')
        self.assertEqual(pages, expected)

    def test_extract(self):
        pages, expected = self.load_and_parse('extractor-several')
        self.assertEqual(pages, expected)

    def load_and_parse(self, fname):
        path = Path(self.base_path).joinpath(fname + '.xml')
        pages = list()
        collector = lambda x: pages.append(copy.copy(x))
        woordener.extract(path, collector)

        path = Path(self.base_path).joinpath(fname + '-expected.yaml')
        expected = yaml.load(Path(path).read_text(), Loader=yaml.FullLoader)

        return (pages, expected)
