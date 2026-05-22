#==================================================
# Nama  : Ahmad Abian Hakim
# NIM   : J0403251069
# Kelas : A2
#==================================================

def createGraph(V, edges):
    # Membuat matriks 2D ukuran V x V diisi dengan 0  
    adj = [[0 for _ in range(V)] for _ in range(V)]

    # Mengisi adjacency matrix berdasarkan list edges 
    for it in edges:
        u = it[0] 
        v = it[1] 
        adj[u][v] = 1 
        
        # Karena graf tidak berarah (undirected), tandai secara timbal balik 
        adj[v][u] = 1
    return adj

if __name__ == "__main__":
    # Sesuai gambar: ada 4 node (0, 1, 2, 3) 
    V = 4 
    
    # Daftar hubungan (edge) sesuai gambar soal
    # 0-1, 0-2, 1-2 (diagonal), 2-3 (bawah)
    edges = [[0, 1], [0, 2], [1, 2], [2, 3]] 

    # Membangun matriks menggunakan fungsi
    mat = createGraph(V, edges)

    print("Adjacency Matrix Representation:") 
    for i in range(V): 
        for j in range(V): 
            # Mencetak isi tiap sel matriks t
            print(mat[i][j], end=" ")
        # Pindah baris setelah mencetak satu baris penuh
        print()