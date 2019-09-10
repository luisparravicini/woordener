import wikitextparser as wtp
from .page_handler import parse_xml


class SectionFormatError(Exception):
    def __init__(self, title, format):
        self.title = title
        self.format = format


def extract_section(data):
    doc = wtp.parse(data)
    sections = [x for x in doc.sections if x.title == 'Dutch']

    result = None
    if len(sections) > 0:
        result = sections[0].contents
    return result


def extract(path, collector):
    c = lambda x: _prepare_section(x, collector)
    parse_xml(path, c)


def _prepare_section(page, collector):
    title = page.title
    f = page.format
    if f != 'text/x-wiki':
        raise SectionFormatError(title, f)
    section = extract_section(page.content)
    if section is not None:
        collector(title, section)
