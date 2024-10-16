import itertools
import re
from typing import Iterator

from textnode import TextNode

def text_to_textnodes(text: str) -> list[TextNode]:
    result: list[TextNode] = [TextNode(text, 'text'),]
    result = split_nodes_delimiter(result, '**')
    result = split_nodes_delimiter(result, '*')
    result = split_nodes_delimiter(result, '`')
    result = split_nodes_image(result)
    result = split_nodes_link(result)
    return result

def split_nodes_delimiter(nodes: list[TextNode], sep: str) -> list[TextNode]:
    """Takes a list of nodes and splits them into a new list of nodes based on `sep`

    Args:
        nodes (list[TextNode]): list of nodes to be split
        sep (str): separator used to split the nodes

    Returns:
        list[TextNode]: list mixing different types of text nodes based on `sep`
    """
    result: list[TextNode] = list()
    for node in nodes:
        if node.text_type != 'text':
            result.append(node)
            continue
        if sep == '*':
            # This matches exactly one `*` and not `**`
            sections = re.split(r'(?<!\*)\*(?!\*)', node.text)
        else:
            sections = node.text.split(sep)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for text_type, text in zip(itertools.cycle(('text', node._text_type_sep[sep])), sections):
            if text:
                result.append(TextNode(text, text_type))
    return result


## Below is from the Solution on boot.dev.  It fails two of the tests.
# def split_nodes_delimiter(old_nodes, delimiter):
#     new_nodes = []
#     for old_node in old_nodes:
#         if old_node.text_type != 'text':
#             new_nodes.append(old_node)
#             continue
#         split_nodes = []
#         sections = old_node.text.split(delimiter)
#         if len(sections) % 2 == 0:
#             raise ValueError("Invalid markdown, formatted section not closed")
#         for i in range(len(sections)):
#             if sections[i] == "":
#                 continue
#             if i % 2 == 0:
#                 split_nodes.append(TextNode(sections[i], 'text'))
#             else:
#                 split_nodes.append(TextNode(sections[i], old_node._text_type_sep[delimiter]))
#         new_nodes.extend(split_nodes)
#     return new_nodes

def split_nodes_image(nodes: list[TextNode]) -> list[TextNode]:
    result: list[TextNode] = list()
    for node in nodes:
        if node.text_type != 'text':
            result.append(node)
            continue
        prev_match: int = 0
        for match in extract_markdown_images(node.text):
            if match.start() > 0 and match.start() != prev_match:
                result.append(TextNode(node.text[prev_match:match.start()], 'text'))
            result.append(TextNode(match.groups()[0], 'image', match.groups()[1]))
            prev_match = match.end()
        if prev_match != len(node.text):
            result.append(TextNode(node.text[prev_match:], 'text'))
    return result

def split_nodes_link(nodes: list[TextNode]) -> list[TextNode]:
    result: list[TextNode] = list()
    for node in nodes:
        if node.text_type != 'text':
            result.append(node)
            continue
        prev_match: int = 0
        for match in extract_markdown_links(node.text):
            if match.start() > 0 and match.start() != prev_match:
                result.append(TextNode(node.text[prev_match:match.start()+1], 'text'))
            result.append(TextNode(match.groups()[0], 'link', match.groups()[1]))
            prev_match = match.end()
        if prev_match != len(node.text):
            result.append(TextNode(node.text[prev_match:], 'text'))
    return result

def extract_markdown_images(text: str) -> Iterator[re.Match]:
    return re.finditer(r'!\[([\w\s]+)\]\(([^\)]+)\)', text)

def extract_markdown_links(text: str) -> Iterator[re.Match]:
    return re.finditer(r'[^!]{0,1}\[([\w\s]+)\]\(([^\)]+)\)', text)