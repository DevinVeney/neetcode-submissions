class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for num in nums:
            if num not in hashmap.keys():
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        
        intermediary=[]
        for key,val in hashmap.items():
            intermediary.append((val,key))
        intermediary = sorted(intermediary, key=lambda x: x[0])

        output=[]
        for _ in range(k):
            val, key = intermediary.pop()
            output.append(key)
        return output



