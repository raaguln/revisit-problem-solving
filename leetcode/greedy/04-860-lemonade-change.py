class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_dollar = 0
        ten_dollar = 0
        
        for paid in bills:
            if paid == 5:
                five_dollar += 1
            elif paid == 10:
                if five_dollar == 0:
                    return False
                five_dollar -= 1
                ten_dollar += 1
            else:  # paid == 20
                # Prefer giving one $10 and one $5 as change
                if ten_dollar > 0 and five_dollar > 0:
                    ten_dollar -= 1
                    five_dollar -= 1
                elif five_dollar >= 3:
                    five_dollar -= 3
                else:
                    return False
        return True