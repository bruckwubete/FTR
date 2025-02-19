class Solution:
    @staticmethod
    def two_sums(nums, target):
        residues = {}
        for idx, n in enumerate(nums):
            r_idx = (target - n)
            if n in residues.keys():
                return [residues[n], idx]
            residues[r_idx] = idx
        return [-1, -1]


if __name__ == '__main__':
    print(Solution.two_sums([3, 2, 4], 6))
    print(Solution.two_sums([-1, -2, -3, -4, -5], -8))
    print(Solution.two_sums([10, 15, 20, 30], 45))
