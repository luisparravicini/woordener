import unittest
import xml.sax
from pathlib import Path
from dataclasses import dataclass
import copy
import yaml


@dataclass
class Page:
    title: str = None
    format: str = None
    content: str = None


class PageHandler(xml.sax.ContentHandler):
    def __init__(self, collector):
        self.current_tag = None
        self.inside_page = False
        self.page = Page()
        self.collector = collector

    def startElement(self, tag, attributes):
        self.current_tag = tag
        if tag == 'page':
            self.inside_page = True
            self.page.title = ''
            self.page.format = ''
            self.page.content = ''

    def endElement(self, tag):
        if tag == 'page':
            self.collector(self.page)
            self.inside_page = False

        self.current_tag = None

    def characters(self, content):
        if not self.inside_page:
            return

        if self.current_tag == 'title':
            self.page.title += content
        elif self.current_tag == 'format':
            self.page.format += content
        elif self.current_tag == 'text':
            self.page.content += content


def parse_xml(path, collector):
    parser = xml.sax.make_parser()
    handler = PageHandler(collector)
    parser.setContentHandler(handler)
    parser.parse('file://' + path.as_posix())


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
        parse_xml(path, collector)

        path = Path(self.base_path).joinpath(fname + '-expected.yaml')
        expected = yaml.load(Path(path).read_text(), Loader=yaml.FullLoader)

        return (pages, expected)


if __name__ == '__main__':
    unittest.main()
