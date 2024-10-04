from typing import Optional

class HTMLNode:

    def __init__(self, 
                 tag: Optional[str] = None,
                 value: Optional[str] = None,
                 children: Optional[list["HTMLNode"]] = None,
                 props: Optional[dict[str, str]] = None) -> "HTMLNode":
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq___(self, other: "HTMLNode") -> bool:
        if self.tag != other.tag:
            return False
        if self.value != other.value:
            return False
        if self.children != other.children:
            return False
        if self.props != other.props:
            return False
        return True

    def __repr__(self) -> str:
        return f'HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})'
        
    def to_html(self) -> str:
        return NotImplemented
    
    def props_to_html(self) -> str:
        if self.props is None:
            return ''
        else:
            return ''.join(f' {p}="{v}"' for p, v in self.props.items())