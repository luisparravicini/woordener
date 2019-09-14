import unittest
import woordener


class TestVisitorTitle(unittest.TestCase):

    def test_title_in_list(self):
        items = list()
        for x in woordener.visitors:
            if isinstance(x, woordener.TitleVisitor):
                items.append(x)

        self.assertEqual(len(items), 1)

    def test_levels(self):
        for level in [1, 2, 3, 4, 5, 6]:
            v = woordener.TitleVisitor()
            d = '=' * level
            data = f'{d}Title{d}'
            expected = f'<h{level}>Title</h{level}>'
            self.assertEqual(v.visit(data), expected)

    def test_without_ending_equals(self):
        v = woordener.TitleVisitor()
        data = '=Title'
        self.assertIsNone(v.visit(data))
