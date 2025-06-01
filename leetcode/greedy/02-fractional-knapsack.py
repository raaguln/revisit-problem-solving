'''
- knapsack of "capacity"
- "weights" and "values" of item
- You can take any fraction of an item.

'''
from typing import List

class Solution:
    def fractionalKnapsack(self, capacity: int, weights: List[int], values: List[int]) -> float:
        # Sort items by value/weight ratio in descending order
        # most value per weight goes first into the knapsack
        items = sorted(zip(values, weights), key=lambda x: x[0]/x[1], reverse=True)

        total_value = 0.0
        for value, weight in items:
            if capacity == 0:
                break
            # Either take whole, or fraction of what you can take
            take = min(weight, capacity)
            total_value += take * (value / weight)
            capacity -= take
        return total_value
