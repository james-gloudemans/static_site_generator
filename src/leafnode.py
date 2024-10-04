from typing import Optional

from htmlnode import HTMLNode

class LeafNode(HTMLNode):

    def __init__(self, tag: Optional[str], value: str, props: Optional[dict[str, str]] = None) -> "LeafNode":
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("LeafNode must have a 'value' property")
        if self.tag is None:
            if self.props is not None:
                raise ValueError("LeafNode cannot have 'props' without a 'tag'")
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'