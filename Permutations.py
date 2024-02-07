from typing import List

class Solution:
    @staticmethod
    def check(nums: List[int], num: int) -> bool:
        for i in range(len(nums)):
            if nums[i] == num:
                return False
        return True
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        s = len(nums)
        
        def backtrack(nums: List[int], x: List[int], size: int):
            if size == s:
                ans.append(x[:])  
                return
            for i in range(s):
                if self.check(x, nums[i]):
                    x.append(nums[i])
                    backtrack(nums, x, size + 1)
                    x.pop()  
        
        backtrack(nums, [], 0)
        return ans
