from mermaid import Node, Link, MermaidDiagram

n1 = Node("hi", style="fill:#f9f,stroke:#333,stroke-width:4px")
n2 = Node("bye")
l = Link(n1, n2)
x = MermaidDiagram(
    [n1, n2],
    [l]
)
print(x.to_markdown())