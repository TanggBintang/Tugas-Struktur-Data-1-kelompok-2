class Graf:
    def __init__(self):
        self.daftarkota = {}
       
    def tambahkanVertex(self, Vertex):
        if Vertex not in self.daftarkota:
            self.daftarkota[Vertex] = {}
            return True
        return False
    
    def tambahkanEdge(self, kota1, kota2, jarak):
        if kota1 in self.daftarkota and kota2 in self.daftarkota:
            self.daftarkota[kota1][kota2] = jarak
            self.daftarkota[kota2][kota1] = jarak
            return True
        return False
    
    def dijkstra(self, start):
        jarak = {Vertex: float('inf') for Vertex in self.daftarkota}
        jarak[start] = 0
        dikunjungi = set()
        while len(dikunjungi) < len(self.daftarkota):
            min_jarak = float('inf')
            Vertex_sekarang = None
            for Vertex in self.daftarkota:
                if Vertex not in dikunjungi and jarak[Vertex] < min_jarak:
                    min_jarak = jarak[Vertex]
                    Vertex_sekarang = Vertex
            dikunjungi.add(Vertex_sekarang)
            for tetangga, weight in self.daftarkota[Vertex_sekarang].items():
                jarak_baru = jarak[Vertex_sekarang] + weight
                if jarak_baru < jarak[tetangga]:
                    jarak[tetangga] = jarak_baru
        return jarak

singaporegraph = Graf() 
singaporegraph.tambahkanVertex("SINGAPURA")
singaporegraph.tambahkanVertex("ANG MO KIO")
singaporegraph.tambahkanVertex("SENGKANG")
singaporegraph.tambahkanVertex("PAYA LEBAR")
singaporegraph.tambahkanVertex("BUKIT TIMAH")
singaporegraph.tambahkanVertex("NOVENA")
singaporegraph.tambahkanVertex("TAMPINES")
singaporegraph.tambahkanVertex("JURONG EAST")
singaporegraph.tambahkanVertex("TENGAH")
singaporegraph.tambahkanVertex("CHOA CHU KANG")
singaporegraph.tambahkanVertex("MANDAI")
singaporegraph.tambahkanVertex("KRANJI")
singaporegraph.tambahkanVertex("SEMBAWANG")
