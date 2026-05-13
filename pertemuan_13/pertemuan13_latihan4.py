"""
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B1
Praktikum 13 - Graph III: Spanning Tree

Deskripsi Kasus

Sebuah kampus ingin membangun jaringan kabel internet antar gedung dengan biaya
minimum. Setiap hubungan antar gedung memiliki biaya pemasangan kabel yang
berbeda. Data hubungan gedung:

GedungA - GedungB = 4
GedungA - GedungC = 2
GedungB - GedungD = 3
GedungC - GedungD = 1
GedungA - GedungD = 5

Buatlah program menggunakan algoritma Prim atau Kruskal untuk menentukan
jaringan kabel dengan total biaya minimum. Ketentuan Program harus memuat:
• Representasi weighted graph.
• Implementasi Prim atau Kruskal.
• Output edge yang dipilih.
• Output total biaya minimum.
• Komentar penjelasan program.
"""

# ==========================================================
# Implementasi Prim
# ==========================================================

# Priority queue algorithm agar elemen terkecil selalu
# ada di root / index 0
import heapq

# Variabel studi kasus
gedung = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}


def prim(graph, start):
    "Prim's Algorithm to find Minimum Spanning Tree"
    # Inisialisasi vertex yang telah dikunjungi
    visited = set([start])

    # Inisialisasi list untuk menentukan total minimum
    edges = []

    # Masukkan semua tetangga vertex ke dalam list edges
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    # List untuk menyimpan Minimum Spanning Tree
    mst = []

    # Bobot total awal
    total_weight = 0

    # Untuk setiap tetangga dalam list edges,
    # loop program berikut
    while edges:

        # Pop / delete sebuah edge dan simpan value/bobotnya
        weight, u, v = heapq.heappop(edges)

        # Jika tetangga belum dikunjungi,
        # 1. Tambahkan ke "visited".
        # 2. Masukkan vertex dan edge tersebut ke dalam
        # variabel MST.
        # 3. Tambahkan total_weight dengan bobot edge tadi.
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

            # Cek semua opsi edge,
            # lalu pilih tetangga dengan bobot terkecil.
            # Jangan masukkan tetangga yang sudah dikunjungi
            # agar tidak cycle.
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight


mst, total = prim(gedung, 'A')
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total bobot =", total)

# Jawaban Analisis:
# 1. Algoritma apa yang digunakan?
# 2. Edge mana saja yang dipilih?
# 3. Berapa total biaya minimum?
# 4. Mengapa MST cocok digunakan pada kasus ini?

# Jawaban:
# 1. Algoritma Prim
# 2. A - C, C - D, D - B
# 3. 6
# 4. Agar biaya jaringan internet antargedung diminamilisir.
