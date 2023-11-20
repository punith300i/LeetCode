class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        last_m, last_p, last_g = 0, 0, 0
        collection_time = 0
        
        prefix_travel_sum = [0]*(len(travel)+1)
        prefix_travel_sum[1] = travel[0]
        
        for i in range(1,len(travel)):
            prefix_travel_sum[i+1] = travel[i] + prefix_travel_sum[i]
        
        for index, g in reversed(list(enumerate(garbage))):
            collection_time+=len(g)
            if not last_m  and 'M' in g:
                last_m = index
            if not last_g  and 'G' in g:
                last_g = index
            if not last_p  and 'P' in g:
                last_p = index
        
        return prefix_travel_sum[last_m] + prefix_travel_sum[last_g] + prefix_travel_sum[last_p] + collection_time
