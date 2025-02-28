class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        arr_set = set(arr)
        result = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                curr = arr[i] + arr[j]
                prev = arr[j]
                curr_len = 2
                while curr in arr_set:
                    curr_len += 1
                    result = max(result, curr_len)
                    prev, curr = curr, curr + prev
        return result