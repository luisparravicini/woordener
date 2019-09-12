import wikitextparser as wtp
from .page_handler import parse_xml
import re


def extract_section(data):
    result = None
    m = re.search(r'==Dutch==\s*(.+?)(?:\s+==[^=]|$)', data, re.DOTALL)
    if m is not None:
        result = m.group(1)

    return result


def extract(path, collector):
    c = lambda x: _prepare_section(x, collector)
    parse_xml(path, c)


def _prepare_section(page, collector):
    if page.format == 'text/x-wiki':
        section = extract_section(page.content)
        if section is not None:
            collector(page.title, section)
