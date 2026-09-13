class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]

        size = [1] * n

        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[parent[a]]
            return a

        def union(a, b):
            a, b = find(a), find(b)
            if a == b:
                return
            if size[a] < size[b]:
                a, b = b, a
            parent[b] = parent[a]
            size[a] += size[b]

        for edge in edges:
            union(edge[0], edge[1])
        
        res = 0 
        for i in range(n):
            if parent[i] == i:
                res += 1

        return res



