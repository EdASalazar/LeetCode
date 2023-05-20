from collections import deque, defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: 
            return 0

        adjacent = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                adjacent[word[:i] + '*' + word[i+1:]].append(word)

        
        visited = set()
        queue = deque([(beginWord, 1)])

        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            if word not in visited:
                visited.add(word)
                for i in range(len(word)):
                    neighbors = word[:i] + '*' + word[i+1:]
                    for neighbor in adjacent[neighbors]:
                        queue.append((neighbor, steps + 1))
        return 0
                            
            
        
        
        