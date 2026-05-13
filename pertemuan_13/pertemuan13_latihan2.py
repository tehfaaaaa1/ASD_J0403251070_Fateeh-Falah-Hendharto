"""
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B1
Praktikum 13 - Graph III: Spanning Tree
"""

# ==========================================================
# Implementasi Kruskal
# ==========================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot
edges.sort()
mst = []
total_weight = 0

# Set sederhana untuk node yang sudah dipilih
connected = set()
for weight, u, v in edges:
    # Jika edge tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)


print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total_weight)

# Jawaban Analisis:
# 1. Edge mana yang dipilih pertama kali?
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
# 3. Berapa total bobot MST yang dihasilkan?
# 4. Mengapa edge tertentu tidak dipilih?

# Jawab:
# 1. C -- D.
# 2. Karena untuk mencari jarak atau total bobot minimal.
# 3. 6
# 4. Karena total bobot akan menjadi terlalu berat.
