import itertools
import re

from textnode import TextNode

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
            sections = re.split(r'(?<!\*)\*(?!\*)', node.text)
        else:
            sections = node.text.split(sep)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for text_type, text in zip(itertools.cycle(('text', node._text_type_sep[sep])), sections):
            if text:
                result.append(TextNode(text, text_type))
    return result