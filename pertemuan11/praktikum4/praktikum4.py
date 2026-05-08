#==================================================
# Nama  : Ahmad Abian Hakim
# NIM   : J0403251069
# Kelas : A2
#================================================== 

def createGraphList(edges):
    # Menggunakan dictionary untuk menyimpan adjacency list berbobot 
    adj_list = {}
    for it in edges:
        u, v, w = it[0], it[1], it[2]
        # Inisialisasi list jika node belum ada
        if u not in adj_list: adj_list[u] = []
        if v not in adj_list: adj_list[v] = []
        # Simpan tujuan dan bobotnya (sebagai list)
        adj_list[u].append([v, w])
        adj_list[v].append([u, w])
    return adj_list

def createGraphMatrix(V, nodes, edges):
    # Mapping nama kota ke indeks angka (0 sampai V-1)
    node_to_idx = {nodes[i]: i for i in range(V)}
    # Buat matriks kosong diisi 0 ukuran V x V 
    mat = [[0 for _ in range(V)] for _ in range(V)]
    
    for it in edges:
        u_idx = node_to_idx[it[0]]
        v_idx = node_to_idx[it[1]]
        w = it[2] # Bobot berupa jarak KM 
        # Isi matriks dengan nilai bobot 
        mat[u_idx][v_idx] = w
        mat[v_idx][u_idx] = w
    return mat

if __name__ == "__main__":
    # 1. Menentukan Node (Vertex)
    # Representasi kota di wilayah Banten
    nodes = ["Serang", "Cilegon", "Merak", "Pandeglang", "Rangkasbitung"]
    V = len(nodes)
    
    # 2. Menentukan Hubungan dan Bobot Jarak (Edge & Weight)
    # Format: [Kota A, Kota B, Jarak KM]
    edges = [
        ["Serang", "Cilegon", 20], 
        ["Cilegon", "Merak", 15],
        ["Serang", "Pandeglang", 25], 
        ["Serang", "Rangkasbitung", 35],
        ["Pandeglang", "Rangkasbitung", 20], 
        ["Cilegon", "Pandeglang", 40]
    ]


    #  POIN 3: TAMPILKAN NAMA NODE 
    print("1. DAFTAR NAMA NODE (KOTA):")
    for i, nama in enumerate(nodes):
        print(f"Node {i}: {nama}")

    #  POIN 4: TAMPILKAN HUBUNGAN ANTAR NODE 
    print("\n2. HUBUNGAN ANTAR NODE (JALAN & JARAK):")
    for u, v, w in edges:
        print(f"{u} <---> {v} | Jarak: {w} KM")

    #  POIN 1: TAMPILKAN ADJACENCY LIST
    graph_list = createGraphList(edges)
    print("\n3. ADJACENCY LIST REPRESENTATION (WEIGHTED):")
    for node in nodes:
        print(f"{node}:", end=" ")
        for neighbor in graph_list[node]:
            print(f"-> {neighbor[0]} ({neighbor[1]}KM)", end=" ")
        print()

    #  POIN 2: TAMPILKAN ADJACENCY MATRIX 
    graph_matrix = createGraphMatrix(V, nodes, edges)
    print("\n4. ADJACENCY MATRIX REPRESENTATION (WEIGHTED KM):")
    # Print Header Nama Kota (Inisial)
    print("      ", "  ".join([n[:3] for n in nodes]))
    for i in range(V):
        print(f"{nodes[i][:3]:<5}", end=" ")
        for j in range(V):
            # Tampilkan jarak, jika 0 berarti tidak ada jalur langsung
            print(f"{graph_matrix[i][j]:>3}", end="  ")
        print()