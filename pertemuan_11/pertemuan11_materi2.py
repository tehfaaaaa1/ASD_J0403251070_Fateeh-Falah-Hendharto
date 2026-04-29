"""
Implementasi BFS
"""

from collections import deque


def bfs(graph, start):
    """
    Fungsi untuk melakukan penelusuran graph dengan BFS\n
    Graph: Dictionary yang menyimpan struktur dari graph\n
    Start: Node awal penelusuran
    """

    # Queue untuk menyimpan node yang akan diproses
    queue = deque()
    # Variabel untuk menyimpan node yang sudah diproses
    visited = set()

    # Masukkan node awal ke queue
    queue.append(start)

    # Tandai node awal sebagai node yang sudah dikunjungi
    visited.add(start)

    while queue:
        # Ambil node paling depan dari queue
        node = queue.popleft()

        # Tampilkan node yang sedang dikunjungi
        print(node, end=" ")
        # periksa semua tetangga dari node yang diambil
        for neighbor in graph[node]:
            # jika tetangga belum dikunjungi
            if neighbor not in visited:
                # tandai tetangga sebagai sudah dikunjungi
                visited.add(neighbor)
                # masukkan tetangga ke queue untuk diproses selanjutnya
                queue.append(neighbor)


test_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# menjalankan BFS dari node A
bfs(test_graph, 'A')
