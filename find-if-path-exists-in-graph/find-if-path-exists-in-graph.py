from collections import defaultdict


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        def dfs(node):
            if node == destination:
                return True
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    if dfs(neighbor):
                        return True
                    
            return False
                    
        graph = defaultdict(list)
        
        for edge in edges:
            u, v = edge
            graph[u].append(v)
            graph[v].append(u)          
                    
        seen = set()     
                
        return dfs(source)
        