from enum import StrEnum
from typing import Sequence
from .node import Node
from .link import Link


class Orientation(StrEnum):
    default = ""
    top_to_bottom = "TB"
    top_down = "TD"
    bottom_to_top = "BT"
    right_to_left = "RL"
    left_to_right = "LR"

class MermaidDiagram:
    title: str = ""
    nodes: list[Node]
    links: list[Link]
    orientation: Orientation

    def __init__(self, nodes: list[Node], links: list[Link], title: str="", orientation: Orientation=Orientation.default) -> None:
        self.title = title
        self.nodes = nodes
        self.links = links
        self.orientation = orientation

    def to_markdown(self) -> str:
        node_text = "\n".join(
            n.to_markdown()
            for n in self.nodes
        )
        link_text = "\n".join(
            l.to_markdown()
            for l in self.links
        )
        header = f"---\ntitle: {self.title}\n---" if self.title else ""
        graph_defines = f"graph {self.orientation}"
        return f"{header}\n{graph_defines}\n{node_text}\n{link_text}"