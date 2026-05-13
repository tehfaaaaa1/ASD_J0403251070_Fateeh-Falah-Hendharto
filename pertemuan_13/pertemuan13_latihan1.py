"""
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B1
Praktikum 13 - Graph III: Spanning Tree
"""

# Daftar edge graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D'),
]

# Contoh Spanning Tree
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B'),
]

print("Edge pada graph:")
for edge in edges:
    print(edge)

print('\nSpanning Tree:')
for edge in spanning_tree:
    print(edge)

print('\nJumlah edge graph:', len(edges))
print('Jumlah edge spanning tree:', len(spanning_tree))

# Jawaban Analisis:
# 1. Apa perbedaan graph awal dan spanning tree?
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?

# Jawab:
# 1. Jumlah edge yang digunakan spanning tree lebih sedikit
# daripada graph awal.
# 2. Karena menjadi tidak efisien dan menambah overhead
# maintenance.
# 3. Karena tidak ada vertex yang edge-nya siklus, jadi
# hanya ada jalan lurus
