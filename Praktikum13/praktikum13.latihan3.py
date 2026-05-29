# Nama :    Ahmad Abian Hakim
# NIM :     J0403251069
# Kelas :   TPL A2
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Latihan 3: Implementasi Algoritma Prim
# ==========================================================

import heapq

graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    visited = set([start])
    edges = []

    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    while edges:
        weight, u, v = heapq.heappop(edges)

        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight


mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total)


# Jawaban Analisis:
#
# 1. Node awal apa yang digunakan?
#    Jawaban:
#    Node awal yang digunakan adalah A.
#
# 2. Edge mana yang dipilih pertama kali?
#    Jawaban:
#    Edge pertama yang dipilih adalah A-C dengan bobot 2 karena
#    merupakan edge dengan bobot terkecil dari node A.
#
# 3. Bagaimana Prim menentukan edge berikutnya?
#    Jawaban:
#    Prim memilih edge dengan bobot paling kecil yang menghubungkan
#    node yang sudah dikunjungi dengan node yang belum dikunjungi.
#
# 4. Berapa total bobot MST yang dihasilkan?
#    Jawaban:
#    Total bobot MST yang dihasilkan adalah 6.
#
# 5. Apa perbedaan pendekatan Prim dan Kruskal?
#    Jawaban:
#    Prim membangun MST mulai dari satu node awal dan memperluas tree
#    secara bertahap. Sedangkan Kruskal memilih edge dengan bobot
#    terkecil dari seluruh graph tanpa bergantung pada node awal.