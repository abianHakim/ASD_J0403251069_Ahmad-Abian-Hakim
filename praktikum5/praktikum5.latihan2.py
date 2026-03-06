# ==========================================================
# Latihan 2: Tracing Rekursi
# ==========================================================

# Penjelasan pada fungsi ini adalah:
# Tulisan "Keluar" muncul terbalik karena setelah mencapai n == 0,
# fungsi tidak langsung selesai semuanya.
# Fungsi akan kembali ke pemanggilan sebelumnya satu per satu.
# Karena yang terakhir dipanggil akan selesai lebih dulu,
# maka urutan keluarnya menjadi kebalikan dari urutan masuknya.

def countdown(n):

    if n == 0:  # base case
        print("Selesai")  # tampilkan selesai
        return  # hentikan fungsi

    print("Masuk:", n)  # fase masuk (stacking)

    countdown(n - 1)  # pemanggilan rekursif

    print("Keluar:", n)  # fase keluar (unwinding)

countdown(3)