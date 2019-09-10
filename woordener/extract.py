import wikitextparser as wtp
from .page_handler import parse_xml

class SectionFormatError(Exception):
    pass

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
    if page.format != 'text/x-wiki':
        raise SectionFormatError()
    collector(page)
