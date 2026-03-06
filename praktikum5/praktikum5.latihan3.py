# ==========================================================
# Latihan 3: Mencari Nilai Maksimum
# ==========================================================

# Penjelasan pada fungsi ini adalah:
# Base case terjadi saat index berada di elemen terakhir.
# Recursive call mencari nilai maksimum dari sisa list.

def cari_maks(data, index=0):

    # Base case
    if index == len(data) - 1:  # jika sudah di elemen terakhir
        return data[index]  # kembalikan elemen terakhir

    # Recursive case
    maks_sisa = cari_maks(data, index + 1)  # cari maksimum dari sisa list

    if data[index] > maks_sisa:  # bandingkan elemen sekarang dengan maksimum sisa
        return data[index]  # kembalikan yang lebih besar
    else:
        return maks_sisa  # kembalikan maksimum sisa

angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))