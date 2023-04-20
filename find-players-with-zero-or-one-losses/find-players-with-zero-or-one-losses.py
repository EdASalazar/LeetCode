from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
            winners = set()
            losers = set()
            losers_hash = defaultdict(int)
            winsOnly = []
            oneLoss = []
            
            for arr in matches:
                winners.add(arr[0])
                losers.add(arr[1])
                losers_hash[arr[1]] +=1
            
            for x in losers_hash:
                if losers_hash[x] == 1:
                    oneLoss.append(x)
            
            for win in winners:
                if win not in losers:
                    winsOnly.append(win)

            return [sorted(list(winsOnly)), sorted(list(oneLoss))]  
        
                  

        