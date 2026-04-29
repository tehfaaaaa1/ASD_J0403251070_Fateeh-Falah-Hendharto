"""
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B1

Latihan 2 : Studi kasus DFS
"""


def dfs(graph, node, visited: set):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


test_graph = {
    'A': ['B', 'C'],
    'B': ['E', 'D'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

print("DFS dari A:")
dfs(test_graph, 'A', set())


# Pertanyaan Analisis
# 1. Mengapa DFS masuk ke node terdalam terlebih dahulu?
# 2. Apa yang terjadi jika urutan neighbor diubah?
# 3. Bandingkan hasil DFS dengan BFS pada graph yang sama.

# 1. Karena prinsipnya DFS itu berupa stack. Ketika sudah sampai
#    ujung node (tidak ada hubungan), algoritma akan kembali mencari
#    di tetangga lain.

# 2. Urutan tetangga node-nya pun akan berubah.
# Hasil awal:
# DFS dari A:
# A B D E C F
# Hasil modifikasi:
# DFS dari A:
# A B E D C F

# 3. Hasilnya berbeda.
# BFS dari A:
# A B C D E F
# DFS dari A:
# A B D E C F
