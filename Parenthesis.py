class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def backtrack(p: str, r: int, l: int, n: int):
            nonlocal ans
            if r == n and l == n:
                ans.append(p)
            if r < n:
                backtrack(p + '(', r + 1, l, n)
            if l < r:
                backtrack(p + ')', r, l + 1, n)
        
        backtrack('', 0, 0, n)
        return ans
