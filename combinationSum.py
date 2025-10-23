from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def helper(temp, curr_sum, curr_index):
            if curr_sum == target:
                result.append(temp[:])
                return
            if curr_index >= len(candidates) or curr_sum > target:
                return
            temp.append(candidates[curr_index])
            helper(temp, curr_sum + candidates[curr_index], curr_index)
            temp.pop()
            helper(temp, curr_sum, curr_index + 1)
        helper([], 0, 0)
        return result
