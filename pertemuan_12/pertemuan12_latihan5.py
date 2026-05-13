"""
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B
Pertemuan 12 - Graph II: Shortest Path
"""

# ==========================================================
# Latihan 5: Studi Kasus dengan Program Shortest Path
# Algoritma: Dijkstra
# ==========================================================

import heapq


def dijkstra(graph, start):
    # Menyimpan jarak minimum / infinite
    distances = {node: float('inf') for node in graph}

    # Jarak Node Awal = 0
    distances[start] = 0

    # Priority Queue
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

    # Periksa semua tetangga
    for neighbor, weight in graph[current_node].items():
        distance = current_distance + weight

        # Jika ditemukan jarak lebih kecil
        if distance < distances[neighbor]:
            distances[neighbor] = distance
            heapq.heappush(pq, (distance, neighbor))

    return distances


# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
test_graph = {
    'bogor': {'jakarta': 5, 'depok': 2},
    'depok': {'jakarta': 2, 'bandung': 6},
    'jakarta': {'bandung': 7},
    'bandung': {}
}

hasil = dijkstra(test_graph, 'bogor')
print("Jarak terpendek dari Bogor:")
for lokasi, jarak in hasil.items():
    print("Bogor ->", lokasi, "=", jarak)

# Jawaban Analisis:
# 1. Node awal yang digunakan apa?
# Bogor
# 2. Node mana yang memiliki jarak paling kecil dari node awal?
# Depok
# 3. Node mana yang memiliki jarak paling besar dari node awal?
# Jakarta
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
# Cara kerjanya seperti algoritma biasa:
# 1. Tentukan node awal
# 2. Beri jarak awal:
#   - node awal = 0
#   - node lain = tak hingga (∞)
# 3. Pilih node dengan jarak terkecil
# 4. Perbarui jarak tetangganya
# 5. Tandai node sebagai selesai diproses
# 6. Ulangi sampai semua node selesai
# Dengan studi kasus yang diangkat, algoritma berusaha mencari jarak antar kota
# yang terdekat.
