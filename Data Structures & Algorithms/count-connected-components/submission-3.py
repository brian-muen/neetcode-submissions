class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]

        size = [1] * n

        def union(a, b):
            pa, pb = parent[a], parent[b]
            if pa == pb:
                return
            if size[pa] < size[pb]:
                pa, pb = pb, pa
            parent[pb] = parent[pa]
            size[pa] += size[pb]

        for edge in edges:
            union(edge[0], edge[1])
        
        res = 0 
        for i in range(n):
            if parent[i] == i:
                res += 1

        return res



