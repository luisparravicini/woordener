import xml.sax
from dataclasses import dataclass


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
