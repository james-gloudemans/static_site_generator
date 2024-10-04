import unittest

from leafnode import LeafNode
from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_when_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a different text node", "bold")
        self.assertNotEqual(node, node2)

    def test_eq_when_not_eq_url_is_none(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", "Not None")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        text = 'This is text'
        type = 'text'
        url = 'This is url'
        node = TextNode(text, type, url)
        self.assertEqual(repr(node), f'TextNode({text}, {type}, {url})')
    
    def test_repr_url_is_none(self):
        text = 'This is text'
        type = 'text'
        node = TextNode(text, type)
        self.assertEqual(repr(node), f'TextNode({text}, {type}, None)')

    def test_to_html_node_text(self):
        node = TextNode('Plain text', 'text')
        self.assertEqual(node.to_html_node().to_html(), 'Plain text')

    def test_to_html_node_bold(self):
        node = TextNode('Bolded text', 'bold')
        self.assertEqual(node.to_html_node().to_html(), '<b>Bolded text</b>')

    def test_to_html_node_italic(self):
        node = TextNode('Italic text', 'italic')
        self.assertEqual(node.to_html_node().to_html(), '<i>Italic text</i>')

    def test_to_html_node_code(self):
        node = TextNode('Some code', 'code')
        self.assertEqual(node.to_html_node().to_html(), '<code>Some code</code>')

    def test_to_html_node_link(self):
        node = TextNode('Link text', 'link', 'https://www.google.com')
        self.assertEqual(node.to_html_node().to_html(), '<a href="https://www.google.com">Link text</a>')

    def test_to_html_node_link_no_url(self):
        node = TextNode('Link text', 'link')
        self.assertRaises(ValueError, node.to_html_node)

    def test_to_html_node_image(self):
        node = TextNode('alt text', 'image', 'https://www.google.com')
        self.assertEqual(node.to_html_node().to_html(), '<img src="https://www.google.com" alt="alt text"></img>')

    def test_to_html_node_image_no_url(self):
        node = TextNode('alt text', 'image')
        self.assertRaises(ValueError, node.to_html_node)

if __name__ == "__main__":
    unittest.main()