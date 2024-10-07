import functools
import unittest

from textnode import TextNode
from split_nodes import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_code_centered(self):
        node = TextNode("This is text with a `code block` word", 'text')
        result = [
            TextNode("This is text with a ", 'text'),
            TextNode("code block", 'code'),
            TextNode(" word", 'text'),
        ]
        self.assertListEqual(split_nodes_delimiter([node,], '`'), result)

    def test_bold_centered(self):
        node = TextNode("This is text with a **bold** word", 'text')
        result = [
            TextNode("This is text with a ", 'text'),
            TextNode("bold", 'bold'),
            TextNode(" word", 'text'),
        ]
        self.assertListEqual(split_nodes_delimiter([node,], '**'), result)

    def test_italic_centered(self):
        node = TextNode("This is text with an *italic* word", 'text')
        result = [
            TextNode("This is text with an ", 'text'),
            TextNode("italic", 'italic'),
            TextNode(" word", 'text'),
        ]
        self.assertListEqual(split_nodes_delimiter([node,], '*'), result)

    def test_multiple_all_same(self):
        node = TextNode("This text has *two* italic *words* omg", 'text')
        result = [
            TextNode("This text has ", 'text'),
            TextNode("two", 'italic'),
            TextNode(" italic ", 'text'),
            TextNode("words", 'italic'),
            TextNode(" omg", 'text')
        ]
        self.assertListEqual(split_nodes_delimiter([node,], '*'), result)

    def test_split_at_beginning(self):
        node = TextNode("*This* text has an italic word at the beginning", 'text')
        result = [
            TextNode("This", 'italic'),
            TextNode(" text has an italic word at the beginning", 'text')
        ]
        self.assertListEqual(split_nodes_delimiter([node,], '*'), result)

    def test_split_at_end(self):
        node = TextNode("This text has an italic word at the *end*", 'text')
        result = [
            TextNode("This text has an italic word at the ", 'text'),
            TextNode("end", 'italic')
        ]
        self.assertListEqual(split_nodes_delimiter([node,], '*'), result)

    def test_split_with_other_type(self):
        node = TextNode("This text has both a **bold** and an *italic* word", 'text')
        result = [
            TextNode("This text has both a **bold** and an ", 'text'),
            TextNode("italic", 'italic'),
            TextNode(" word", 'text')
        ]
        self.assertListEqual(split_nodes_delimiter([node,], '*'), result)

    def test_split_with_other_type_nearby(self):
        node = TextNode("This text has **bold** *and italic* pieces next to each other", 'text')
        result = [
            TextNode("This text has **bold** ", 'text'),
            TextNode("and italic", 'italic'),
            TextNode(" pieces next to each other", 'text')
        ]
        self.assertListEqual(split_nodes_delimiter([node,], '*'), result)

    def test_split_with_multiple_input_nodes(self):
        nodes = [
            TextNode("This is *node* 1", 'text'),
            TextNode("This is *node* 2", 'text')
        ]
        result = [
            TextNode("This is ", 'text'),
            TextNode("node", 'italic'),
            TextNode(" 1", 'text'),
            TextNode("This is ", 'text'),
            TextNode("node", 'italic'),
            TextNode(" 2", 'text')
        ]
        self.assertListEqual(split_nodes_delimiter(nodes, '*'), result)

    def test_invalid_markdown(self):
        node = TextNode("This is invalid *markdown", 'text')
        split_nodes_callable = functools.partial(split_nodes_delimiter, nodes=[node,], sep='*')
        self.assertRaises(ValueError, split_nodes_callable)
