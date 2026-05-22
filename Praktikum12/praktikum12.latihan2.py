# Nama : Ahmad Abian Hakim
# NIM  : J0403251069
# Kelas: TPL-A2
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 2: Implementasi Dijkstra
# ==========================================================

import heapq

# Weighted graph dengan bobot positif
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]

    # Proses selama priority queue masih berisi data
    while priority_queue:

        # Mengambil node dengan jarak terkecil
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat,
        # maka proses dilewati
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():

            # Menghitung jarak baru
            distance = current_distance + weight

            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance

                # Masukkan jarak terbaru ke priority queue
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Menjalankan fungsi Dijkstra dari node A
hasil = dijkstra(graph, 'A')

# Menampilkan hasil jarak terpendek
print("Jarak terpendek dari node A:")

for node, distance in hasil.items():
    print(node, "=", distance)


# Jawaban Analisis:
# 1. Jarak terpendek dari A ke B adalah 4.

# 2. Jarak terpendek dari A ke C adalah 2.

# 3. Jarak terpendek dari A ke D adalah 3.

# 4. Jarak A ke D lebih kecil melalui C dibandingkan melalui B
#    karena jalur A -> C -> D memiliki total bobot:
#    2 + 1 = 3.
#    Sedangkan jalur A -> B -> D memiliki total bobot:
#    4 + 5 = 9.

# 5. Fungsi priority_queue dalam algoritma Dijkstra adalah
#    untuk menyimpan node berdasarkan jarak terkecil agar
#    proses pencarian jalur terpendek menjadi lebih efisien.

# 6. Dijkstra tidak cocok untuk graph dengan bobot negatif
#    karena algoritma ini menggunakan pendekatan greedy
#    dan menganggap jarak minimum yang sudah dipilih
#    tidak akan berubah lagi.
#    Jika terdapat bobot negatif, hasil shortest path
#    dapat menjadi tidak akurat.