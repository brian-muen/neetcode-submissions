class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [False] * 3

        candidates = [True] * len(triplets)
        for idx, position in enumerate(target):
            for pos, item in enumerate(triplets):
                if item[idx] > position:
                    candidates[pos] = False
        
        for idx, position in enumerate(target):
            for pos, item in enumerate(triplets):
                if candidates[pos] == False:
                    continue
                if item[idx] == position:
                    res[idx] = True
        
        for i in res:
            if i == False:
                return False
        return True


            



                    

        
                
        

        


        