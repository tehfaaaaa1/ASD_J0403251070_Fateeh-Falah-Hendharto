"""
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B1

Latihan 1 : Studi kasus BFS
"""

from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


test_graph = {
    'rumah': ['sekolah', 'toko'],
    'sekolah': ['perpustakaan'],
    'toko': ['pasar'],
    'perpustakaan': [],
    'pasar': []
}

print("BFS dari Rumah:")
bfs(test_graph, 'rumah')


# Pertanyaan Analisis
# 1. Node mana yang dikunjungi pertama?
# 2. Mengapa BFS cocok untuk mencari jalur terdekat?
# 3. Apa perbedaan urutan BFS jika struktur graph diubah?

# 1. Rumah karena dimulai dari node rumah

# 2. Karena BFS menelusuri secara per-level, jadi jika sudah
#    ketemu sebuah node, akan dihentikan.

# 3. Terdapat perbedaan.
# Graph awal
# BFS dari Rumah:
# rumah sekolah toko perpustakaan pasar

# Graph setelah edge pasar ditambah ke rumah
# BFS dari Rumah:
# rumah sekolah toko pasar perpustakaan
