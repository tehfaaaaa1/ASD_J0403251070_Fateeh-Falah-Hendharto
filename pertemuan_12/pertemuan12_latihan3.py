"""
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B
Pertemuan 12 - Materi 1
Topik   : Algoritma Dijkstra
"""

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

test_graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {},
}
hasil = dijkstra(test_graph, "A")
print(hasil)
