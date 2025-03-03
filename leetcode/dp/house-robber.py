from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[-1]
        elif len(nums) == 2:
            return max(nums)
        else:
            # odds_sum = 0
            # evens_sum = 0
            # for i, n in enumerate(nums):
            #     if i % 2 == 0:
            #         evens_sum += n
            #     else:
            #         odds_sum += n
            # return max(odds_sum, evens_sum)
            dp = nums[:]
            for i in range(2, len(nums)):
                dp[i] = max(dp[:i-1]) + nums[i]

            print(dp)
            return max(dp)
