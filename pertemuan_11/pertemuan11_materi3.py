"""
Implementasi DFS
"""


def dfs(graph, node, visited: set):
    """
    Fungsi untuk menelusuri graph menggunakan DFS\n
    Graph: Dictionary yang menyimpang graph\n
    Node: Menyimpan node yang sedang dikunjungi\n
    Visited: Menyimpan node yang sudah dikunjungi
    """

    # Tandai node saat ini sebagai node yang sudah dikunjungi
    visited.add(node)
    # Tampilkan node yang sedang dikunjungi
    print(node, end=" ")

    # Periksa semua tetangga dari node saat ini
    for neighbor in graph[node]:
        # Jika tetangga belum pernah dikunjungi,
        # Lakukan dfs secara rekursif ke tetangga tersebut
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


test_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

dfs(test_graph, "A", set())
