from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left = 0
        mid = 0
        right = max(candies)
        while left < right:
            mid = (left + right + 1) // 2
            if k > sum([i // mid for i in candies]):
                right = mid - 1
            else:
                left = mid
        return left


if __name__ == '__main__':
    print(Solution().maximumCandies([5, 10, 10], 9))

"""
Accepted
Next question
1960. Maximum Product of the Length of Two Palindromic Substrings
More challenges
875. Koko Eating Bananas
1760. Minimum Limit of Balls in a Bag
1870. Minimum Speed to Arrive on Time
"""