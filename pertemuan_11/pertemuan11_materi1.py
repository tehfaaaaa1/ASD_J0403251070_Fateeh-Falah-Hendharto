"""
Implementasi Dasar Graph
"""

test_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C'],
}

for vertex, edge in test_graph.items():
    print(vertex, "->", edge)
