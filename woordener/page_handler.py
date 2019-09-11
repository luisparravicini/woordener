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
        self.data = list()
        self.page_tags = ['title', 'format', 'text']

    def startElement(self, tag, attributes):
        self.current_tag = tag
        if tag == 'page':
            self.data.clear()
            self.inside_page = True
            self.page.title = None
            self.page.format = None
            self.page.content = None

    def endElement(self, tag):
        if self.inside_page:
            if self.current_tag == 'title':
                self.page.title = self._pop_data()
            elif self.current_tag == 'format':
                self.page.format = self._pop_data()
            elif self.current_tag == 'text':
                self.page.content = self._pop_data()

        if tag == 'page':
            self.collector(self.page)
            self.inside_page = False

        self.current_tag = None

    def characters(self, content):
        if not self.inside_page:
            return

        if self.current_tag in self.page_tags:
            self.data += content

    def _pop_data(self):
        s = ''.join(self.data)
        self.data.clear()
        return s


def parse_xml(path, collector):
    parser = xml.sax.make_parser()
    handler = PageHandler(collector)
    parser.setContentHandler(handler)
    parser.parse('file://' + path.as_posix())
