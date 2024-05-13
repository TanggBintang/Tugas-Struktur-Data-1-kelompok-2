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
singaporegraph.tambahkanEdge("SINGAPURA","JURONG EAST", 13)
singaporegraph.tambahkanEdge("SINGAPURA","BUKIT TIMAH", 8)   
singaporegraph.tambahkanEdge("SINGAPURA","PAYA LEBAR", 9)
singaporegraph.tambahkanEdge("SINGAPURA","NOVENA", 5)
singaporegraph.tambahkanEdge("SINGAPURA","TAMPINES", 14)
singaporegraph.tambahkanEdge("JURONG EAST","TENGAH", 3)
singaporegraph.tambahkanEdge("JURONG EAST","CHOA CHU KANG", 7)
singaporegraph.tambahkanEdge("JURONG EAST","BUKIT TIMAH", 7)
singaporegraph.tambahkanEdge("JURONG EAST","SINGAPURA", 13)
singaporegraph.tambahkanEdge("BUKIT TIMAH","SINGAPURA", 8)
singaporegraph.tambahkanEdge("BUKIT TIMAH","JURONG EAST", 6)
singaporegraph.tambahkanEdge("BUKIT TIMAH","CHOA CHU KANG", 9)
singaporegraph.tambahkanEdge("BUKIT TIMAH","ANG MO KIO", 7)
singaporegraph.tambahkanEdge("BUKIT TIMAH","MANDAI", 11)
singaporegraph.tambahkanEdge("BUKIT TIMAH","NOVENA", 4)
singaporegraph.tambahkanEdge("NOVENA","BUKIT TIMAH", 4)
singaporegraph.tambahkanEdge("NOVENA","SINGAPURA", 5)
singaporegraph.tambahkanEdge("NOVENA","ANG MO KIO", 5)
singaporegraph.tambahkanEdge("NOVENA","SENGKANG", 9)
singaporegraph.tambahkanEdge("NOVENA","TAMPINES", 13)
singaporegraph.tambahkanEdge("PAYA LEBAR","SINGAPURA", 9)
singaporegraph.tambahkanEdge("PAYA LEBAR","ANG MO KIO", 6)
singaporegraph.tambahkanEdge("PAYA LEBAR","MANDAI", 12)
singaporegraph.tambahkanEdge("PAYA LEBAR","SENGKANG", 4)
singaporegraph.tambahkanEdge("PAYA LEBAR","TAMPINES", 6)
singaporegraph.tambahkanEdge("TAMPINES","SINGAPURA", 14)
singaporegraph.tambahkanEdge("TAMPINES","NOVENA", 13)
singaporegraph.tambahkanEdge("TAMPINES","PAYA LEBAR", 6)
singaporegraph.tambahkanEdge("TAMPINES","SENGKANG", 7)
singaporegraph.tambahkanEdge("SENGKANG","TAMPINES", 9)
singaporegraph.tambahkanEdge("SENGKANG","PAYA LEBAR", 4)
singaporegraph.tambahkanEdge("SENGKANG","NOVENA", 9)
singaporegraph.tambahkanEdge("SENGKANG","ANG MO KIO", 6)
singaporegraph.tambahkanEdge("SENGKANG","MANDAI", 9)
singaporegraph.tambahkanEdge("SENGKANG","SEMBAWANG", 11)
singaporegraph.tambahkanEdge("TENGAH","JURONG EAST", 3)
singaporegraph.tambahkanEdge("TENGAH","CHOA CHU KANG", 4)
singaporegraph.tambahkanEdge("CHOA CHU KANG","TENGAH", 4)
singaporegraph.tambahkanEdge("CHOA CHU KANG","JURONG EAST", 6)
singaporegraph.tambahkanEdge("CHOA CHU KANG","BUKIT TIMAH", 9)
singaporegraph.tambahkanEdge("CHOA CHU KANG","ANG MO KIO", 11)
singaporegraph.tambahkanEdge("CHOA CHU KANG","MANDAI", 10)
singaporegraph.tambahkanEdge("CHOA CHU KANG","KRANJI", 4)
singaporegraph.tambahkanEdge("ANG MO KIO","NOVENA", 5)
singaporegraph.tambahkanEdge("ANG MO KIO","BUKIT TIMAH", 7)
singaporegraph.tambahkanEdge("ANG MO KIO","CHOA CHU KANG", 11)
singaporegraph.tambahkanEdge("ANG MO KIO","MANDAI", 7)
singaporegraph.tambahkanEdge("ANG MO KIO","SENGKANG", 6)
singaporegraph.tambahkanEdge("ANG MO KIO","PAYA LEBAR", 6)
singaporegraph.tambahkanEdge("MANDAI","SEMBAWANG", 3)
singaporegraph.tambahkanEdge("MANDAI","KRANJI", 8)
singaporegraph.tambahkanEdge("MANDAI","CHOA CHU KANG", 10)
singaporegraph.tambahkanEdge("MANDAI","BUKIT TIMAH", 11)
singaporegraph.tambahkanEdge("MANDAI","ANG MO KIO", 7)
singaporegraph.tambahkanEdge("MANDAI","PAYA LEBAR", 12)
singaporegraph.tambahkanEdge("MANDAI","SENGKANG", 9)
singaporegraph.tambahkanEdge("KRANJI","CHOA CHU KANG", 4)
singaporegraph.tambahkanEdge("KRANJI","MANDAI", 8)
singaporegraph.tambahkanEdge("KRANJI","SEMBAWANG", 9)
singaporegraph.tambahkanEdge("SEMBAWANG","KRANJI", 9)
singaporegraph.tambahkanEdge("SEMBAWANG","MANDAI", 3)
singaporegraph.tambahkanEdge("SEMBAWANG","SENGKANG", 11)

jarak = singaporegraph.dijkstra("SINGAPURA")
for Vertex in jarak:
    print("Jarak dari", Vertex, ":", jarak[Vertex])
singaporegraph.tambahkanVertex("TENGAH")
singaporegraph.tambahkanVertex("CHOA CHU KANG")
singaporegraph.tambahkanVertex("MANDAI")
singaporegraph.tambahkanVertex("KRANJI")
singaporegraph.tambahkanVertex("SEMBAWANG")
