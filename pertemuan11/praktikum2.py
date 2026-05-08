#==================================================
# Nama  : Ahmad Abian Hakim
# NIM   : J0403251069
# Kelas : A2
#==================================================

def createGraph(edges):
    # Menggunakan dictionary untuk menyimpan adjacency list
    adj = {}

    # Mengisi adjacency list berdasarkan pasangan huruf (node)
    for it in edges:
        u = it[0]
        v = it[1]
        
        # Jika node belum ada di dictionary, buat list kosong
        if u not in adj:
            adj[u] = []
        if v not in adj:
            adj[v] = []
            
        # Tambahkan hubungan antar node (tetangga)
        adj[u].append(v)
        # Karena graf tidak berarah (undirected), tambahkan sebaliknya
        adj[v].append(u)
    return adj

if __name__ == "__main__":
    # Daftar hubungan (edge) 
    edges = [["A", "B"], ["A", "C"], ["B", "D"], ["C", "D"]]

    # Membangun adjacency list menggunakan fungsi
    graph = createGraph(edges)

    print("Adjacency List Representation:")
    # Menampilkan isi dictionary sesuai urutan abjad node
    for node in sorted(graph.keys()):
        # Print node dan daftar tetangganya
        print(f"{node}:", end=" ")
        for neighbor in graph[node]:
            print(neighbor, end=" ")
        print()