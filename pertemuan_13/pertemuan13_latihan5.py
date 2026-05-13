"""
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B1
Praktikum 13 - Graph III: Spanning Tree

Kasus 1 . Jaringan Jalan Antar Kota
Bogor - Jakarta = 5
Bogor - Depok = 2
Depok - Jakarta = 3
Jakarta - Bandung = 6
Depok - Bandung = 4

Ketentuan Program. Program harus memuat:
1. Representasi weighted graph.
2. Implementasi Kruskal atau Prim.
3. Output MST.
4. Output total bobot minimum.
5. Komentar penjelasan program.
"""

# ==========================================================
# Implementasi Kruskal
# ==========================================================

# Daftar edge: (bobot, vertex 1, vertex 2)
edges = [
    (2, 'Bo', 'D'),
    (3, 'D', 'J'),
    (4, 'D', 'Ba'),
    (5, 'Bo', 'J'),
    (6, 'J', 'Ba')
]

# Mengurutkan edge berdasarkan bobot
# Inisialisasi list Minimum Spanning Tree dan Total Bobot
edges.sort()
mst = []
total_weight = 0

# Set sederhana untuk menyimpan node yang sudah dipilih.
# Set digunakan agar tidak ada value duplikat.
connected = set()
# Loop isi list edges
for weight, u, v in edges:
    # Jika edge tidak membentuk cycle sederhana,
    # 1. Tambahkan ke MST
    # 2. Jumlahkan total bobot dengan bobot edge
    # 3. Tambahkan vertex awal dan vertex tetangga
    # ke set connected.
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
# 1. Kasus apa yang dipilih?
# 2. Algoritma apa yang digunakan?
# 3. Edge mana saja yang dipilih dalam MST?
# 4. Berapa total bobot MST?
# 5. Mengapa edge tertentu tidak dipilih?

# Jawaban:
# 1. Kasus 1: jaringan jalan antar kota
# 2. Kruskal's Algorithm
# 3. Bogor - Depok, Depok - Jakarta, Depok - Bandung
# 4. 9
# 5. Karena kita mencari edge yang paling kecil agar total bobot
# minimal.
