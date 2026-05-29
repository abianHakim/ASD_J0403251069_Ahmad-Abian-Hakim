# Nama :    Ahmad Abian Hakim
# NIM :     J0403251069
# Kelas :   TPL A2
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Latihan 5: Tugas Mandiri MST
# Kasus 1: Jaringan Jalan Antar Kota
# Algoritma: Kruskal
# ==========================================================

# Daftar edge jaringan jalan antar kota: (bobot, kota1, kota2)
edges = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_bobot = 0
connected = set()

for bobot, u, v in edges:
    # Edge dipilih jika masih menghubungkan kota yang belum terhubung
    if u not in connected or v not in connected:
        mst.append((u, v, bobot))
        total_bobot += bobot
        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree Jaringan Jalan Antar Kota:")
for edge in mst:
    print(edge)

print("Total bobot minimum =", total_bobot)


# Jawaban Analisis:
#
# 1. Kasus apa yang dipilih?
#    Jawaban:
#    Kasus yang dipilih adalah Kasus 1, yaitu Jaringan Jalan Antar Kota.
#
# 2. Algoritma apa yang digunakan?
#    Jawaban:
#    Algoritma yang digunakan adalah Kruskal.
#
# 3. Edge mana saja yang dipilih dalam MST?
#    Jawaban:
#    Edge yang dipilih adalah Bogor-Depok dengan bobot 2,
#    Depok-Jakarta dengan bobot 3, dan Depok-Bandung dengan
#    bobot 4.
#
# 4. Berapa total bobot MST?
#    Jawaban:
#    Total bobot MST adalah 9, yang diperoleh dari penjumlahan
#    2 + 3 + 4.
#
# 5. Mengapa edge tertentu tidak dipilih?
#    Jawaban:
#    Karena edge tersebut memiliki bobot yang lebih besar atau tidak
#    diperlukan lagi setelah semua kota terhubung. Jika tetap dipilih,
#    total bobot akan bertambah dan bisa membentuk cycle.