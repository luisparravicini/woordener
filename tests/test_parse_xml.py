import unittest
import yaml
import copy
from pathlib import Path
import woordener


class TestParseXML(unittest.TestCase):

    def setUp(self):
        self.base_path = Path(__file__).parent.joinpath('data', 'xml')

    def test_parse(self):
        pages, expected = self.load_and_parse('parse-1')
        self.assertEqual(pages, expected)

    def load_and_parse(self, fname):
        path = Path(self.base_path).joinpath(fname + '.xml')
        pages = list()
        collector = lambda x: pages.append(copy.copy(x))
        woordener.parse_xml(path, collector)

        path = Path(self.base_path).joinpath(fname + '-expected.yaml')
        expected = yaml.load(Path(path).read_text(), Loader=yaml.FullLoader)

        return (pages, expected)
