# ==========================================================
# Studi Kasus: Generator PIN
# ==========================================================

# Penjelasan pada fungsi ini adalah:
# Program ini membuat semua kemungkinan PIN 3 digit
# menggunakan angka 0, 1, dan 2.
# Karena setiap posisi boleh memakai angka yang sama,
# maka angka bisa muncul berulang (contoh: 000, 111, 222).
#
# Jika ingin supaya angka tidak boleh sama,
# kita harus mengecek dulu apakah angka tersebut
# sudah ada di dalam variabel "hasil".
# Jika sudah ada, maka jangan dipakai lagi.

def buat_pin(panjang, hasil=""):

    if len(hasil) == panjang:  # base case  
        print("PIN:", hasil)  # tampilkan PIN
        return  # hentikan cabang

    for angka in ["0", "1", "2"]:  # loop pilihan angka
        buat_pin(panjang, hasil + angka)  # panggil rekursif dengan menambah angka

buat_pin(3)