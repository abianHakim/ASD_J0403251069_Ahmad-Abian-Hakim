# Praktikum 1 : konsep ADT dan File Handling
# Latihan Dasar 1 : Membaca seluruh isi file data

print("Membuka file dalam satu string")

with open('data_mahasiswa.txt','r',encoding='utf 8')as file:
    isi_file = file.read()
print(isi_file)


#============================================================================
#PRAKTIKUM 1: Konsep ADT dan File Handling
#LATIHAN DASAR 2: Parsing baris menjadi data satuan dan menampilkannya dalam bentuk kolom data
#============================================================================

print("Membuaka file per baris")
jumlah_baris = 0
with open('data_mahasiswa.txt','r',encoding='utf 8')as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() #menghilangkan karakter newline
print('baris Ke-', jumlah_baris)
print('isinya', baris)

with open('data_mahasiswa.txt','r',encoding='utf 8')as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter newline
        nim, nama, nilai = baris.split(',') #pecah menjadi data satuan

print("Nim: ",nim, "| Nama: ",nama,  "| Nilai: ",nilai) 

#============================================================================
#PRAKTIKUM 1: Konsep ADT dan File Handling
#LATIHAN DASAR 3: Membaca data dan menyimpannya ke dalam struktur data list
#============================================================================

data_list= [] #membuat list kosong untuk di gabungkan

with open('data_mahasiswa.txt','r',encoding='utf 8')as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter newline
        nim, nama, nilai = baris.split(',') #pecah menjadi data satuan
        data_list.append([nim,nama,int(nilai)]) #menghubungkan data ke list

print('Menampilkan list')
print(data_list)
print("contoh record pertama", data_list[0]) #Mengambil data pada array dimulai dari index 0


#============================================================================
#PRAKTIKUM 1: Konsep ADT dan File Handling
#LATIHAN DASAR 4: Membaca data dan menyimpannya ke dalam struktur data Dictionary
#============================================================================

data_dict = {} #inisialsasi 

with open('data_mahasiswa.txt','r',encoding='utf 8')as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter newline
        nim, nama, nilai = baris.split(',') #pecah menjadi data satuan
        #simpan data dalam dictionary
        data_dict[nim] = {
            'nama' : nama,
            'nilai' : int(nilai),
        }

print('menampilkan data dictionary')
print(data_dict)