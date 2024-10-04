from typing import Optional

from htmlnode import HTMLNode

class ParentNode(HTMLNode):

    def __init__(self, tag: str, children: list["HTMLNode"], props: Optional[dict[str, str]] = None) -> "ParentNode":
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError('ParentNode must have a tag')
        if self.children is None:
            raise ValueError('ParentNode must have children')
        inner_html = ''.join(c.to_html() for c in self.children)
        return f'<{self.tag}{self.props_to_html()}>{inner_html}</{self.tag}>'