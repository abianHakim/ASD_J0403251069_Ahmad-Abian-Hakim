# Nama : Ahmad Abian Hakim
# NIM  : J0403251069
# Kelas: TPL-A2
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================

# Representasi weighted graph menggunakan dictionary bersarang
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Menghitung dua kemungkinan jalur dari A ke D

# Jalur pertama:
# A -> B -> D
jalur_1 = graph['A']['B'] + graph['B']['D']

# Jalur kedua:
# A -> C -> D
jalur_2 = graph['A']['C'] + graph['C']['D']

# Menampilkan total bobot masing-masing jalur
print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

# Membandingkan jalur untuk menentukan jalur terpendek
if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")


# Jawaban Analisis:
# 1. Total bobot jalur A -> B -> D adalah 9.
#    dapat dari 4 + 5 = 9.

# 2. Total bobot jalur A -> C -> D adalah 3.
#    dapat dari 2 + 1 = 3.

# 3. Jalur yang dipilih sebagai jalur terpendek adalah?
#    A -> C -> D karena memiliki total bobot lebih kecil.

# 4. Jalur terpendek tidak selalu ditentukan dari jumlah edge
#    yang paling sedikit? 
#    karena algoritma shortest path
#    berfokus pada total bobot terkecil, bukan jumlah langkah.
#    Meskipun jumlah edge sama atau lebih banyak, jalur dengan
#    total bobot lebih kecil tetap menjadi pilihan terbaik.