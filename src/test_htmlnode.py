import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode('tag', 'value', ['child1', 'child2'], {'prop1':'val1', 'prop2':'val2'})
        self.assertEqual(repr(node), "HTMLNode(tag=tag, value=value, children=['child1', 'child2'], props={'prop1': 'val1', 'prop2': 'val2'})")

    def test_props_to_html(self):
        node = HTMLNode(None, None, None, {'href': 'https://www.google.com', 'target': '_blank'})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_props_to_html_props_is_none(self):
        node = HTMLNode(None, None, None, None)
        self.assertEqual(node.props_to_html(), "")
        