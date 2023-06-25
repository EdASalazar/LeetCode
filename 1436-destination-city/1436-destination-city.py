class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        departures = set()
        arrivals = set()

        for path in paths:
            departures.add(path[0])
            arrivals.add(path[1])
            print(departures, arrivals)

        for arrival in arrivals:
            if arrival not in departures:
                return arrival

        
       

        