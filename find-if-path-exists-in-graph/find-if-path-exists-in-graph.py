from collections import defaultdict


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        print(edges, n, source, destination)
        
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
                    
        n = len(edges)
        graph = defaultdict(list)
        
        for edge in edges:
            u, v = edge
            graph[u].append(v)
            graph[v].append(u)
            
        print(graph)            
                    

        seen = set()     
                
        
        return dfs(source)
        