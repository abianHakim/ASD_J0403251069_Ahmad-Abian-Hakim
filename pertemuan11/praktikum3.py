#==================================================
# Nama  : Ahmad Abian Hakim
# NIM   : J0403251069
# Kelas : A2
#==================================================

def createGraph(matrix):
    # Menggunakan dictionary untuk menyimpan hasil konversi ke adjacency list
    adj = {}
    V = len(matrix)

    # Melakukan perulangan untuk setiap baris dalam matriks
    for i in range(V):
        # Setiap node (indeks i) diawali dengan list kosong
        adj[i] = []
        # Mengecek setiap kolom (indeks j) dalam baris tersebut
        for j in range(V):
            # Jika bernilai 1, artinya ada hubungan (edge)
            if matrix[i][j] == 1:
                adj[i].append(j)
    return adj

if __name__ == "__main__":
    # Data adjacency matrix 
    matrix = [
        [0, 1, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [0, 0, 1, 0]
    ] 

    # Melakukan konversi menggunakan fungsi
    graph_list = createGraph(matrix)

    print("Adjacency List Representation (Hasil Konversi):")
    # Menampilkan hasil konversi
    for node in graph_list:
        print(f"{node}:", end=" ")
        for neighbor in graph_list[node]:
            print(neighbor, end=" ")
        print()