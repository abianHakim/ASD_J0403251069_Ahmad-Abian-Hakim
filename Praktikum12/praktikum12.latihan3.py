# Nama : Ahmad Abian Hakim
# NIM  : J0403251069
# Kelas: TPL-A2
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):

        # Periksa semua edge
        for node in graph:

            for neighbor, weight in graph[node].items():

                # Jika jarak ke node saat ini sudah diketahui,
                # dan ditemukan jarak yang lebih kecil ke neighbor,
                # maka lakukan update jarak
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:

                    distances[neighbor] = distances[node] + weight

    return distances


# Menjalankan fungsi Bellman-Ford dari node A
hasil = bellman_ford(graph, 'A')

# Menampilkan hasil jarak terpendek
print("Jarak terpendek dari node A:")

for node, distance in hasil.items():
    print(node, "=", distance)


# Jawaban Analisis:
# 1. Bobot langsung dari A ke B adalah 5.

# 2. Total bobot jalur A -> C -> B adalah 2.
#    Didapat dari 4 + (-2) = 2.

# 3. Jalur yang menghasilkan jarak lebih kecil menuju B
#    adalah jalur A -> C -> B karena total bobotnya 2,
#    lebih kecil dibanding jalur langsung A -> B yaitu 5.

# 4. Bellman-Ford dapat digunakan pada graph dengan
#    bobot negatif karena algoritma ini melakukan
#    relaksasi seluruh edge secara berulang sehingga
#    tetap dapat menemukan jarak minimum dengan benar.

# 5. Relaksasi edge adalah proses memperbarui jarak
#    minimum suatu node jika ditemukan jalur yang
#    memiliki total bobot lebih kecil.

# 6. Perbedaan utama Bellman-Ford dan Dijkstra adalah:
#    - Bellman-Ford dapat menangani bobot negatif,
#      sedangkan Dijkstra tidak bisa.
#    - Dijkstra menggunakan pendekatan greedy,
#      sedangkan Bellman-Ford menggunakan relaksasi edge.
#    - Dijkstra lebih cepat dibanding Bellman-Ford.