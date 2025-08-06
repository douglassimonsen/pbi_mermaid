from mermaid import Node, Link, MermaidDiagram

n1 = Node("hi")
n2 = Node("bye")
l = Link(n1, n2)
x = MermaidDiagram(
    [n1, n2],
    [l]
)
print(x.to_markdown())