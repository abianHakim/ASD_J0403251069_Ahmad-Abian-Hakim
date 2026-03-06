# ==========================================================
# Latihan 4: Kombinasi Huruf
# ==========================================================

# Penjelasan pada fungsi ini adalah:
# Setiap posisi memiliki 2 kemungkinan (A atau B).
# Jika panjang n, maka jumlah kombinasi adalah 2^n.

def kombinasi(n, hasil=""):

    if len(hasil) == n:  # base case jika panjang sudah n
        print(hasil)  # tampilkan kombinasi
        return  # hentikan cabang

    kombinasi(n, hasil + "A")  # pilih A
    kombinasi(n, hasil + "B")  # pilih B

kombinasi(2)