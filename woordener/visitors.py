import re

class Visitor:
    def _accept(self, data):
        return False

    def visit(self, data):
        if not self._accept(data):
            return None

        return self._do_visit(data)


class TitleVisitor(Visitor):
    def _accept(self, data):
        self.match = re.fullmatch(r'(=+)([^=]+)=+', data)
        return (self.match is not None)

    def _do_visit(self, data):
        level = len(self.match.group(1))
        title = self.match.group(2)
        return f'<h{level}>{title}</h{level}>'


class DefaultVisitor(Visitor):
    def _accept(self, data):
        return True

    def _do_visit(self, data):
        return data


visitors = [
    TitleVisitor(),
    DefaultVisitor(),
]
