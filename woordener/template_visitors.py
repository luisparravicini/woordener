import re

#
# https://en.wikipedia.org/wiki/Template:Wikipedia
#


class TemplateVisitor:

    def visit(self, data):
        pass


class TemplateWikipediaVisitor(TemplateVisitor):

    def visit(self, title, data):
        match = re.fullmatch(r'{{(.*?)}}', data)
        if match is None:
            return data

        parts = match.group(1).split('|')
        name = parts[0]
        if len(parts) == 2:
            params = [parts[1]]
        else:
            params = parts[1:]
        params = [x.split('=') for x in params]
        if name != 'wikipedia':
            return data

        lang = params[-1][1]
        if len(params) > 1:
            link_title = params[0][0]
        else:
            link_title = title

        link = f'<a href="https://{lang}.wikipedia.org/wiki/{link_title}">{title}</a>'
        return link


template_visitors = [
    TemplateWikipediaVisitor(),
]
