from .node import Node
from enum import StrEnum


class LinkShape(StrEnum):
    normal = "---"
    dotted = "-.-"
    thick = "==="


class LinkHead(StrEnum):
    none = ""
    arrow = ">"
    left_arrow = "<"
    bullet = "o"
    cross = "x"


class Link: 
    from_node: Node
    to_node: Node
    from_head: str
    to_head: str
    link_shape: LinkShape

    def __init__(self, from_node: Node, to_node: Node, from_head: LinkHead=LinkHead.none, to_head: LinkHead=LinkHead.arrow, link_shape: LinkShape=LinkShape.normal) -> None:
        self.from_node = from_node
        self.to_node = to_node
        self.from_head = from_head
        self.to_head = to_head
        self.link_shape = link_shape

    def to_markdown(self) -> str:
        return f"{self.from_node.id} {self.from_head}{self.link_shape}{self.to_head} {self.to_node.id}"