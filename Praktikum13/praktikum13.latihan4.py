# Nama :    Ahmad Abian Hakim
# NIM :     J0403251069
# Kelas :   TPL A2
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Latihan 4: Studi Kasus Jaringan Kabel Antar Gedung
# Algoritma: Kruskal
# ==========================================================

# Daftar edge: (biaya, gedung1, gedung2)
edges = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
]

# Mengurutkan edge dari biaya terkecil
edges.sort()

mst = []
total_biaya = 0
connected = set()

for biaya, u, v in edges:
    # Edge dipilih jika masih menghubungkan node baru
    if u not in connected or v not in connected:
        mst.append((u, v, biaya))
        total_biaya += biaya
        connected.add(u)
        connected.add(v)

print("Jaringan kabel dengan biaya minimum:")
for edge in mst:
    print(edge)

print("Total biaya minimum =", total_biaya)


# Jawaban Analisis:
#
# 1. Algoritma apa yang digunakan?
#    Jawaban:
#    Algoritma yang digunakan adalah Kruskal.
#
# 2. Edge mana saja yang dipilih?
#    Jawaban:
#    Edge yang dipilih adalah GedungC-GedungD dengan bobot 1,
#    GedungA-GedungC dengan bobot 2, dan GedungB-GedungD dengan
#    bobot 3.
#
# 3. Berapa total biaya minimum?
#    Jawaban:
#    Total biaya minimum yang diperoleh adalah 6.
#
# 4. Mengapa MST cocok digunakan pada kasus ini?
#    Jawaban:
#    Karena MST dapat menghubungkan seluruh gedung dengan biaya
#    pemasangan kabel yang minimum tanpa membuat koneksi yang
#    berlebihan.