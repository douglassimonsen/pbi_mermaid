from enum import Enum
from dataclasses import dataclass


@dataclass
class Shape:
    start: str
    end: str


class NodeShape(Enum):
    normal = Shape("[", "]")
    round_edge = Shape("(", ")")
    stadium_shape = Shape("([", "])")
    subroutine_shape = Shape("[[", "]]")
    cylindrical = Shape("[(", ")]")
    circle = Shape("((", "))")
    label_shape = Shape(">", "]")
    rhombus = Shape("{", "}")
    hexagon = Shape("{{", "}}")
    parallelogram = Shape("[/", "/]")
    parallelogram_alt = Shape("[\\", "\\]")
    trapezoid = Shape("[/", "\\]")
    trapezoid_alt = Shape("[\\", "/]")
    double_circle = Shape("(((", ")))")


class Node:
    id: str
    shape: Shape
    content: str

    def __init__(self, id: str, shape: NodeShape=NodeShape.normal, content: str="") -> None:
        self.id = id
        self.shape = shape.value
        self.content = content

    def to_markdown(self) -> str:
        return f"{self.id}{self.shape.start}\"{self.content or self.id}\"{self.shape.end}"