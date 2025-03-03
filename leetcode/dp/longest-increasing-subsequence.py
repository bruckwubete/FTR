from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int], n=None) -> int:
        dp =[1] * len(nums)
        seq = []
        for i in range(1, len(nums)):
            cur_seq = []
            for k in range(i):
                if nums[i] > nums[k]:
                    if dp[k] + 1 > dp[i]:
                        cur_seq.append(nums[k])
                        dp[i] = dp[k] + 1
            cur_seq.append(nums[i])
            if dp[i] == max(dp):
                seq = cur_seq
            curr_seq = []
            # prev_len = [dp[k] for k in range(i) if nums[i] > nums[k]]
            # dp[i] = 1 + max(prev_len, default=0)
        print(seq)
        return max(dp, default=0)