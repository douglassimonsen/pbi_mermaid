from mermaid import Link, MermaidDiagram, Node

n1 = Node("hi", style="fill:#f9f,stroke:#333,stroke-width:4px")
n2 = Node("bye")
link = Link(n1, n2)
diagram = MermaidDiagram([n1, n2], [link])
print(diagram.show())
