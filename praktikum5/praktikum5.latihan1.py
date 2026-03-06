# ==========================================================
# Latihan 1: Rekursi Pangkat
# ==========================================================

# Penjelasan pada fungsi ini adalah:
# Base case terjadi saat n == 0, karena setiap bilangan pangkat 0 bernilai 1.
# Recursive case adalah a * pangkat(a, n-1), artinya nilai diperkecil sampai 0.

def pangkat(a, n):  # fungsi rekursif untuk menghitung pangkat

    # Base case
    if n == 0:  # jika pangkat sudah 0
        return 1  # kembalikan 1

    # Recursive case
    return a * pangkat(a, n - 1)  # a dikali hasil pangkat(a, n-1)

print(pangkat(2, 4))  # Output: 16