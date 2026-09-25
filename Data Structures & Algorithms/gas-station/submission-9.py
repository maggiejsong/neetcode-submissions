# Input: gas = [1, 2] cost = [3, 2]
# Output: -1

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        
        total = 0
        result = 0
        n = len(gas)
        for i in range(n):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                res = i + 1
        
        return res

