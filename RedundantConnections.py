class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf=UnionFind(len(edges)+1)
        # print(uf)
        for edge in edges:
            if uf.union( edge[0],edge[1]):
                return edge

        
class UnionFind:
    def __init__(self, n):
        self.parent=[i for i in range(n)]
        
    def __str__(self):
        return f'{self.parent}'

            
    def root(self,i):
        while i != self.parent[i]:
            i=self.parent[i]
        return i
            
    def connected(self,i,j):
        return self.root(i)==self.root(j)
   
    
    def union(self,i,j):
        if self.connected(i,j):
            return True
        else:
            self.parent[self.root(i)]=self.root(j)
            return False
