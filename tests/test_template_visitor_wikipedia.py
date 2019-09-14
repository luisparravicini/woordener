import unittest
import woordener


class TestTemplateVisitorTitle(unittest.TestCase):

    def test_title_in_list(self):
        items = list()
        for x in woordener.template_visitors:
            if isinstance(x, woordener.TemplateWikipediaVisitor):
                items.append(x)

        self.assertEqual(len(items), 1)

    def test_only_lang(self):
        lang = 'nl'
        title = 'woordenboek'
        data = f'{{{{wikipedia|lang={lang}}}}}'
        self.assertVisitor(title, title, lang, data)

    def test_another_word(self):
        lang = 'nl'
        title = 'lens'
        template_title = 'lens (optiek)'
        data = f'{{{{wikipedia|{template_title}|lang={lang}}}}}'
        self.assertVisitor(title, template_title, lang, data)

    def assertVisitor(self, title, template_title, lang, data):
        expected = f'<a href="https://wikipedia.org/wiki/{lang}:{template_title}">{title}</a>'
        v = woordener.TemplateWikipediaVisitor()
        self.assertEqual(v.visit(title, data), expected)
