from collections import defaultdict

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        seen = set(restricted)
        graph = defaultdict(list)
        
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
                
                    
        for edge in edges:
            u, v = edge
            graph[u].append(v)
            graph[v].append(u)
        
        dfs(0)
        
        return max(1, len(seen) - len(restricted))
        