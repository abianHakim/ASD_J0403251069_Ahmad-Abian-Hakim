# Nama : Ahmad Abian Hakim
# NIM  : J0403251069
# Kelas: TPL-A2
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================

import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak node awal adalah 0
    distances[start] = 0

    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]

    # Proses selama priority queue masih memiliki data
    while priority_queue:

        # Mengambil node dengan jarak terkecil
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak saat ini lebih besar dari jarak yang tersimpan,
        # maka proses dilewati
        if current_distance > distances[current_node]:
            continue

        # Memeriksa semua tetangga node saat ini
        for neighbor, weight in graph[current_node].items():

            # Menghitung jarak baru
            distance = current_distance + weight

            # Jika ditemukan jarak yang lebih kecil
            if distance < distances[neighbor]:

                # Update jarak minimum
                distances[neighbor] = distance

                # Masukkan ke priority queue
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Menjalankan algoritma Dijkstra dari node Gerbang
hasil = dijkstra(graph, 'Gerbang')

# Menampilkan hasil jarak terpendek
print("Jarak terpendek dari Gerbang Kampus:")

for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")


# Jawaban Analisis:
# 1. Lokasi yang paling dekat dari Gerbang adalah Kantin
#    dengan waktu tempuh 2 menit.

# 2. Waktu tempuh terpendek dari Gerbang ke Aula adalah 7 menit.
#    Jalur tercepat:
#    Gerbang -> Kantin -> Lab -> Aula
#    = 2 + 4 + 1
#    = 7 menit.

# 3. Jalur langsung tidak selalu menghasilkan jarak paling kecil.
#    Terkadang jalur yang melewati beberapa node lain memiliki
#    total bobot lebih kecil dibanding jalur langsung.

# 4. Dijkstra cocok digunakan pada kasus lokasi kampus ini
#    karena seluruh bobot graph bernilai positif dan algoritma
#    Dijkstra sangat efisien untuk mencari jalur terpendek
#    pada weighted graph dengan bobot positif.