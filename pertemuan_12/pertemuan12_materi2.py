"""
Nama    : Fateeh Falah Hendharto
NIM     : J0403251070
Kelas   : B
Pertemuan 12 - Materi 2
Topik   : Algoritma Dijkstra
"""

def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Relaksasi berulang
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[weight] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    
    return distances
