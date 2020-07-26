"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        visited=[]
        stack=[node]
        mapping={}
        while stack:
            elem=stack[-1]
            stack.pop()
            print(elem.val)
            node_c=Node(elem.val)
            mapping[elem]=node_c
            
            visited.append(elem)
            for n in elem.neighbors:
                    if n not in visited and n not in stack:
                        stack.append(n)
        for old_node in mapping.keys():
            new_neig=[mapping[old_neig] for old_neig in old_node.neighbors ]
            new_node=mapping[old_node]
            new_node.neighbors=new_neig
            
        return mapping[node]
            
        
