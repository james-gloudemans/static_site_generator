import unittest

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
        type = 'This is type'
        url = 'This is url'
        node = TextNode(text, type, url)
        self.assertEqual(repr(node), f'TextNode({text}, {type}, {url})')
    
    def test_repr_url_is_none(self):
        text = 'This is text'
        type = 'This is type'
        node = TextNode(text, type)
        self.assertEqual(repr(node), f'TextNode({text}, {type}, None)')


if __name__ == "__main__":
    unittest.main()