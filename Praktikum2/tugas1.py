#============================================================================
#PRAKTIKUM  2 : Konsep ADT dan File Handling (STUDI KASUS)
#Tugas    1 : Memnuat Fungsi Load Data
#============================================================================

import os

baca_file = "F:\IPB\IPB Smester 2\Algoritma dan Struktur data\Pertemuan 1\Praktikum2\stok_barang.txt"

def baca_data(baca_file):
    data_dict = {}
    with open(baca_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            if not baris:
                continue
            kode, nama, jumlah = baris.split(',')
            data_dict[kode] = {
                'nama': nama,
                'jumlah': int(jumlah)
            }
    return data_dict

buka_data = baca_data(baca_file)
print("jumlah data terbaca:", len(buka_data))

#============================================================================
#PRAKTIKUM  2 : Konsep ADT dan File Handling (STUDI KASUS)
#TUGAS    2 : Memnuat Fungsi Menampilkan data
#============================================================================

def menampilkan_barang(data_dict):
    # Membuat header
    print('\n========== DAFTAR BARANG ===========')
    #membuat tampilan rapih
    print(f"| {'Kode':<10} | {'Nama':<12} | {'Jumlah':>5} |")


    print('-'*35) #membuat garis

    #menampilakan data
    for kode in sorted(data_dict.keys()):
        nama = data_dict[kode]['nama']
        jumlah = data_dict[kode]['jumlah']
        print(f'|{kode:<10} | {nama :<12} | {jumlah:<5} |')

    print('-'*35) #membuat garis
# menampilkan_barang(buka_data)


#============================================================================
#PRAKTIKUM  2 : Konsep ADT dan File Handling (STUDI KASUS)
#TUGAS    3 : Memnuat Fungsi Mencari Data
#============================================================================

def mencari_barang(data_dict):

    kode_cari = input('MAsukan Kode Barang Yang Ingin Dicari: ')
    if kode_cari in data_dict:
        nama = data_dict[kode_cari]['nama']
        jumlah = data_dict[kode_cari]['jumlah']
            
        print('\n======= DATA BARANG DITEMUKAN =======')
        print(f'Kode   : {kode_cari}')
        print(f'Nama   : {nama}')
        print(f'Jumlah : {jumlah}')
    else:
        print('Data Barang Tidak Ditemukan, Pastikan Kode Sudah Benar')

# mencari_barang(buka_data)

#============================================================================
#PRAKTIKUM  2 : Konsep ADT dan File Handling (STUDI KASUS)
#TUGAS    4 : Memnuat Fungsi Update Data
#============================================================================

def ubah_jumlah_barang(data_dict):

    kode = input('Masukan Kode barang yang ingin di update datanya: ').strip()

    if kode not in data_dict:
        print("Kode tidak ditemukan. Update dibatalkan")
        return
    try:
        jumlah_baru = int(input('Masukan Jumlah Yang Anda Inginkan: ').strip())
    except ValueError:
        print('Jumlah harus berupa angka')
        return

    if jumlah_baru < 0 :
        print('Jumlah harus positif')
        return

    jumlah_lama = data_dict[kode]['jumlah']
    data_dict[kode]['jumlah'] = jumlah_baru

    print(f'Update berhasil. Jumlah {kode} beruah dari {jumlah_lama} menjadi {jumlah_baru} ')

# ubah_jumlah_barang(buka_data)

#============================================================================
#PRAKTIKUM  2 : Konsep ADT dan File Handling (STUDI KASUS)
#TUGAS    5 : Memnuat Fungsi Menyimpan data pada file
#============================================================================

def simpan_data(baca_file, data_dict):
    # membuka file dalam mode write
    with open(baca_file, 'w', encoding="utf-8") as file:
        # mengulangi setiap data dalam dictionary
        for kode in sorted(data_dict.keys()):
            nama = data_dict[kode]["nama"]
            jumlah = data_dict[kode]["jumlah"]
            # menulis data ke dalam filel
            file.write(f'{kode},{nama},{jumlah}\n')
# memanggil fungsi simpan data
simpan_data(baca_file, buka_data)
print('\nData Berhasil Disimpan ke file:', baca_file)
# menampilkan_barang(buka_data)


#============================================================================
#PRAKTIKUM  2 : Konsep ADT dan File Handling (STUDI KASUS)
#TUGAS    6 : Memnuat Fungsi Input data baru
#============================================================================

def input_barang(data_dict):
    kode = input('Masukan Kode Barang: ').strip()
    nama = input('Masukan Nama Barang: ').strip()
    try:
        jumlah = int(input('Masukan Jumlah Barang: ').strip())
    except ValueError:
        print('Jumlah harus berupa angka')
        return

    if jumlah < 0 :
        print('Jumlah harus positif')
        return

    data_dict[kode] = {
        'nama': nama,
        'jumlah': jumlah
    }
    print(f'Barang dengan kode {kode} berhasil diinputkan')

# input_barang(buka_data)


def main():
    # load data saat program dijalankan
    buka_data = baca_data(baca_file)

    while True:
        print("\n=== MENU DATA BARANG ===")
        print("1. Tampilkan Data Barang")
        print("2. Cari Data Barang")
        print("3. Ubah Jumlah Barang")
        print("4. Tambah Data Barang Baru")
        # print("5. Simpan Data ke File")
        print("0. Keluar")

        pilihan = input("Pilih Menu: ").strip()

        if pilihan == '1':
            menampilkan_barang(buka_data)

        elif pilihan == '2':
            mencari_barang(buka_data)

        elif pilihan == '3':
            print("\n--- DATA SEBELUM UPDATE ---")
            menampilkan_barang(buka_data)

            ubah_jumlah_barang(buka_data)
            simpan_data(baca_file, buka_data)

            print("\n--- DATA SETELAH UPDATE ---")
            menampilkan_barang(buka_data)

        elif pilihan == '4':
            input_barang(buka_data)
            simpan_data(baca_file, buka_data)

            print("\n--- DATA TERBARU ---")
            menampilkan_barang(buka_data)

        # elif pilihan == '5':
        #     simpan_data(baca_file, buka_data)
        #     print("Data berhasil disimpan ke file.")

        elif pilihan == '0':
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

if __name__ == '__main__':
    main()
