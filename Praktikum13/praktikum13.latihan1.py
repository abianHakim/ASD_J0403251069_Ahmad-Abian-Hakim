# Nama :    Ahmad Abian Hakim
# NIM :     J0403251069
# Kelas :   TPL A2
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Latihan 1: Memahami Konsep Spanning Tree
# ==========================================================

# Daftar edge pada graph awal
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree yang valid
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

print("Edge pada graph:")
for edge in edges:
    print(edge)

print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))


# Jawaban Analisis:
#
# 1. Apa perbedaan graph awal dan spanning tree?
#    Jawaban:
#    Graph awal memiliki lebih banyak edge dan masih dapat membentuk
#    cycle. Sedangkan spanning tree hanya menggunakan edge yang
#    diperlukan untuk menghubungkan seluruh node tanpa membentuk cycle.
#
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    Jawaban:
#    Karena cycle menyebabkan penggunaan edge yang berlebihan dan
#    membuat koneksi menjadi kurang efisien. Spanning tree bertujuan
#    menghubungkan semua node dengan edge seminimal mungkin.
#
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    Jawaban:
#    Karena spanning tree hanya membutuhkan jumlah edge sebanyak
#    jumlah node dikurangi satu. Dengan cara ini seluruh node tetap
#    terhubung tanpa membentuk cycle.