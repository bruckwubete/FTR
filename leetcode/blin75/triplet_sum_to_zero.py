class Solution:
    found_triples = []

    def search_triplets(self, arr):
        arr.sort()
        for i in range(len(arr) - 2):
            l, r = i + 1, len(arr) - 1
            while l < r:
                sum = arr[i] + arr[l] + arr[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    self.found_triples.append([arr[i], arr[l], arr[r]])
                    l += 1
                    r -= 1
        return self.found_triples


if __name__ == '__main__':
    s = Solution()
    print(s.search_triplets([-3, 0, 1, 2, -1, 1, -2]))
