#============================================================================
#PRAKTIKUM  2 : Konsep ADT dan File Handling (STUDI KASUS)
#LATIHAN    1 : Memnuat Fungsi Load Data
#============================================================================

# Variable menyimpan data
nama_file = "F:\IPB\IPB Smester 2\Algoritma dan Struktur data\Pertemuan 1\Praktikum2\data_mahasiswa.txt"

def baca_data(nama_file):
    data_dict = {} # inisialisasi data dictionary
    with open(nama_file,"r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()  #ambil data per baris dan hilangkan newline
            nim, nama, nilai = baris.split(',') #pecah menjadi data satuan
            data_dict[nim] = {
            'nama' : nama,
            'nilai' : int(nilai)
        }
    return data_dict

buka_data = baca_data( nama_file)
# print('jumlah data terbaca' , len(buka_data), '\n')


#============================================================================
#PRAKTIKUM  2 : Konsep ADT dan File Handling (STUDI KASUS)
#LATIHAN    2 : Memnuat Fungsi Menampilkan data
#============================================================================

def menampilkan_data(data_dict):
    # Membuat header tabel
    print('\n======== DAFTAR MAHASISWA =========')
    #untuk tampilan yang rapi, atur lebar kolom
    print(f'|{'NIM' : <10} | {'Nama': <12} | {'Nilai' :>5}|')

    # 'NIM': <10} artinya nim rata kiri dengan lebar kolom 10 karakter
    #{ {'Nama': <12} artinya nama rata kiri dengan lebar kolom 12 karakter
    #{'Nilai' :>5} artinya nilai rata kanan lebar kolom 5

    print('-'*35) #Membuat Garis

#menampilkan isi datanya
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f'|{nim:<10} | {nama :<12} | {nilai:<5}|')

    print('-'*35) #Membuat Garis
# menampilkan_data(buka_data)  #memanggil fungsi untuk menampilkan data


#============================================================================
#PRAKTIKUM  2 : Konsep ADT dan File Handling (STUDI KASUS)
#LATIHAN    3 : Memnuat Fungsi Mencari Data
#============================================================================

def mencari_data(data_dict):

# Pencarian data berdasarkan nim sebanyak key diction 
# Membuat input nim mahasiswa yang akan dicari
    nim_cari = input('Masukan NIM Mahasiswa yang inign dicari: ').strip()
    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print('\n======= Daftar Mahasiswa Ditemukan ========')
        print(f'NIM     : {nim_cari}')
        print(f'Nama    : {nama}')
        print(f'Nilai   : {nilai}')
    else:
        print("Data Mahasiswa Tidak Ditemukan. Pastikan NIM sudah sesuai")

#memanggil fungsi mencari data dari nim
# mencari_data(buka_data)


#============================================================================
#PRAKTIKUM  2 : Konsep ADT dan File Handling (STUDI KASUS)
#LATIHAN    4 : Memnuat Fungsi Update Data
#============================================================================

#membuat fungsi update data

def ubah_data(data_dict):
    
    #awali dulu dengan mencari data / nim mahasiswa yang ingin di update
    nim = input("Masukan NIM mahasiswa yang ingin diubah datanya :").strip()
    
    if nim not in data_dict:
        print("NIM tidak ditemukan. Update dibatalkan")
        return
    
    try:
        nilai_baru = int(input("Masukan nilai baru 0-100 :").strip())
    except ValueError:      
        print("Nilai harus berupa angka . Update dibatalkan")
        
    if nilai_baru < 0 or nilai_baru >= 100:
        print("Nilai harus diantara 0 sampai 100. Update dibatalkan")
    
    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru
    
    print(f"Update behasil. NIlai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")
    
# memanggil ubah data
# ubah_data(buka_data)

#============================================================================
#PRAKTIKUM  2 : Konsep ADT dan File Handling (STUDI KASUS)
#LATIHAN    5 : Memnuat Fungsi Menyimpan data pada file
#============================================================================

def simpan_data(nama_file, data_dict):
    # membuka file dalam mode write 
    with open(nama_file, 'w', encoding="utf-8") as file:
        # mengulangi setiap data dalam dictionary
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            # menulis data ke dalam file
            file.write(f'{nim},{nama},{nilai}\n')

# memanggil fungsi simpan data
simpan_data(nama_file, buka_data) 
print('\nData Berhasil Disimpan ke file:', nama_file)
    

#============================================================================
#PRAKTIKUM  2 : Konsep ADT dan File Handling (STUDI KASUS)
#LATIHAN    6: Memnuat Fungsi interaktif
#============================================================================


def main():

    #load data otomatis saat program dimulai
    buka_data = baca_data(nama_file)

    while True:
        print("\n===MENU DATA MAHASISWA===")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Berdasarkan NIM")
        print("3. Ubah Nilai Mahasiswa ")
        print("4. Simpan Data ke File")
        print("0. Keluar")

        pilihan = input("Pilih Menu: ").strip()

        if pilihan == '1': 
            menampilkan_data(buka_data)

        elif pilihan == '2':
            mencari_data(buka_data)

        elif pilihan == '3':
            ubah_data(buka_data)

        elif pilihan == '4':
            simpan_data(nama_file,buka_data)
            print('data berhasil diperbaharui. data yang sudah di update\n')
            menampilkan_data(buka_data)

        elif pilihan == '0':
            print('Program selesai')
            break

        else:
            print('pilihan tidak valid')
            

if __name__ == '__main__' :
    main()