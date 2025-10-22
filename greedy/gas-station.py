class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If total gas is less than total cost, it's impossible to complete the circuit
        if sum(gas) < sum(cost):
            return -1
        
        start = 0      # starting station index
        tank = 0       # current gas in tank
        
        # Traverse all stations
        for i in range(len(gas)):
            tank += gas[i] - cost[i]   # gain gas, then spend gas for next move
            
            # If tank goes negative, reset start position
            if tank < 0:
                start = i + 1
                tank = 0
        
        return start
