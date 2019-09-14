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
        data = f'{{{{wikipedia|lang={lang}}}}}'
        title = 'woordenboek'
        expected = f'<a href="https://wikipedia.org/wiki/{lang}:{title}">{title}</a>'
        v = woordener.TemplateWikipediaVisitor()
        self.assertEqual(v.visit(title, data), expected)

    def test_another_word(self):
        lang = 'nl'
        title = 'lens'
        template_title = 'lens (optiek)'
        data = f'{{{{wikipedia|{template_title}|lang={lang}}}}}'
        expected = f'<a href="https://wikipedia.org/wiki/{lang}:{template_title}">{title}</a>'
        v = woordener.TemplateWikipediaVisitor()
        self.assertEqual(v.visit(title, data), expected)
