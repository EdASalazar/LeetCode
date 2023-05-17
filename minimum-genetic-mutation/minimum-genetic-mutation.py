from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        queue = deque([(startGene, 0)])
        seen = set(startGene)
        chromo = 'ACGT'

        while queue: 
            node, steps = queue.popleft()
            if node == endGene:
                return steps
        

            for c in chromo:
                for i in range(len(node)):
                    neighbor = node[:i] + c + node[i +1:]
                    if neighbor not in seen and neighbor in bank:
                        queue.append((neighbor, steps + 1))
                        seen.add(neighbor)


                    
        return -1
        
        