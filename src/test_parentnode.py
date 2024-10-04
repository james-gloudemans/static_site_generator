import unittest

from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):

    def test_to_html_no_children(self):
        node = ParentNode('p', None)
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

    def test_to_html_nested_parent_nodes(self):
        node1 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        node2 = LeafNode("a", "Link", {"href": "https://www.google.com"})
        node3 = ParentNode("p", [node1, node2])
        self.assertEqual(node3.to_html(), '<p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><a href="https://www.google.com">Link</a></p>')