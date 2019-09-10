import unittest
import yaml
from pathlib import Path
import woordener


class TestExtractor(unittest.TestCase):

    def setUp(self):
        self.base_path = Path(__file__).parent.joinpath('data', 'xml')

    def test_not_in_wikitext(self):
        with self.assertRaises(woordener.SectionFormatError) as ctx:
            self.load_and_parse('extractor-not-wikitext')
            self.fail("exception expected")
        self.assertEqual(ctx.exception.format, 'text/blah')
        self.assertEqual(ctx.exception.title, 'Wiktionary:Welcome, newcomers')

    def test_none(self):
        pages, expected = self.load_and_parse('extractor-none')
        self.assertEqual(pages, expected)

    def test_extract(self):
        pages, expected = self.load_and_parse('extractor-several')
        self.assertEqual(pages, expected)

    def load_and_parse(self, fname):
        path = Path(self.base_path).joinpath(fname + '.xml')
        pages = list()
        collector = lambda title, section: pages.append((title, section))
        woordener.extract(path, collector)

        path = Path(self.base_path).joinpath(fname + '-expected.yaml')
        expected = yaml.load(Path(path).read_text(), Loader=yaml.FullLoader)

        return (pages, expected)
