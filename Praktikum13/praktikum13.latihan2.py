# Nama :    Ahmad Abian Hakim
# NIM :     J0403251069
# Kelas :   TPL A2
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Latihan 2: Implementasi Sederhana Algoritma Kruskal
# ==========================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0
connected = set()

for weight, u, v in edges:
    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total_weight)


# Jawaban Analisis:
#
# 1. Edge mana yang dipilih pertama kali?
#    Jawaban:
#    Edge yang dipilih pertama kali adalah C-D dengan bobot 1 karena
#    memiliki bobot paling kecil dibandingkan edge lainnya.
#
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
#    Jawaban:
#    Karena algoritma Kruskal bekerja dengan memilih edge yang memiliki
#    bobot terkecil terlebih dahulu agar total bobot MST yang dihasilkan
#    menjadi minimum.
#
# 3. Berapa total bobot MST yang dihasilkan?
#    Jawaban:
#    Total bobot MST yang dihasilkan adalah 6, yaitu dari penjumlahan
#    bobot edge 1 + 2 + 3.
#
# 4. Mengapa edge tertentu tidak dipilih?
#    Jawaban:
#    Karena setelah seluruh node terhubung, edge tambahan tidak lagi
#    diperlukan dan dapat menyebabkan cycle atau menambah total bobot.