from typing import Optional

from htmlnode import HTMLNode
from leafnode import LeafNode

class TextNode:

    _text_types: set[str] = set((
        'text',
        'bold',
        'italic',
        'code',
        'link',
        'image',
    ))

    _text_type_sep: dict[str, str] = {
        '**': 'bold',
        '*': 'italic',
        '`': 'code',
    }

    def __init__(self, text: str, text_type: str, url: Optional[str] = None) -> "TextNode":
        self.text = text
        if text_type not in self._text_types:
            raise ValueError(f'text_type {text_type} for TextNode not found in: {self._text_types}')
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: "TextNode") -> bool:
        if self.text != other.text:
            return False
        if self.text_type != other.text_type:
            return False
        if self.url != other.url:
            return False
        return True
    
    def __repr__(self) -> str:
        return f'TextNode({self.text}, {self.text_type}, {self.url})'
    
    def to_html_node(self) -> HTMLNode:
        match self.text_type:
            case 'text':
                return LeafNode(None, self.text)
            case 'bold':
                return LeafNode('b', self.text)
            case 'italic':
                return LeafNode('i', self.text)
            case 'code':
                return LeafNode('code', self.text)
            case 'link':
                if self.url is None:
                    raise ValueError('Attempted to convert TextNode of type link with no url')
                return LeafNode('a', self.text, {'href': self.url})
            case 'image':
                if self.url is None:
                    raise ValueError('Attempted to convert TextNode of type image with no url')
                return LeafNode('img', '', {'src': self.url, 'alt': self.text})
        return HTMLNode()