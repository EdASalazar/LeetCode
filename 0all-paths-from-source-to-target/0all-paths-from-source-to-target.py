class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        ans = []

        def backtrack(curr, path):
            if curr == target:
                ans.append(list(path))
                return
            
            for next_node in graph[curr]:
                path.append(next_node)
                backtrack(next_node, path)
                path.pop()
            
                    
        path = [0]       
        backtrack(0, path)
       
        return ans
        
        
        